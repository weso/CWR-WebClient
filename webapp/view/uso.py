# -*- encoding: utf-8 -*-
from flask import render_template, Blueprint

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

uso_views = Blueprint('uso', __name__,
                      template_folder='templates',
                      static_folder='static')

"""
Upload routes.
"""


@uso_views.route('/uso/upload', methods=['GET'])
def upload():
    return render_template('uso/upload.html')