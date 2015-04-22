# -*- encoding: utf-8 -*-
from flask import render_template, redirect, url_for, Blueprint

from cwr_webclient.config import view_conf
from cwr_webclient.service.cwr_file import LocalCWRFileService
from cwr_webclient.service.file import LocalFileService
from cwr_webclient.service.match import LocalMatchingService
from cwr_webclient.service.pagination import DefaultPaginationService

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

cwr_match_blueprint = Blueprint('cwr_match', __name__,
                                template_folder='templates')

PER_PAGE = view_conf.per_page

cwr_service = LocalCWRFileService()
file_service = LocalFileService()
match_service = LocalMatchingService()
pagination_service = DefaultPaginationService()

"""
CWR matching routes.
"""


@cwr_match_blueprint.route('/', methods=['GET'])
def match():
    sources = match_service.get_sources()
    return render_template('match.html', sources=sources)


@cwr_match_blueprint.route('/report', methods=['GET'])
def report():
    result = {}

    result['pairs'] = match_service.get_match_pairs()

    return render_template('match_result.html', result=result)


@cwr_match_blueprint.route('/report/download', methods=['GET'])
def report_download():
    return redirect(url_for('.report'))


@cwr_match_blueprint.route('/edit', methods=['GET'])
def edit():
    result = {}

    result['pairs'] = match_service.get_match_pairs()

    options = match_service.get_match_options()

    return render_template('match_edit.html', result=result, options=options)
