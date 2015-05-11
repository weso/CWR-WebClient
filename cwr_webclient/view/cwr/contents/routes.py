# -*- encoding: utf-8 -*-
from flask import render_template, redirect, url_for, abort, Blueprint, current_app

from cwr_webclient.config import view_conf


__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

cwr_contents_blueprint = Blueprint('cwr_contents', __name__,
                                   template_folder='templates',
                                   static_folder='static',
                                   static_url_path='/static/cwr')

PER_PAGE = view_conf.per_page

"""
CWR validation routes.
"""


@cwr_contents_blueprint.route('/<int:file_id>', methods=['GET'])
def summary(file_id):
    cwr_service = current_app.config['FILE_SERVICE']
    cwr = cwr_service.get_file(file_id)

    if not cwr:
        abort(404)

    cwr = cwr.contents

    groups = cwr.transmission.groups

    return render_template('summary.html', cwr=cwr, current_tab='summary_item',
                           groups=groups, file_id=file_id)


@cwr_contents_blueprint.route('/<int:file_id>/group/<int:index>', defaults={'page': 1}, methods=['GET'])
@cwr_contents_blueprint.route('/<int:file_id>/group/<int:index>/page/<int:page>', methods=['GET'])
def transactions(index, page, file_id):
    cwr_service = current_app.config['FILE_SERVICE']
    cwr = cwr_service.get_file(file_id).contents

    if not cwr and page != 1:
        abort(404)

    group = cwr.transmission.groups[index]

    pagination_service = current_app.config['PAGINATION_SERVICE']

    transactions = pagination_service.get_page_transactions(page, group)
    pagination = pagination_service.get_transactions_paginator(page, group)

    return render_template('transactions.html', paginator=pagination, groups=cwr.transmission.groups,
                           group=group, transactions=transactions, current_tab='agreements_item', file_id=file_id)


@cwr_contents_blueprint.route('/download', methods=['GET'])
def report_download():
    return redirect(url_for('.summary'))
