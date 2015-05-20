# -*- encoding: utf-8 -*-
import os

from cwr_webclient.uploads import __uploads__
from data_web.accessor_web import CWRWebConfiguration


__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

config_dict = CWRWebConfiguration().get_config()


class Config(object):
    os_env = os.environ

    SECRET_KEY = os_env.get('CWR_WEBCLIENT_SECRET', os.urandom(24))
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13
    ASSETS_DEBUG = False
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.

    # TODO: Should be removed
    UPLOAD_FOLDER = os_env.get('CWR_WEBCLIENT_UPLOAD', __uploads__.path())


class DevConfig(Config):
    """
    Development configuration.
    """
    ENV = 'dev'
    DEBUG = True
    DEBUG_TB_ENABLED = True
    ASSETS_DEBUG = True  # Don't bundle/minify static assets
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.


class TestConfig(Config):
    TESTING = True
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 1  # For faster tests
    WTF_CSRF_ENABLED = False  # Allows form testing