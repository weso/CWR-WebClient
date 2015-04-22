# -*- encoding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from cwr_webclient.utils.file_manager import FileManager


"""
Offers services for CWR files.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class CWRFileService(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_data(self, id):
        raise NotImplementedError('The get_data method must be implemented')


class LocalCWRFileService(CWRFileService):
    def __init__(self):
        super(LocalCWRFileService, self).__init__()
        self._fileManager = FileManager
        self._files_data = {}

    def get_data(self, id):
        if id in self._files_data:
            data = self._files_data[id]
        else:
            data = self._fileManager.read_cwr(id)
            self._files_data[id] = data

        return data