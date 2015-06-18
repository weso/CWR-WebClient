# -*- encoding: utf-8 -*-

import StringIO

import xlsxwriter

"""
Web app module.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


def generate_match_report_excel(matches):
    output = StringIO.StringIO()
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0

    for match in (matches):
        print match
        print match['query']
        worksheet.write(row, col, match['query'])
        row += 1

    workbook.close()

    output.seek(0)
    return output.read()
