# -*- encoding: utf-8 -*-
import os
import logging

from flask import url_for, request, Flask
from werkzeug.contrib.fixers import ProxyFix
from webapp.view import common_views,cwr_views,uso_views

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 33507))
    host = os.environ.get('HOST', '0.0.0.0')
    debug = bool(os.environ.get('DEBUG', True))
    secret = os.environ.get('SECRET_KEY', 'development_key')

    app = Flask(__name__)
    app.register_blueprint(common_views)
    app.register_blueprint(cwr_views)
    app.register_blueprint(uso_views)

    app.wsgi_app = ProxyFix(app.wsgi_app)

    app.config['DEBUG'] = debug
    app.config['SECRET_KEY'] = secret

    if debug:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(filename='cwr.log', level=logging.INFO, maxBytes=10000, backupCount=1)

    logging.info('Debug mode is set to %r' % debug)

    app.jinja_env.globals['url_for_other_page'] = url_for_other_page

    app.run(host=host, port=port)