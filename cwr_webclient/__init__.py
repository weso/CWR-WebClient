# -*- coding: utf-8 -*-
"""
    CWR Web Client
    ~~~~~~~~~~~~~~
    Client for CWR services.
    :copyright: (c) 2015 by WESO
    :license: MIT, see LICENSE for more details.
"""

__version__ = '0.0.1'
__license__ = 'MIT'


def _url_for_other_page(page):
    from flask import url_for, request

    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)


def create_app():
    import os
    import logging
    from logging.handlers import RotatingFileHandler
    from logging import Formatter

    from flask import Flask
    from werkzeug.contrib.fixers import ProxyFix
    from cwr_webclient.view import common_blueprint, cwr_file_blueprint, cwr_contents_blueprint, \
        cwr_acknowledgement_blueprint, cwr_match_blueprint, cwr_upload_blueprint, mera_match_blueprint, \
        cwr_crossroads_blueprint

    from cwr_webclient.uploads import __uploads__

    from cwr_webclient.service.appinfo import WESOApplicationInfoService
    from cwr_webclient.service.file import LocalFileService
    from cwr_webclient.service.match import WSMatchingService, TestMatchingService, MatchingFileProcessor, \
        MatchingStatusChecker
    from cwr_webclient.service.pagination import DefaultPaginationService

    from data_web.accessor_web import CWRWebConfiguration

    appinfo_service = WESOApplicationInfoService()

    config = CWRWebConfiguration()
    config = config.get_config()

    debug = bool(config['debug'])
    secret = config['secretKey']
    if len(secret) == 0:
        secret = os.urandom(24)
    upload = config['upload.folder']
    if len(upload) == 0:
        upload = __uploads__.path()
    log = config['log.folder']
    if len(log) == 0:
        log = 'cwr_webapp.log'

    # match_ws = os.environ.get('CWR_WEBCLIENT_MATCH_WS', 'http://127.0.0.1:33567/cwr/')
    # match_ws_results = os.environ.get('CWR_WEBCLIENT_MATCH_WS_RESULTS', 'http://127.0.0.1:33567/cwr/results')
    # match_ws_status = os.environ.get('CWR_WEBCLIENT_MATCH_WS_STATUS', 'http://127.0.0.1:33567/cwr/status')
    match_ws = config['ws.match']
    match_ws_results = config['ws.match.results']
    match_ws_status = config['ws.match.status']

    app = Flask(__name__)
    app.register_blueprint(common_blueprint)
    app.register_blueprint(cwr_contents_blueprint, url_prefix='/cwr/contents')
    app.register_blueprint(cwr_acknowledgement_blueprint, url_prefix='/cwr/acknowledgement')
    app.register_blueprint(cwr_file_blueprint, url_prefix='/cwr/file')
    app.register_blueprint(cwr_upload_blueprint, url_prefix='/cwr/upload')
    app.register_blueprint(mera_match_blueprint, url_prefix='/cwr/match')
    # app.register_blueprint(cwr_crossroads_blueprint, url_prefix='/cwr/crossroads')

    app.wsgi_app = ProxyFix(app.wsgi_app)

    app.config['DEBUG'] = debug
    app.config['SECRET_KEY'] = secret
    app.config['UPLOAD_FOLDER'] = upload

    app.config['MATCH_SERVICE'] = WSMatchingService(match_ws, match_ws_results)

    checker = MatchingStatusChecker(app.config['MATCH_SERVICE'], match_ws_status)

    app.config['FILE_SERVICE'] = LocalFileService(app.config['UPLOAD_FOLDER'], checker)
    # app.config['MATCH_SERVICE'] = TestMatchingService()
    app.config['PAGINATION_SERVICE'] = DefaultPaginationService()

    app.jinja_env.globals['company'] = appinfo_service.get_company()
    app.jinja_env.globals['application'] = appinfo_service.get_application()

    app.config['FILE_SERVICE'].register_processor(MatchingFileProcessor(app.config['MATCH_SERVICE']))

    if debug:
        handler = RotatingFileHandler(log, maxBytes=10000, backupCount=1)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(Formatter('[%(levelname)s][%(asctime)s] %(message)s'))

        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger('').addHandler(handler)

        app.logger.addHandler(handler)

    app.jinja_env.globals['url_for_other_page'] = _url_for_other_page

    return app