# -*- encoding: utf-8 -*-
from flask import render_template, redirect, url_for, request, flash, Blueprint

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

uso_upload_blueprint = Blueprint('uso_upload', __name__,
                                 template_folder='templates',
                                 static_folder='static')

REJECTED_EXTENSIONS = set(['html', 'htm', 'php'])

"""
Upload routes.
"""


@uso_upload_blueprint.route('/', methods=['GET'])
def upload():
    return render_template('uso_upload.html')


@uso_upload_blueprint.route('/', methods=['POST'])
def upload_handler():
    # Get the name of the uploaded file
    if 'file' in request.files:
        sent_file = request.files['file']
    else:
        flash('No file selected')
        return redirect(url_for('.upload'))

    if sent_file:
        # admin_service = current_app.config['CWR_ADMIN_SERVICE']

        # file_id = admin_service.process(sent_file)

        # return redirect(url_for('mera_match.setup_match', file_id=file_id))
        return redirect(url_for('cwr_file.list'))
    else:
        flash('No file selected')
        return redirect(url_for('.upload'))


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[
                                   1] not in REJECTED_EXTENSIONS
