# -*- coding: utf-8 -*-

import unittest
import StringIO

from cwr_webclient.service.cwr_service import WSCWRService

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestWSCWRServiceNoService(unittest.TestCase):
    def setUp(self):
        self._service = WSCWRService('http://127.0.0.1:1', 'http://127.0.0.1:1',
                                     'http://127.0.0.1:1',
                                     'http://127.0.0.1:1',
                                     'http://127.0.0.1:1',
                                     'http://127.0.0.1:1',
                                     'http://127.0.0.1:1')

    def test_process(self):
        file = StringIO.StringIO('text1')
        file.filename = 'filename'

        self._service.process(file)

    def test_get_files(self):
        self._service.get_files()

    def test_get_file(self):
        self._service.delete_file('abc')

    def test_delete_file(self):
        self._service.delete_file('abc')
