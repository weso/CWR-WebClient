# -*- encoding: utf-8 -*-
from flask import render_template, Blueprint

from cwr_webclient.config import view_conf
from cwr_webclient.service.cwr_file import LocalCWRFileService
from cwr_webclient.service.file import LocalFileService
from cwr_webclient.service.match import LocalMatchingService
from cwr_webclient.service.pagination import DefaultPaginationService

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

cwr_acknowledgement_blueprint = Blueprint('cwr_acknowledgement', __name__,
                                          template_folder='templates')

PER_PAGE = view_conf.per_page

cwr_service = LocalCWRFileService()
file_service = LocalFileService()
match_service = LocalMatchingService()
pagination_service = DefaultPaginationService()

"""
CWR acknowledgement routes.
"""


@cwr_acknowledgement_blueprint.route('/acknowledgement', methods=['GET'])
def report():
    return render_template('acknowledgement.html')