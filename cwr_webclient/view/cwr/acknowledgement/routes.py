# -*- encoding: utf-8 -*-
from flask import render_template, Blueprint

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

cwr_acknowledgement_blueprint = Blueprint('cwr_acknowledgement', __name__,
                                          template_folder='templates')

"""
CWR acknowledgement routes.
"""


@cwr_acknowledgement_blueprint.route('/<string:file_id>/acknowledgement',
                                     methods=['GET'])
def report(file_id):
    return render_template('acknowledgement.html', file_id=file_id)
