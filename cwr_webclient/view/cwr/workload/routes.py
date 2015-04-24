# -*- encoding: utf-8 -*-
from flask import render_template, Blueprint

from cwr_webclient.service.workload import LocalCWRWorkloadService


__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

cwr_workload_blueprint = Blueprint('cwr_workload', __name__,
                                   template_folder='templates')

workload_service = LocalCWRWorkloadService()

"""
CWR waiting lists routes.
"""


@cwr_workload_blueprint.route('/', methods=['GET'])
def workload():
    workload_list = workload_service.get_workload_list()

    return render_template('cwr_workload.html', workload=workload_list)