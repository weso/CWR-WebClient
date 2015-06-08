# -*- encoding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import json

import requests

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


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


class WSCWRService(CWRService):
    def __init__(self, url, url_files):
        super(WSCWRService, self).__init__()
        self._url = url
        self._url_files = url_files

    def process(self, file_data):
        data = {}
        data['filename'] = str(file_data.filename)

        data['contents'] = str(file_data.read())

        headers = {'Content-Type': 'application/json'}

        requests.post(self._url, data=json.dumps(data), headers=headers)

        return 0

    def get_files(self):
        files = requests.get(self._url_files).json()

        return files
