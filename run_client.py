# -*- encoding: utf-8 -*-
from cwr_webclient import create_app
import os

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 33507))
    host = os.environ.get('HOST', '0.0.0.0')

    app = create_app()

    app.run(host=host, port=port)