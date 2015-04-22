# -*- encoding: utf-8 -*-
from flask import render_template, redirect, url_for, request, session, flash, Blueprint, current_app

from cwr_webclient.service.file import LocalFileService

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

cwr_upload_blueprint = Blueprint('cwr_upload', __name__,
                                 template_folder='templates',
                                 static_folder='static')

file_service = LocalFileService()

"""
Upload routes.
"""


@cwr_upload_blueprint.route('/upload', methods=['GET'])
def upload():
    return render_template('upload_cwr.html')


@cwr_upload_blueprint.route('/upload', methods=['POST'])
def upload_handler():
    # Get the name of the uploaded file
    sent_file = request.files['file']

    if sent_file:
        file_id = file_service.save_file(sent_file, current_app.config['UPLOAD_FOLDER'])

        session['cwr_file_id'] = file_id

        return redirect(url_for('cwr_validation.report'))
    else:
        flash('No file selected')
        return redirect(url_for('.upload'))


REJECTED_EXTENSIONS = set(['html', 'htm', 'php'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] not in REJECTED_EXTENSIONS
