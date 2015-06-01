# -*- encoding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from cwr_webclient.utils.pagination import Paginator

"""
Offers services for pagination.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class PaginationService(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_transactions_paginator(self, page, group):
        raise NotImplementedError(
            'The get_transactions_paginator method must be implemented')

    @abstractmethod
    def get_page_transactions(self, page, group):
        raise NotImplementedError(
            'The get_page_transactions method must be implemented')


class DefaultPaginationService(object):
    def __init__(self, per_page):
        super(DefaultPaginationService, self).__init__()
        self._per_page = per_page

    def get_transactions_paginator(self, page, group):
        total_entries = len(group.transactions)

        return Paginator(page, self._per_page, total_entries)

    def get_page_transactions(self, page, group):
        pos = (page - 1) * self._per_page

        return group.transactions[pos:pos + self._per_page]
