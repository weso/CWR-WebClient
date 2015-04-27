# -*- encoding: utf-8 -*-
from flask import render_template, Blueprint


__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

cwr_database_blueprint = Blueprint('cwr_database', __name__,
                                   template_folder='templates')

"""
CWR waiting lists routes.
"""


@cwr_database_blueprint.route('/', methods=['GET'])
def list():
    return render_template('cwr_database.html')