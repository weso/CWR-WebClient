# -*- encoding: utf-8 -*-
import logging
import json

from flask import render_template, Blueprint, current_app, abort, make_response

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

mera_match_blueprint = Blueprint('mera_match', __name__,
                                 template_folder='templates')

_logger = logging.getLogger(__name__)

"""
Upload routes.
"""


@mera_match_blueprint.route('/<string:file_id>/summary/', methods=['GET'])
def summary(file_id):
    _logger.info('Checking summery for id %s' % file_id)

    data = _get_matches(file_id)

    return render_template('mera_match_summary.html', file_id=file_id,
                           matches=data)


@mera_match_blueprint.route('/<string:file_id>/results/', methods=['GET'])
def result(file_id):
    _logger.info('Checking results for id %s' % file_id)

    data = _get_matches(file_id)

    return render_template('mera_match_results.html', file_id=file_id,
                           matches=data)


@mera_match_blueprint.route('/<string:file_id>/report/', methods=['GET'])
def report(file_id):
    _logger.info('Checking summery for id %s' % file_id)

    report_service = current_app.config['CWR_MATCH_REPORT_SERVICE']

    report = report_service.generate_report_excel(_get_matches(file_id))

    response = make_response(report)

    response.headers["Content-Disposition"] = "attachment; filename=result.xlsx"
    response.headers[
        "Content-type"] = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    return response


def _get_matches(file_id):
    match_service = current_app.config['CWR_ADMIN_SERVICE']

    data = match_service.get_file(file_id)

    if not data or 'match' not in data:
        abort(404)

    return json.loads(data['match'])
