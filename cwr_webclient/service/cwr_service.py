# -*- encoding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import json
import logging

from requests.exceptions import ConnectionError
import requests

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

_logger = logging.getLogger(__name__)


class CWRService(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def process(self, file_data):
        raise NotImplementedError('The validate method must be implemented')

    @abstractmethod
    def get_files(self):
        raise NotImplementedError('The get_files method must be implemented')

    @abstractmethod
    def get_file(self, file_id):
        raise NotImplementedError('The get_file method must be implemented')


class WSCWRService(CWRService):
    def __init__(self, url, url_files):
        super(WSCWRService, self).__init__()
        self._url = url
        self._url_files = url_files

    def process(self, file_data):
        data = {}
        data['filename'] = str(file_data.filename)

        data['contents'] = str(file_data.read()).decode('latin-1')

        _logger.info('Processing file %s' % file_data.filename)

        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json'}

        data = json.dumps(data)

        try:
            requests.post(self._url, data=data, headers=headers)
        except (ConnectionError, ValueError):
            _logger.info('Error sending file')

        return 0

    def get_files(self):
        try:
            files = requests.get(self._url_files).json()
        except (ConnectionError, ValueError):
            files = []

        return files

    def get_file(self, file_id):
        data = {}
        data['id'] = file_id

        headers = {'Content-Type': 'application/json'}

        try:
            file = requests.get(self._url_files, data=json.dumps(data),
                                headers=headers).json()
        except (ConnectionError, ValueError):
            file = None

        return file
