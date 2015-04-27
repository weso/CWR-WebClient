# -*- encoding: utf-8 -*-
from flask import render_template, redirect, url_for, request, session, flash, Blueprint, current_app


__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

cwr_file_blueprint = Blueprint('cwr_file', __name__,
                               template_folder='templates',
                               static_folder='static')

REJECTED_EXTENSIONS = set(['html', 'htm', 'php'])

"""
Upload routes.
"""


@cwr_file_blueprint.route('/upload', methods=['GET'])
def upload():
    return render_template('cwr_upload.html')


@cwr_file_blueprint.route('/upload', methods=['POST'])
def upload_handler():
    # Get the name of the uploaded file
    sent_file = request.files['file']

    if sent_file:
        file_service = current_app.config['FILE_SERVICE']

        file_id = file_service.save_file(sent_file, current_app.config['UPLOAD_FOLDER'])

        session['cwr_file_id'] = file_id

        return redirect(url_for('cwr_validation.report'))
    else:
        flash('No file selected')
        return redirect(url_for('.upload'))


@cwr_file_blueprint.route('/file', methods=['GET'])
def list():
    file_service = current_app.config['FILE_SERVICE']

    files = file_service.get_files()

    return render_template('cwr_file_listing.html', files=files)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] not in REJECTED_EXTENSIONS
