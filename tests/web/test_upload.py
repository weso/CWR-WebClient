# -*- coding: utf-8 -*-

import unittest

from cwr_webclient import create_app


__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestUpload(unittest.TestCase):
    def setUp(self):
        self._app = create_app()

        self._app.config['DEBUG'] = False
        self._app.config['TESTING'] = True

        self._client = self._app.test_client()

    def test_post_no_file(self):
        with self._app.app_context():
            self._client.post('/cwr/upload/', data=dict(file=None))
            self.assert_flashes('No file selected')

    def assert_flashes(self, expected_message, expected_category='message'):
        with self._client.session_transaction() as session:
            try:
                category, message = session['_flashes'][0]
            except KeyError:
                raise AssertionError('nothing flashed')
            assert expected_message in message
            assert expected_category == category