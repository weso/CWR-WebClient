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
        raise NotImplementedError('The process method must be implemented')

    @abstractmethod
    def get_files(self):
        raise NotImplementedError('The get_files method must be implemented')

    @abstractmethod
    def get_file(self, file_id):
        raise NotImplementedError('The get_file method must be implemented')


class WSCWRService(CWRService):
    def __init__(self, url, url_files, url_file_delete, url_match_begin,
                 url_match_reject, url_match_confirm, url_match_feedback):
        super(WSCWRService, self).__init__()
        self._url = url
        self._url_files = url_files
        self._url_file_delete = url_file_delete
        self._url_match_begin = url_match_begin
        self._url_match_reject = url_match_reject
        self._url_match_confirm = url_match_confirm
        self._url_match_feedback = url_match_feedback

    def process(self, file_data):
        data = {}
        data['filename'] = str(file_data.filename)

        data['contents'] = str(file_data.read()).decode('latin-1')

        _logger.info('Processing file %s' % file_data.filename)

        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json'}

        data = json.dumps(data)

        try:
            _logger.info('Sending uploaded file')
            requests.post(self._url, data=data, headers=headers)
            _logger.info('Sent uploaded file')
        except (ConnectionError, ValueError):
            _logger.info('Error sending file')

    def begin_match(self, file_id, config):
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json'}

        data = {}
        data['file_id'] = file_id
        data['config'] = config

        data = json.dumps(data)

        try:
            requests.post(self._url_match_begin, data=data, headers=headers)
        except (ConnectionError, ValueError):
            _logger.info('Error asking for match')

    def send_feedback(self, file_id):
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json'}

        data = {}
        data['file_id'] = file_id

        data = json.dumps(data)

        try:
            requests.post(self._url_match_feedback, data=data, headers=headers)
        except (ConnectionError, ValueError):
            _logger.info('Error sending feedback')

    def reject_match(self, file_id, pos):
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json'}

        data = {}
        data['file_id'] = file_id
        data['pos'] = pos

        data = json.dumps(data)

        try:
            requests.post(self._url_match_reject, data=data, headers=headers)
        except (ConnectionError, ValueError):
            _logger.info('Error rejecting match')

    def confirm_match(self, file_id, pos):
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json'}

        data = {}
        data['file_id'] = file_id
        data['pos'] = pos

        data = json.dumps(data)

        try:
            requests.post(self._url_match_confirm, data=data, headers=headers)
        except (ConnectionError, ValueError):
            _logger.info('Error confirming match')

    def get_files(self):
        try:
            files = requests.get(self._url_files).json()
        except (ConnectionError, ValueError):
            files = []

        return files

    def delete_file(self, file_id):
        _logger.info('Deleting file with id %s' % file_id)
        data = {}
        data['file_id'] = file_id

        headers = {'Content-Type': 'application/json'}

        try:
            requests.post(self._url_file_delete, data=json.dumps(data),
                          headers=headers).json()
        except (ConnectionError, ValueError):
            pass

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
