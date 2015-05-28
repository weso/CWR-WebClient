# -*- encoding: utf-8 -*-
from cwr_webclient import create_app
import os
from cwr_webclient.config import DevConfig, ProdConfig

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


if __name__ == '__main__':
    port = int(os.environ.get('CWR_WEB_CLIENT_PORT', 33507))
    host = os.environ.get('CWR_WEB_CLIENT_HOST', '127.0.0.1')
    env = os.environ.get('CWR_WEB_CLIENT_ENV', 'dev')

    if env == 'prod':
        app = create_app(ProdConfig)
    else:
        app = create_app(DevConfig)

    app.run(host=host, port=port)
