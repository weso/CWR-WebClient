# -*- encoding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from webapp.config import view_conf
from webapp.model.pagination import Paginator


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
        pass

    @abstractmethod
    def get_page_transactions(self, page, group):
        pass


class DefaultPaginationService(object):
    PER_PAGE = view_conf.per_page

    def __init__(self):
        super(DefaultPaginationService, self).__init__()

    def get_transactions_paginator(self, page, group):
        total_entries = len(group.transactions)

        return Paginator(page, self.PER_PAGE, total_entries)

    def get_page_transactions(self, page, group):
        pos = (page - 1) * self.PER_PAGE

        return group.transactions[pos:pos + self.PER_PAGE]