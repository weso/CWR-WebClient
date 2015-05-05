# -*- encoding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import os
import datetime
import logging

from werkzeug.utils import secure_filename
from cwr.parser.file import CWRFileDecoder
from cwr.parser.cwrjson import JSONEncoder

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

    @abstractmethod
    def generate_json(self, data):
        raise NotImplementedError('The generate_json method must be implemented')


class FileProcessor(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def process(self, data, file_id):
        raise NotImplementedError('The process method must be implemented')


class LocalFileService(FileService):
    def __init__(self, path, processors=None):
        super(FileService, self).__init__()
        self._files_data = {}
        self._path = path
        self._decoder = CWRFileDecoder()
        self._encoder_json = JSONEncoder()

        if not processors:
            self._processors = []
        else:
            self._processors = processors

        self._logger = logging.getLogger(__name__)

    def _read_cwr(self, filename, path):
        file_path = os.path.join(path, filename)
        return self._decoder.decode(file_path)

    def generate_json(self, data):
        return self._encoder_json.encode(data)

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
            files.append(value)

        return files

    def register_processor(self, processor):
        self._processors.append(processor)

    def save_file(self, file, path):
        self._logger.info("Saving file %s to %s" % (file, path))

        filename = secure_filename(file.filename)
        file.save(os.path.join(path, filename))

        data = self._read_cwr(filename, self._path)
        index = len(self._files_data)

        self._files_data[index] = CWRFileData(index, filename, data, datetime.datetime.now(), WorkloadStatus.done)

        cwr_json = self.generate_json(data);

        for processor in self._processors:
            processor.process(cwr_json, index)

        return index
