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

    from flask import Flask
    from werkzeug.contrib.fixers import ProxyFix
    from cwr_webclient.view import common_blueprint, cwr_file_blueprint, cwr_contents_blueprint, \
        cwr_acknowledgement_blueprint, cwr_match_blueprint, cwr_upload_blueprint, mera_match_blueprint

    from cwr_webclient.uploads import __uploads__

    from cwr_webclient.service.appinfo import WESOApplicationInfoService
    from cwr_webclient.service.file import LocalFileService
    from cwr_webclient.service.match import WSMatchingService
    from cwr_webclient.service.pagination import DefaultPaginationService

    appinfo_service = WESOApplicationInfoService()

    debug = bool(os.environ.get('CWR_WEBCLIENT_DEBUG', True))
    secret = os.environ.get('CWR_WEBCLIENT_SECRET_KEY', os.urandom(24))
    upload = os.environ.get('CWR_WEBCLIENT_UPLOAD_FOLDER', __uploads__.path())

    match_ws = os.environ.get('CWR_WEBCLIENT_MATCH_WS', 'http://somewhere.org/cwr')

    app = Flask(__name__)
    app.register_blueprint(common_blueprint)
    app.register_blueprint(cwr_contents_blueprint, url_prefix='/cwr/contents')
    app.register_blueprint(cwr_acknowledgement_blueprint, url_prefix='/cwr/acknowledgement')
    app.register_blueprint(cwr_file_blueprint, url_prefix='/cwr/file')
    app.register_blueprint(cwr_upload_blueprint, url_prefix='/cwr/upload')
    app.register_blueprint(mera_match_blueprint, url_prefix='/cwr/match')

    app.wsgi_app = ProxyFix(app.wsgi_app)

    app.config['DEBUG'] = debug
    app.config['SECRET_KEY'] = secret
    app.config['UPLOAD_FOLDER'] = upload

    app.config['MATCH_WS'] = DefaultPaginationService()

    app.config['FILE_SERVICE'] = LocalFileService(app.config['UPLOAD_FOLDER'])
    app.config['MATCH_SERVICE'] = WSMatchingService(app.config['MATCH_WS'])
    app.config['PAGINATION_SERVICE'] = DefaultPaginationService()

    app.jinja_env.globals['company'] = appinfo_service.get_company()
    app.jinja_env.globals['application'] = appinfo_service.get_application()

    if debug:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(filename='cwr_webclient.log', level=logging.INFO, maxBytes=10000, backupCount=1)

    app.jinja_env.globals['url_for_other_page'] = _url_for_other_page

    return app