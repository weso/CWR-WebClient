# -*- coding: utf-8 -*-

import unittest

from cwr_webclient import create_app
from cwr_webclient.config import TestConfig
from tests.utils.web import assert_flashes
from cwr_webclient.service.match import WSMatchingService, MatchingStatusChecker


__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestMatchServiceInvalidURL(unittest.TestCase):
    def setUp(self):
        self._service = WSMatchingService('','')

    def test_post_no_file(self):
        data = self._service.get_match_result(0)

        self.assertEqual(None,data)

class TestMatchServiceConnectionDenied(unittest.TestCase):
    def setUp(self):
        self._service = WSMatchingService('http://127.0.0.1/abcde','http://127.0.0.1/abcde')

    def test_post_no_file(self):
        data = self._service.get_match_result(0)

        self.assertEqual(None,data)