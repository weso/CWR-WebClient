# -*- coding: utf-8 -*-

from flask_cache import Cache
from flask_debugtoolbar import DebugToolbarExtension

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

cache = Cache()

debug_toolbar = DebugToolbarExtension()
