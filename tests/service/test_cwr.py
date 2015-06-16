# -*- coding: utf-8 -*-

import unittest
import StringIO

from cwr_webclient.service.cwr import WSCWRService

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestWSCWRServiceNoService(unittest.TestCase):
    def setUp(self):
        self._service = WSCWRService('http://127.0.0.1:1', 'http://127.0.0.1:1')

    def test_process(self):
        file = StringIO.StringIO('text1')
        file.filename = 'filename'

        self._service.process(file)
