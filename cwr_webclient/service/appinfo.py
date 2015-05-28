# -*- encoding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from cwr_webclient.model.info import CompanyInfo, ApplicationInfo

"""
Offers services for acquiring application related information.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


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
        self._application = ApplicationInfo('CWR Frontend', 2015, 'https://github.com/weso/CWR-WebClient', 'GitHub')

    def get_company(self):
        return self._company

    def get_application(self):
        return self._application
