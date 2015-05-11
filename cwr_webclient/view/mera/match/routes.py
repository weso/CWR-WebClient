# -*- encoding: utf-8 -*-
import logging

from flask import render_template, Blueprint, current_app


__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

mera_match_blueprint = Blueprint('mera_match', __name__,
                                 template_folder='templates')

REJECTED_EXTENSIONS = set(['html', 'htm', 'php'])

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
        _logger.info('No data found')
        data = []

    return render_template('mera_match.html', file_id=file_id, matches=data)
