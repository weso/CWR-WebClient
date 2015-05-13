# -*- encoding: utf-8 -*-
import logging

from flask import render_template, Blueprint, current_app, redirect, url_for, request
from cwr.parser.encoder.cwrjson import JSONEncoder


__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

mera_match_blueprint = Blueprint('mera_match', __name__,
                                 template_folder='templates')

_logger = logging.getLogger(__name__)

"""
Upload routes.
"""


@mera_match_blueprint.route('/<int:file_id>', methods=['GET'])
def result(file_id):
    _logger.info('Checking results for id %s' % file_id)

    match_service = current_app.config['MATCH_SERVICE']

    data = match_service.get_match_result(file_id)

    if not data:
        _logger.info('No data found for file_id %s' % file_id)
        data = []

    return render_template('mera_match.html', file_id=file_id, matches=data)


@mera_match_blueprint.route('/setup/<int:file_id>', methods=['GET'])
def setup_match(file_id):
    return render_template('send_match.html', file_id=file_id)


@mera_match_blueprint.route('/send/<int:file_id>', methods=['POST'])
def send_match(file_id):
    match_service = current_app.config['MATCH_SERVICE']
    file_service = current_app.config['FILE_SERVICE']

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

    encoder_json = JSONEncoder()

    data = file_service.get_file(file_id).contents

    json_data = encoder_json.encode(data)

    match_service.match(json_data, file_id, config_dict)

    return redirect(url_for('cwr_file.list'))
