# -*- encoding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from cwr_webclient.report import mera as mera_reporter
from cwr_webclient.report import cwr as cwr_reporter

"""
Offers services for pagination.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class ReportService(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def generate_report_excel(self, data, filename):
        raise NotImplementedError(
            'The generate_report_excel method must be implemented')


class MeraReportService(ReportService):
    def generate_report_excel(self, data, filename):
        return mera_reporter.generate_match_report_excel(data, filename)


class CWRReportService(ReportService):
    def generate_report_excel(self, data, filename):
        return cwr_reporter.generate_cwr_report_excel(data)
