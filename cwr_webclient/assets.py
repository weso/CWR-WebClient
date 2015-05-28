# -*- coding: utf-8 -*-

from flask_assets import Bundle, Environment

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

css = Bundle(
    'common/libs/bootstrap/dist/css/bootstrap.css',
    'common/css/style.css',
    filters='cssmin',
    output='public/css/common.css'
)

js = Bundle(
    'common/libs/bootstrap/dist/js/bootstrap.js',
    filters='jsmin',
    output='public/js/common.js'
)

assets = Environment()

assets.register('js_all', js)
assets.register('css_all', css)
