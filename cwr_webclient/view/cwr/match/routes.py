# -*- encoding: utf-8 -*-
from flask import render_template, redirect, url_for, Blueprint, current_app, abort

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

cwr_match_blueprint = Blueprint('cwr_match', __name__,
                                template_folder='templates')

"""
CWR matching routes.
"""


@cwr_match_blueprint.route('/', methods=['GET'])
def match():
    match_service = current_app.config['MATCH_SERVICE']
    sources = match_service.get_sources()

    if not sources:
        abort(404)

    return render_template('match.html', sources=sources)


@cwr_match_blueprint.route('/report', methods=['GET'])
def report():
    result = {}

    match_service = current_app.config['MATCH_SERVICE']
    result['pairs'] = match_service.get_match_pairs()

    return render_template('match_result.html', result=result)


@cwr_match_blueprint.route('/report/download', methods=['GET'])
def report_download():
    return redirect(url_for('.report'))


@cwr_match_blueprint.route('/edit', methods=['GET'])
def edit():
    result = {}

    match_service = current_app.config['MATCH_SERVICE']

    result['pairs'] = match_service.get_match_pairs()

    options = match_service.get_match_options()

    if not options:
        abort(404)

    return render_template('match_edit.html', result=result, options=options)
