# -*- encoding: utf-8 -*-

from abc import ABCMeta, abstractmethod


"""
Offers services for CWR files.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class CWRDatabaseService(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_files_list(self):
        raise NotImplementedError('The get_data method must be implemented')


class LocalCWRDatabaseService(CWRDatabaseService):
    def __init__(self):
        super(LocalCWRDatabaseService, self).__init__()

    def get_files_list(self):
        files = []

        files.append({'name': 'file1'})
        files.append({'name': 'file2'})

        return files