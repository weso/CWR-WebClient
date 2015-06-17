# -*- encoding: utf-8 -*-
import logging
import json

from flask import render_template, Blueprint, current_app

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

mera_match_blueprint = Blueprint('mera_match', __name__,
                                 template_folder='templates')

_logger = logging.getLogger(__name__)

"""
Upload routes.
"""


@mera_match_blueprint.route('/<string:file_id>', methods=['GET'])
def result(file_id):
    _logger.info('Checking results for id %s' % file_id)

    match_service = current_app.config['CWR_ADMIN_SERVICE']

    data = json.loads(match_service.get_file(file_id)['match'])

    print data
    print data.__class__.__name__

    if not data:
        _logger.info('No data found')
        data = []

    return render_template('mera_match.html', file_id=file_id, matches=data)
