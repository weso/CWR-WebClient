# -*- encoding: utf-8 -*-
from flask import render_template, redirect, url_for, request, flash, Blueprint, current_app


__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

cwr_crossroads_blueprint = Blueprint('cwr_crossroads', __name__,
                                 template_folder='templates')

"""
Upload routes.
"""


@cwr_crossroads_blueprint.route('/', methods=['GET'])
def decisions():
    return render_template('cwr_crossroads.html')

