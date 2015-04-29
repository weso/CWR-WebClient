# -*- encoding: utf-8 -*-
from flask import render_template, Blueprint, current_app


__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

mera_match_blueprint = Blueprint('mera_match', __name__,
                                 template_folder='templates')

REJECTED_EXTENSIONS = set(['html', 'htm', 'php'])

"""
Upload routes.
"""


@mera_match_blueprint.route('/<int:file_id>', methods=['GET'])
def result(file_id):
    match_service = current_app.config['MATCH_SERVICE']
    file_service = current_app.config['FILE_SERVICE']

    data = file_service.get_file(file_id).contents
    data = file_service.generate_json(data)
    data = match_service.match(data)

    return render_template('mera_match.html', file_id=file_id, matches=data)
