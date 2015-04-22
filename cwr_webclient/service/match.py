# -*- encoding: utf-8 -*-

from abc import ABCMeta, abstractmethod

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
    def get_sources(self):
        raise NotImplementedError('The get_sources method must be implemented')

    @abstractmethod
    def get_match_pairs(self):
        raise NotImplementedError('The get_match_pairs method must be implemented')

    @abstractmethod
    def get_match_options(self):
        raise NotImplementedError('The get_match_options method must be implemented')


class LocalMatchingService(object):
    def __init__(self):
        super(LocalMatchingService, self).__init__()

    def get_sources(self):
        uso = (
            {'id': 'USO_1', 'name': 'USO_1', 'matched': True},
            {'id': 'USO_2', 'name': 'USO_2', 'matched': False},
            {'id': 'USO_3', 'name': 'USO_3', 'matched': True},
            {'id': 'USO_4', 'name': 'USO_4', 'matched': True},
        )
        cwr = (
            {'id': 'CWR_1', 'name': 'CWR_1', 'matched': True},
            {'id': 'CWR_2', 'name': 'CWR_2', 'matched': False},
            {'id': 'CWR_3', 'name': 'CWR_3', 'matched': True},
            {'id': 'CWR_4', 'name': 'CWR_4', 'matched': True},
        )

        sources = {'uso': uso, 'cwr': cwr}

        return sources

    def get_match_pairs(self):
        pairs = (
            {'cwr': 'The Beatles', 'match': 'The Beatels', 'source': 'Music Database'},
            {'cwr': 'The Beatles', 'match': 'Los Bitels', 'source': 'Music Database'},
            {'cwr': 'The Beatles', 'match': 'The Beatel', 'source': 'Music Database'},
            {'cwr': 'The Beatles', 'match': 'Beatles Lennon', 'source': 'Music Database'},
            {'cwr': 'Shakira', 'match': 'Shikira', 'source': 'Music Database'},
            {'cwr': 'Shakira', 'match': 'Shaquira', 'source': 'Music Database'},
        )

        return pairs

    def get_match_options(self):
        options = (
            {'value': 'The Beatels', 'name': 'The Beatels'},
            {'value': 'Los Bitels', 'name': 'Los Bitels'},
            {'value': 'The Beatel', 'name': 'The Beatel'},
            {'value': 'Beatles Lennon', 'name': 'Beatles Lennon'},
            {'value': 'Shikira', 'name': 'Shikira'},
            {'value': 'Shaquira', 'name': 'Shaquira'},
        )

        return options