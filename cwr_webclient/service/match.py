# -*- encoding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import json

import requests


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
    def match(self, cwr_json):
        raise NotImplementedError('The get_data method must be implemented')


class TestMatchingService(object):
    def __init__(self):
        super(TestMatchingService, self).__init__()

        json_data = '[ { "query" : "Shakira I. Mebarack", "type_of_query" : "artist", "refinements" : [ { "type": "song", "content" : "Waka Waka" }, { "type" : "song", "content" : "La Tortura" } ], "results" : [ { "entity" : "http://example.org/Shakira", "raw_score" : 0.95, "matched_forms" : { "Shakira Isabel Mebarack" : 0.75, "Shakira Mebarack" : 0.95 }, "refined_score" : 2.95, "refinements": [ { "type" : "song", "score" : 1, "relevance" : 1, "content" : "Waka Waka", "matched_forms" : { "Waka_Waka" : 1, "Waka Waka feat" : 0.85 } }, { "type" : "song", "score" : 1, "relevance" : 1, "content" : "La Tortura", "matched_forms" : { "La Tortura" : 1 } } ] }, { "entity" : "http://example.org/Schakira", "raw_score" : 0.4, "matched_forms" : { "Schakira" : 0.4 }, "refined_score" : 0.4, "refinements": [] } ] } ]'

        self._json = json.loads(json_data)

    def match(self, cwr_json):
        return self._json


class WSMatchingService(object):
    def __init__(self, url):
        super(WSMatchingService, self).__init__()
        self._url = url

    def match(self, cwr_json):
        headers = {'Content-Type': 'application/json'}

        r = requests.post(self._url, data=cwr_json, headers=headers)