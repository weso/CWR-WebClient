# -*- coding: utf-8 -*-

import unittest

from mock import Mock
from cwr.file import CWRFile, FileTag
from cwr.transmission import Transmission, TransmissionHeader, \
    TransmissionTrailer

from cwr_webclient import create_app
from cwr_webclient.config import TestConfig
from cwr_webclient.model.file import CWRFileData
from cwr_webclient.service.match import MatchingService
from cwr_webclient.service.file import FileService

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestUpload(unittest.TestCase):
    def setUp(self):
        self._app = create_app(TestConfig)

        match_service_mock = Mock(spec=MatchingService)
        file_service_mock = Mock(spec=FileService)

        file_content_mock = Mock(spec=CWRFileData)

        cwr_tag = FileTag(0, 0, '', '', '')
        transmission = Transmission(TransmissionHeader(), TransmissionTrailer(),
                                    [])
        cwr_file = CWRFile(cwr_tag, transmission)

        file_content_mock.contents = cwr_file

        file_service_mock.get_file = Mock(return_value=file_content_mock)

        self._app.config['MATCH_SERVICE'] = match_service_mock
        self._app.config['FILE_SERVICE'] = file_service_mock

        self._app.config['DEBUG'] = False
        self._app.config['TESTING'] = True

        self._client = self._app.test_client()

    def test_send_valid(self):
        config = {}

        config['blocking_function'] = 0
        config['result_query'] = 0
        config['findsong.threshold'] = 0
        config['relevances.artist'] = 0
        config['song.threshold'] = 0
        config['artist.threshold'] = 0

        with self._app.app_context():
            self._client.post('/cwr/match/send/1', data=config)
