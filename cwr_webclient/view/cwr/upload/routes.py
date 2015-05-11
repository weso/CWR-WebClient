# -*- encoding: utf-8 -*-
from flask import render_template, redirect, url_for, request, flash, Blueprint, current_app


__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

cwr_upload_blueprint = Blueprint('cwr_upload', __name__,
                                 template_folder='templates',
                                 static_folder='static')

REJECTED_EXTENSIONS = set(['html', 'htm', 'php'])

"""
Upload routes.
"""


@cwr_upload_blueprint.route('/', methods=['GET'])
def upload():
    return render_template('cwr_upload.html')


@cwr_upload_blueprint.route('/', methods=['POST'])
def upload_handler():
    # Get the name of the uploaded file
    if 'file' in request.files:
        sent_file = request.files['file']
    else:
        flash('No file selected')
        return redirect(url_for('.upload'))

    if sent_file:
        file_service = current_app.config['FILE_SERVICE']

        file_id = file_service.save_file(sent_file, current_app.config['UPLOAD_FOLDER'])

        return redirect(url_for('cwr_crossroads.decisions'))
    else:
        flash('No file selected')
        return redirect(url_for('.upload'))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] not in REJECTED_EXTENSIONS
