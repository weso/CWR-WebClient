# -*- encoding: utf-8 -*-
from flask import render_template, redirect, url_for, abort, request, session, flash, Blueprint

from webapp.config import app_conf, view_conf
from webapp.service.cwr import LocalCWRFileService
from webapp.service.match import LocalMatchingService
from webapp.service.pagination import DefaultPaginationService


__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

common_views = Blueprint('common_views', __name__,
                        template_folder='templates',
                        static_folder='static')

PER_PAGE = view_conf.per_page

cwr_service = LocalCWRFileService()
match_service = LocalMatchingService()
pagination_service = DefaultPaginationService()

"""
Basic routes.
"""


@common_views.route('/', methods=['GET'])
def index():
    return render_template('index.html', app_title=app_conf.title)


"""
Upload routes.
"""


@common_views.route('/cwr/upload', methods=['GET'])
def upload_cwr():
    return render_template('cwr/upload.html')


@common_views.route('/upload/cwr', methods=['POST'])
def upload_cwr_handler():
    # Get the name of the uploaded file
    sent_file = request.files['file']

    if sent_file:
        file_id = cwr_service.save_file(sent_file)

        session['cwr_file_id'] = file_id

        return redirect(url_for('.cwr_validation_report'))
    else:
        flash('No file selected')
        return redirect(url_for('.upload_cwr'))


@common_views.route('/uso/upload', methods=['GET'])
def upload_uso():
    return render_template('uso/upload.html')


"""
CWR matching routes.
"""


@common_views.route('/cwr/match', methods=['GET'])
def cwr_match():
    sources = match_service.get_sources()
    return render_template('cwr/match.html', sources=sources)


@common_views.route('/cwr/match/report', methods=['GET'])
def cwr_match_report():
    result = {}

    result['pairs'] = match_service.get_match_pairs()

    return render_template('cwr/match_result.html', result=result)


@common_views.route('/cwr/match/report/download', methods=['GET'])
def cwr_match_report_download():
    return redirect(url_for('.match_report'))


@common_views.route('/cwr/match/edit', methods=['GET'])
def cwr_match_edit():
    result = {}

    result['pairs'] = match_service.get_match_pairs()

    options = match_service.get_match_options()

    return render_template('cwr/match_edit.html', result=result, options=options)


"""
CWR validation routes.
"""


@common_views.route('/cwr/validation/report', methods=['GET'])
def cwr_validation_report():
    cwr = cwr_service.get_data(session['cwr_file_id'])

    return render_template('cwr/report/summary.html', cwr=cwr, current_tab='summary_item',
                           groups=cwr.transmission.groups)


@common_views.route('/cwr/validation/report/group/<int:index>', defaults={'page': 1}, methods=['GET'])
@common_views.route('/cwr/validation/report/group/<int:index>/page/<int:page>', methods=['GET'])
def cwr_validation_report_transactions(index, page):
    cwr = cwr_service.get_data(session['cwr_file_id'])

    if not cwr and page != 1:
        abort(404)

    group = cwr.transmission.groups[index]

    transactions = pagination_service.get_page_transactions(page, group)
    pagination = pagination_service.get_transactions_paginator(page, group)

    return render_template('cwr/report/transactions.html', paginator=pagination, groups=cwr.transmission.groups,
                           group=group, transactions=transactions, current_tab='agreements_item')


@common_views.route('/cwr/validation/report/download', methods=['GET'])
def cwr_validation_report_download():
    return redirect(url_for('.validation_report'))


"""
CWR acknowledgement routes.
"""


@common_views.route('/cwr/acknowledgement', methods=['GET'])
def cwr_acknowledgement_generation():
    return render_template('cwr/acknowledgement.html')