# -*- encoding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import os
import datetime
import logging

from werkzeug.utils import secure_filename
from cwr.parser.decoder.file import default_file_decoder

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


class FileProcessor(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def process(self, data, file_id):
        raise NotImplementedError('The process method must be implemented')


class StatusChecker(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_status(self, file_id):
        raise NotImplementedError('The get_status method must be implemented')


class LocalFileService(FileService):
    def __init__(self, path, checker):
        super(FileService, self).__init__()
        self._files_data = {}
        self._path = path
        self._decoder = default_file_decoder()
        self._checker = checker

        self._logger = logging.getLogger(__name__)

    def _read_cwr(self, file_data):
        data = {}
        data['filename'] = os.path.basename(file_data.filename)

        self._logger.info("Reading CWR file %s" % (data['filename']))

        data['contents'] = file_data.read()

        return self._decoder.decode(data)

    def get_file(self, file_id):
        self._logger.info("Acquiring file with id %s" % file_id)

        if file_id in self._files_data:
            data = self._files_data[file_id]
        else:
            data = None

        return data

    def get_files(self):
        self._logger.info("Acquiring all files")

        files = []

        for value in self._files_data.itervalues():
            value.status = self._checker.get_status(value.file_id)
            files.append(value)

        return files

    def save_file(self, file, path):

        filename = secure_filename(file.filename)
        file_path = '%s/%s' % (path, filename)

        # file.save(file_path)

        data = self._read_cwr(file)
        index = len(self._files_data)

        self._files_data[index] = CWRFileData(index, filename, data, datetime.datetime.now(), WorkloadStatus.processing)

        return index
