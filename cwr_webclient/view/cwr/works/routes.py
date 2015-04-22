# -*- encoding: utf-8 -*-
from flask import render_template, Blueprint

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

cwr_works_blueprint = Blueprint('cwr_works', __name__,
                                template_folder='templates')

"""
CWR waiting lists routes.
"""


@cwr_works_blueprint.route('/', methods=['GET'])
def works():
    return render_template('cwr_lists.html')