# -*- encoding: utf-8 -*-
from flask import render_template, Blueprint

from cwr_webclient import app_conf


__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

common_blueprint = Blueprint('common_views', __name__,
                             template_folder='templates',
                             static_folder='static',
                             static_url_path='/static/common')

"""
Basic routes.
"""


@common_blueprint.route('/', methods=['GET'])
def index():
    return render_template('index.html', app_title=app_conf.title)


