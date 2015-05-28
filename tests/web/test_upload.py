# -*- coding: utf-8 -*-

import unittest

from cwr_webclient import create_app
from cwr_webclient.config import TestConfig
from tests.utils.web import assert_flashes


__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestUpload(unittest.TestCase):
    def setUp(self):
        self._app = create_app(TestConfig)

        self._app.config['DEBUG'] = False
        self._app.config['TESTING'] = True

        self._client = self._app.test_client()

    def test_post_no_file(self):
        with self._app.app_context():
            self._client.post('/cwr/upload/')
            assert_flashes(self._client, 'No file selected')

    def test_post_file_none(self):
        with self._app.app_context():
            self._client.post('/cwr/upload/', data=dict(file=None))
            assert_flashes(self._client, 'No file selected')