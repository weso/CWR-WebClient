# -*- encoding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from cwr_webclient.model.workload import WorkloadInfo, WorkloadStatus


"""
Offers services for CWR files.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class CWRWorkloadService(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_workload_list(self):
        raise NotImplementedError('The get_workload_list method must be implemented')


class LocalCWRWorkloadService(CWRWorkloadService):
    def __init__(self):
        super(LocalCWRWorkloadService, self).__init__()
        self._workload = []

        self._workload.append(WorkloadInfo('file1', WorkloadStatus.processing))
        self._workload.append(WorkloadInfo('file2', WorkloadStatus.waiting))
        self._workload.append(WorkloadInfo('file3', WorkloadStatus.waiting))
        self._workload.append(WorkloadInfo('file4', WorkloadStatus.done))

    def get_workload_list(self):
        return self._workload