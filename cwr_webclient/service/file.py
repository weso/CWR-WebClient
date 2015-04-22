# -*- encoding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import os

from werkzeug.utils import secure_filename


__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class FileService(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def save_file(self, file, path):
        raise NotImplementedError('The save_file method must be implemented')


class LocalFileService(FileService):
    def __init__(self):
        super(FileService, self).__init__()

    def save_file(self, file, path):
        filename = secure_filename(file.filename)
        file.save(os.path.join(path, filename))

        return file.filename