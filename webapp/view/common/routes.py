# -*- encoding: utf-8 -*-
from flask import render_template, Blueprint

from webapp.config import app_conf, view_conf
from webapp.service.cwr import LocalCWRFileService
from webapp.service.match import LocalMatchingService
from webapp.service.pagination import DefaultPaginationService


__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

common_blueprint = Blueprint('common_views', __name__,
                             template_folder='templates',
                             static_folder='static')

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


