# -*- encoding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import json
import logging

import requests

from cwr_webclient.service.file import FileProcessor, StatusChecker
from cwr_webclient.model.workload import WorkloadStatus


"""
Offers services for CWR files.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class MatchingService(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def match(self, cwr_json, file_id):
        raise NotImplementedError('The match method must be implemented')

    @abstractmethod
    def get_match_result(self, file_id):
        raise NotImplementedError('The get_match_result method must be implemented')


class TestMatchingService(object):
    def __init__(self):
        super(TestMatchingService, self).__init__()

        json_data = '[ { "query" : "Shakira I. Mebarack", "type_of_query" : "artist", "refinements" : [ { "type": "song", "content" : "Waka Waka" }, { "type" : "song", "content" : "La Tortura" } ], "results" : [ { "entity" : "http://example.org/Shakira", "raw_score" : 0.95, "matched_forms" : { "Shakira Isabel Mebarack" : 0.75, "Shakira Mebarack" : 0.95 }, "refined_score" : 2.95, "refinements": [ { "type" : "song", "score" : 1, "relevance" : 1, "content" : "Waka Waka", "matched_forms" : { "Waka_Waka" : 1, "Waka Waka feat" : 0.85 } }, { "type" : "song", "score" : 1, "relevance" : 1, "content" : "La Tortura", "matched_forms" : { "La Tortura" : 1 } } ] }, { "entity" : "http://example.org/Schakira", "raw_score" : 0.4, "matched_forms" : { "Schakira" : 0.4 }, "refined_score" : 0.4, "refinements": [] } ] } ]'

        self._json = json.loads(json_data)

    def match(self, cwr_json, file_id):
        pass

    def get_match_result(self, file_id):
        return self._json


class WSMatchingService(object):
    def __init__(self, url):
        super(WSMatchingService, self).__init__()
        self._url = url

        self._logger = logging.getLogger(__name__)

    def match(self, cwr_json, file_id):
        self._logger.info("Matching file with id %s" % file_id)

        headers = {'Content-Type': 'application/json', 'Accept': 'text/plain'}

        self._logger.info("Posting file's data to %s" % self._url)
        cwr_json = json.loads(cwr_json)
        cwr_json['file_id'] = file_id
        cwr_json = json.dumps(cwr_json)
        requests.post(self._url, data=cwr_json, headers=headers, verify=False)

    def get_match_result(self, file_id):
        return None


class MatchingFileProcessor(FileProcessor):
    def __init__(self, service):
        super(MatchingFileProcessor, self).__init__()
        self._service = service

    def process(self, data, file_id):
        self._service.match(data, file_id)


class MatchingStatusChecker(StatusChecker):
    def __init__(self, service, url):
        super(MatchingStatusChecker, self).__init__()
        self._service = service
        self._url = url

    def get_status(self, file_id):
        headers = {'Content-Type': 'application/json', 'Accept': 'text/plain'}

        data = {}
        data['file_id'] = file_id
        data = json.dumps(data)

        response = requests.post(self._url, data=data, headers=headers)

        status = response.json()['status']
        if status == 'error':
            status = WorkloadStatus.error
        elif status == 'waiting':
            status = WorkloadStatus.waiting
        elif status == 'processing':
            status = WorkloadStatus.processing
        elif status == 'done':
            status = WorkloadStatus.done
        elif status == 'rejected':
            status = WorkloadStatus.rejected

        return status
