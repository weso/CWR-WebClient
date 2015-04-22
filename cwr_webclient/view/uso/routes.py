# -*- encoding: utf-8 -*-
from flask import render_template, Blueprint

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

uso_blueprint = Blueprint('uso', __name__,
                          template_folder='templates')

"""
Upload routes.
"""


@uso_blueprint.route('/upload', methods=['GET'])
def upload():
    return render_template('upload_uso.html')