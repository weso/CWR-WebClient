# -*- encoding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import os
import datetime

from werkzeug.utils import secure_filename
from cwr.parser.file import CWRFileDecoder

from cwr_webclient.model.file import CWRFileData
from cwr_webclient.model.workload import WorkloadStatus


__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class FileService(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_files(self):
        raise NotImplementedError('The get_files method must be implemented')

    @abstractmethod
    def get_file(self, id):
        raise NotImplementedError('The get_data method must be implemented')

    @abstractmethod
    def save_file(self, file, path):
        raise NotImplementedError('The save_file method must be implemented')


class LocalFileService(FileService):
    def __init__(self, path):
        super(FileService, self).__init__()
        self._files = [CWRFileData('File1', datetime.datetime.now(), WorkloadStatus.done),
                       CWRFileData('File2', datetime.datetime.now(), WorkloadStatus.done),
                       CWRFileData('File3', datetime.datetime.now(), WorkloadStatus.processing)]
        self._files_data = {}
        self._path = path
        self._decoder = CWRFileDecoder()

    def get_file(self, id):
        if id in self._files_data:
            data = self._files_data[id]
        else:
            data = self._read_cwr(id, self._path)
            self._files_data[id] = data

        return data

    def get_files(self):
        return self._files

    def save_file(self, file, path):
        filename = secure_filename(file.filename)
        file.save(os.path.join(path, filename))

        return file.filename

    def _read_cwr(self, filename, path):
        file_path = os.path.join(path, filename)
        return self._decoder.decode(file_path)