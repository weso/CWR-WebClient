# -*- encoding: utf-8 -*-

"""
Offers services for CWR files.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class CWRFileData(object):
    def __init__(self, file_id, name, contents, date, status):
        self._file_id = file_id
        self._name = name
        self._contents = contents
        self._date = date
        self._status = status

    @property
    def contents(self):
        return self._contents

    @property
    def date(self):
        return self._date

    @property
    def file_id(self):
        return self._file_id

    @property
    def name(self):
        return self._name

    @property
    def status(self):
        return self._status