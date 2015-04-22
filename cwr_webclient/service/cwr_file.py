# -*- encoding: utf-8 -*-

import os
from abc import ABCMeta, abstractmethod

from cwr.parser.file import CWRFileDecoder


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
    def get_data(self, id, path):
        raise NotImplementedError('The get_data method must be implemented')


class LocalCWRFileService(CWRFileService):
    def __init__(self):
        super(LocalCWRFileService, self).__init__()
        self._files_data = {}

    def get_data(self, id, path):
        if id in self._files_data:
            data = self._files_data[id]
        else:
            data = self._read_cwr(id, path)
            self._files_data[id] = data

        return data

    def _read_cwr(self, filename, path):
        decoder = CWRFileDecoder()
        file_path = os.path.join(path, filename)
        return decoder.decode(file_path)