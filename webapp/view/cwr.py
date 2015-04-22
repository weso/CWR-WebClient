# -*- encoding: utf-8 -*-
from flask import render_template, redirect, url_for, abort, request, session, flash, Blueprint

from webapp.config import view_conf
from webapp.service.cwr import LocalCWRFileService
from webapp.service.match import LocalMatchingService
from webapp.service.pagination import DefaultPaginationService

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

cwr_views = Blueprint('cwr', __name__,
                      template_folder='templates',
                      static_folder='static')

PER_PAGE = view_conf.per_page

cwr_service = LocalCWRFileService()
match_service = LocalMatchingService()
pagination_service = DefaultPaginationService()

"""
Upload routes.
"""


@cwr_views.route('/cwr/upload', methods=['GET'])
def upload():
    return render_template('cwr/upload.html')


@cwr_views.route('/upload/cwr', methods=['POST'])
def upload_handler():
    # Get the name of the uploaded file
    sent_file = request.files['file']

    if sent_file:
        file_id = cwr_service.save_file(sent_file)

        session['cwr_file_id'] = file_id

        return redirect(url_for('.validation_report'))
    else:
        flash('No file selected')
        return redirect(url_for('.upload_cwr'))


"""
CWR matching routes.
"""


@cwr_views.route('/cwr/match', methods=['GET'])
def match():
    sources = match_service.get_sources()
    return render_template('cwr/match.html', sources=sources)


@cwr_views.route('/cwr/match/report', methods=['GET'])
def match_report():
    result = {}

    result['pairs'] = match_service.get_match_pairs()

    return render_template('cwr/match_result.html', result=result)


@cwr_views.route('/cwr/match/report/download', methods=['GET'])
def match_report_download():
    return redirect(url_for('.match_report'))


@cwr_views.route('/cwr/match/edit', methods=['GET'])
def match_edit():
    result = {}

    result['pairs'] = match_service.get_match_pairs()

    options = match_service.get_match_options()

    return render_template('cwr/match_edit.html', result=result, options=options)


"""
CWR validation routes.
"""


@cwr_views.route('/cwr/validation/report', methods=['GET'])
def validation_report():
    cwr = cwr_service.get_data(session['cwr_file_id'])

    return render_template('cwr/report/summary.html', cwr=cwr, current_tab='summary_item',
                           groups=cwr.transmission.groups)


@cwr_views.route('/cwr/validation/report/group/<int:index>', defaults={'page': 1}, methods=['GET'])
@cwr_views.route('/cwr/validation/report/group/<int:index>/page/<int:page>', methods=['GET'])
def validation_report_transactions(index, page):
    cwr = cwr_service.get_data(session['cwr_file_id'])

    if not cwr and page != 1:
        abort(404)

    group = cwr.transmission.groups[index]

    transactions = pagination_service.get_page_transactions(page, group)
    pagination = pagination_service.get_transactions_paginator(page, group)

    return render_template('cwr/report/transactions.html', paginator=pagination, groups=cwr.transmission.groups,
                           group=group, transactions=transactions, current_tab='agreements_item')


@cwr_views.route('/cwr/validation/report/download', methods=['GET'])
def validation_report_download():
    return redirect(url_for('.validation_report'))


"""
CWR acknowledgement routes.
"""


@cwr_views.route('/cwr/acknowledgement', methods=['GET'])
def acknowledgement_generation():
    return render_template('cwr/acknowledgement.html')