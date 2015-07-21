# -*- encoding: utf-8 -*-
import logging
import json

from flask import render_template, Blueprint, current_app, abort, make_response, \
    redirect, url_for, request

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
    cwr_service = current_app.config['CWR_ADMIN_SERVICE']
    cwr = cwr_service.get_file(file_id)
    filename = cwr['name']

    _logger.info('Generating match report for id %s' % file_id)

    report_service = current_app.config['CWR_MATCH_REPORT_SERVICE']

    report = report_service.generate_report_excel(_get_matches(file_id),
                                                  filename)

    response = make_response(report)

    response.headers["Content-Disposition"] = "attachment; filename=result.xlsx"
    response.headers[
        "Content-type"] = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    return response


@mera_match_blueprint.route('/begin/<string:file_id>', methods=['GET'])
def begin(file_id):
    _logger.info('Beginning match for id %s' % file_id)

    return render_template('mera_match_send.html', file_id=file_id)


@mera_match_blueprint.route('/feedback/<string:file_id>', methods=['GET'])
def feedback(file_id):
    _logger.info('Sending feedback for id %s' % file_id)

    match_service = current_app.config['CWR_ADMIN_SERVICE']

    match_service.send_feedback(file_id)

    return redirect(url_for('cwr_file.list'))


@mera_match_blueprint.route('/reject/<string:file_id><int:pos>',
                            methods=['GET'])
def reject_match(file_id, pos):
    _logger.info('Rejecting match #%s for id %s' % (pos, file_id))

    cwr_service = current_app.config['CWR_ADMIN_SERVICE']

    cwr_service.reject_match(file_id, pos)

    return redirect(url_for('.result', file_id=file_id))


@mera_match_blueprint.route('/confirm/<string:file_id><int:pos>',
                            methods=['GET'])
def confirm_match(file_id, pos):
    _logger.info('Confirming match #%s for id %s' % (pos, file_id))

    cwr_service = current_app.config['CWR_ADMIN_SERVICE']

    cwr_service.confirm_match(file_id, pos)

    return redirect(url_for('.result', file_id=file_id))


@mera_match_blueprint.route('/send/<string:file_id>', methods=['POST'])
def send_match(file_id):
    config = request.form

    config_dict = {}

    config_subdict = {
        'blocking_function': float(config['blocking_function']),
        'result_query': int(config['result_query'])
    }
    config_dict['blocking'] = config_subdict

    config_subdict = {
        "threshold": float(config['findsong.threshold']),
        "relevances": {
            "artist": float(config['relevances.artist'])
        }
    }
    config_dict['commands'] = {
        "find_song": config_subdict
    }

    config_dict['fields'] = {
        "song": {
            "threshold": float(config['song.threshold'])
        },
        "artist": {
            "threshold": float(config['artist.threshold'])
        }
    }

    match_service = current_app.config['CWR_ADMIN_SERVICE']

    match_service.begin_match(file_id, config_dict)

    return redirect(url_for('cwr_file.list'))


def _get_matches(file_id):
    match_service = current_app.config['CWR_ADMIN_SERVICE']

    data = match_service.get_file(file_id)

    if not data or 'match' not in data or not data['match']:
        abort(404)

    return json.loads(data['match'])
