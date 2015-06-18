# -*- encoding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from cwr_webclient.report.mera import generate_match_report_excel

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
    def generate_report_excel(self, data):
        raise NotImplementedError(
            'The generate_report_excel method must be implemented')


class MeraReportService(ReportService):
    def __init__(self, match_service):
        super(MeraReportService, self).__init__()
        self._match_service = match_service

    def generate_report_excel(self, data):
        return generate_match_report_excel(data)
