# -*- encoding: utf-8 -*-
from flask import render_template, Blueprint, current_app

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

cwr_file_blueprint = Blueprint('cwr_file', __name__,
                               template_folder='templates',
                               static_folder='static')


@cwr_file_blueprint.route('/', methods=['GET'])
def list():
    file_service = current_app.config['CWR_ADMIN_SERVICE']

    files = file_service.get_files()

    if not files:
        files = []

    return render_template('cwr_file_listing.html', files=files)


@cwr_file_blueprint.route('/search', methods=['GET'])
def search():
    return render_template('cwr_search.html')
