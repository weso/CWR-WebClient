# -*- coding: utf-8 -*-

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


def assert_flashes(client, expected_message, expected_category='message'):
    with client.session_transaction() as session:
        try:
            category, message = session['_flashes'][0]
        except KeyError:
            raise AssertionError('nothing flashed')
        assert expected_message in message
        assert expected_category == category