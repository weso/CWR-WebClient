# -*- encoding: utf-8 -*-
from flask import render_template, redirect, url_for, abort, session, Blueprint, current_app

from cwr_webclient.config import view_conf
from cwr_webclient.service.cwr_file import LocalCWRFileService
from cwr_webclient.service.file import LocalFileService
from cwr_webclient.service.match import LocalMatchingService
from cwr_webclient.service.pagination import DefaultPaginationService

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

cwr_validation_blueprint = Blueprint('cwr_validation', __name__,
                                     template_folder='templates',
                                     static_folder='static',
                                     static_url_path='/static/cwr')

PER_PAGE = view_conf.per_page

cwr_service = LocalCWRFileService()
file_service = LocalFileService()
match_service = LocalMatchingService()
pagination_service = DefaultPaginationService()

"""
CWR validation routes.
"""


@cwr_validation_blueprint.route('/report', methods=['GET'])
def report():
    cwr = cwr_service.get_data(session['cwr_file_id'], current_app.config['UPLOAD_FOLDER'])

    return render_template('summary.html', cwr=cwr, current_tab='summary_item',
                           groups=cwr.transmission.groups)


@cwr_validation_blueprint.route('/report/group/<int:index>', defaults={'page': 1}, methods=['GET'])
@cwr_validation_blueprint.route('/report/group/<int:index>/page/<int:page>', methods=['GET'])
def report_transactions(index, page):
    cwr = cwr_service.get_data(session['cwr_file_id'], current_app.config['UPLOAD_FOLDER'])

    if not cwr and page != 1:
        abort(404)

    group = cwr.transmission.groups[index]

    transactions = pagination_service.get_page_transactions(page, group)
    pagination = pagination_service.get_transactions_paginator(page, group)

    return render_template('transactions.html', paginator=pagination, groups=cwr.transmission.groups,
                           group=group, transactions=transactions, current_tab='agreements_item')


@cwr_validation_blueprint.route('/download', methods=['GET'])
def report_download():
    return redirect(url_for('.report'))
