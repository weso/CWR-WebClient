# -*- encoding: utf-8 -*-
from flask import render_template, redirect, url_for, abort, Blueprint, \
    current_app, make_response
from cwr.parser.decoder.cwrjson import JSONDecoder

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

cwr_contents_blueprint = Blueprint('cwr_contents', __name__,
                                   template_folder='templates',
                                   static_folder='static',
                                   static_url_path='/static/cwr')

"""
CWR validation routes.
"""


@cwr_contents_blueprint.route('/<string:file_id>', methods=['GET'])
def summary(file_id):
    cwr_service = current_app.config['CWR_ADMIN_SERVICE']
    cwr = cwr_service.get_file(file_id)

    if not cwr or 'contents' not in cwr or not cwr['contents']:
        abort(404)

    cwr = cwr['contents']

    decoder = JSONDecoder()

    cwr = decoder.decode(cwr)

    groups = cwr.transmission.groups

    return render_template('summary.html', cwr=cwr, current_tab='summary_item',
                           groups=groups, file_id=file_id)


@cwr_contents_blueprint.route('/<string:file_id>/group/<int:index>',
                              defaults={'page': 1}, methods=['GET'])
@cwr_contents_blueprint.route(
    '/<string:file_id>/group/<int:index>/page/<int:page>', methods=['GET'])
def transactions(index, page, file_id):
    cwr_service = current_app.config['CWR_ADMIN_SERVICE']
    cwr = cwr_service.get_file(file_id)
    cwr = cwr['contents']

    if not cwr and page != 1:
        abort(404)

    decoder = JSONDecoder()

    cwr = decoder.decode(cwr)

    group = cwr.transmission.groups[index]

    pagination_service = current_app.config['PAGINATION_SERVICE']

    transactions = pagination_service.get_page_transactions(page, group)
    pagination = pagination_service.get_transactions_paginator(page, group)

    return render_template('transactions.html', paginator=pagination,
                           groups=cwr.transmission.groups,
                           group=group, transactions=transactions,
                           current_tab='agreements_item', file_id=file_id)


@cwr_contents_blueprint.route('/download', methods=['GET'])
def report_download():
    return redirect(url_for('.summary'))


@cwr_contents_blueprint.route('/<string:file_id>/report/', methods=['GET'])
def report(file_id):
    cwr_service = current_app.config['CWR_ADMIN_SERVICE']
    cwr = cwr_service.get_file(file_id)
    filename = cwr['name']

    if not cwr or 'contents' not in cwr or not cwr['contents']:
        abort(404)

    cwr = cwr['contents']

    decoder = JSONDecoder()

    cwr = decoder.decode(cwr)

    report_service = current_app.config['CWR_REPORT_SERVICE']

    report = report_service.generate_report_excel(cwr, filename)

    response = make_response(report)

    response.headers["Content-Disposition"] = "attachment; filename=result.xlsx"
    response.headers[
        "Content-type"] = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    return response
