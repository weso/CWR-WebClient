# -*- encoding: utf-8 -*-

from abc import ABCMeta, abstractmethod


"""
Offers services for acquiring application related information.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class CompanyInfo(object):
    def __init__(self, name, url):
        self._name = name
        self._url = url

    @property
    def name(self):
        return self._name

    @property
    def url(self):
        return self._url


class ApplicationInfoService(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_company(self):
        raise NotImplementedError('The get_company method must be implemented')


class WESOApplicationInfoService(ApplicationInfoService):
    def __init__(self):
        super(WESOApplicationInfoService, self).__init__()
        # TODO: Change this, the data should be read from somewhere
        self._company = CompanyInfo('WESO', 'http://www.weso.es')


    def get_company(self):
        return self._company