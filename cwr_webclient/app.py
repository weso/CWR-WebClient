# -*- encoding: utf-8 -*-

"""
Web app module.
"""

import os
import logging
from logging.handlers import RotatingFileHandler
from logging import Formatter

from flask import Flask, render_template
from werkzeug.contrib.fixers import ProxyFix

from cwr_webclient.extensions import debug_toolbar, cache, bcrypt
from cwr_webclient.view import *
from cwr_webclient.config import DevConfig
from cwr_webclient.service import DefaultPaginationService, \
    WESOApplicationInfoService, WSCWRService
from data_web.accessor_web import CWRWebConfiguration

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


def _url_for_other_page(page):
    from flask import url_for, request

    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)


def _config_templating(app):
    appinfo_service = WESOApplicationInfoService()

    app.jinja_env.globals['company'] = appinfo_service.get_company()
    app.jinja_env.globals['application'] = appinfo_service.get_application()


def _register_extensions(app):
    bcrypt.init_app(app)
    cache.init_app(app)
    debug_toolbar.init_app(app)


def _register_errorhandlers(app):
    def render_error(error):
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template("{0}.html".format(error_code)), error_code

    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None


def _load_services(app, config):
    match_ws = config['ws.match']
    match_ws_results = config['ws.match.results']
    match_ws_status = config['ws.match.status']

    if len(match_ws) == 0:
        match_ws = os.environ.get('CWR_WEBCLIENT_MATCH_WS',
                                  'http://127.0.0.1:33567/cwr/')

    if len(match_ws_results) == 0:
        match_ws_results = os.environ.get('CWR_WEBCLIENT_MATCH_WS_RESULTS',
                                          'http://127.0.0.1:33567/cwr/results/')

    if len(match_ws_status) == 0:
        match_ws_status = os.environ.get('CWR_WEBCLIENT_MATCH_WS_STATUS',
                                         'http://127.0.0.1:33567/cwr/status/')

    service_admin = WSCWRService('http://127.0.0.1:33508/cwr/process/',
                                 'http://127.0.0.1:33508/cwr/files/')

    app.config['CWR_ADMIN_SERVICE'] = service_admin
    app.config['PAGINATION_SERVICE'] = DefaultPaginationService(
        int(config['perpage']))


def _register_blueprints(app):
    app.register_blueprint(common_blueprint)
    app.register_blueprint(cwr_contents_blueprint, url_prefix='/cwr/contents')
    app.register_blueprint(cwr_acknowledgement_blueprint,
                           url_prefix='/cwr/acknowledgement')
    app.register_blueprint(cwr_file_blueprint, url_prefix='/cwr/file')
    app.register_blueprint(cwr_upload_blueprint, url_prefix='/cwr/upload')
    app.register_blueprint(mera_match_blueprint, url_prefix='/mera/match')
    app.register_blueprint(uso_upload_blueprint, url_prefix='/uso/upload')


def create_app(config_object=DevConfig):
    config = CWRWebConfiguration().get_config()

    app = Flask(__name__)
    app.config.from_object(config_object)
    _register_extensions(app)
    _load_services(app, config)
    _config_templating(app)
    _register_blueprints(app)
    _register_errorhandlers(app)

    app.wsgi_app = ProxyFix(app.wsgi_app)

    if app.config['DEBUG']:
        log = config['log.folder']
        if len(log) == 0:
            log = 'cwr_webapp.log'

        handler = RotatingFileHandler(log, maxBytes=10000, backupCount=1)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(
            Formatter('[%(levelname)s][%(asctime)s] %(message)s'))

        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger('').addHandler(handler)

        app.logger.addHandler(handler)

    app.jinja_env.globals['url_for_other_page'] = _url_for_other_page

    return app
