# -*- encoding: utf-8 -*-
from flask import render_template, Blueprint

from cwr_webclient.config import app_conf, view_conf
from cwr_webclient.service.cwr_file import LocalCWRFileService
from cwr_webclient.service.match import LocalMatchingService
from cwr_webclient.service.pagination import DefaultPaginationService


__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

common_blueprint = Blueprint('common_views', __name__,
                             template_folder='templates',
                             static_folder='static',
                             static_url_path='/static/common')

PER_PAGE = view_conf.per_page

cwr_service = LocalCWRFileService()
match_service = LocalMatchingService()
pagination_service = DefaultPaginationService()

"""
Basic routes.
"""


@common_blueprint.route('/', methods=['GET'])
def index():
    return render_template('index.html', app_title=app_conf.title)


