# -*- encoding: utf-8 -*-

"""
Offers services for CWR files.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class CWRFileData(object):
    def __init__(self, name, date, status):
        self._name = name
        self._date = date
        self._status = status

    @property
    def name(self):
        return self._name

    @property
    def date(self):
        return self._date

    @property
    def status(self):
        return self._status