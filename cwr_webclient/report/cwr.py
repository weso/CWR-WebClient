# -*- encoding: utf-8 -*-

import StringIO

import xlsxwriter

"""
Web app module.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


def generate_cwr_report_excel(cwr):
    output = StringIO.StringIO()
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})

    _generate_cwr_report_excel_general(workbook, cwr)

    for group in cwr.transmission.groups:
        _generate_cwr_report_excel_group(workbook, group)

    workbook.close()

    output.seek(0)
    return output.read()


def _generate_cwr_report_excel_group(workbook, group):
    results_sheet = workbook.add_worksheet(group.group_header.transaction_type)

    bold = workbook.add_format({'bold': 1})

    row = 1
    col = 0

    for transaction in group.transactions:
        for record in transaction:
            results_sheet.write(row, col + 1, record.record_type)
            row += 1


def _generate_cwr_report_excel_general(workbook, cwr):
    results_sheet = workbook.add_worksheet('General info')

    bold = workbook.add_format({'bold': 1})

    header = cwr.transmission.header
    trailer = cwr.transmission.trailer

    row = 1
    col = 0

    results_sheet.write(row, col, 'Sender ID', bold)
    results_sheet.write(row, col + 1, header.sender_id)

    row += 1

    results_sheet.write(row, col, 'Sender Name', bold)
    results_sheet.write(row, col + 1, header.sender_name)

    row += 1

    results_sheet.write(row, col, 'Sender Type', bold)
    results_sheet.write(row, col + 1, header.sender_name)

    row += 1
    row += 1

    results_sheet.write(row, col, 'Creation Date', bold)
    results_sheet.write(row, col + 1, header.creation_date_time)

    row += 1

    results_sheet.write(row, col, 'Transmission Date', bold)
    results_sheet.write(row, col + 1, header.transmission_date)

    row += 1
    row += 1

    results_sheet.write(row, col, 'EDI Standard', bold)
    results_sheet.write(row, col + 1, header.edi_standard)

    row += 1

    results_sheet.write(row, col, 'Character Set', bold)
    results_sheet.write(row, col + 1, header.character_set)

    row += 1
    row += 1

    results_sheet.write(row, col, 'Counts', bold)

    row += 1

    results_sheet.write(row, col, 'Groups', bold)
    results_sheet.write(row, col + 1, trailer.group_count)

    row += 1

    results_sheet.write(row, col, 'Transactions', bold)
    results_sheet.write(row, col + 1, trailer.transaction_count)

    row += 1

    results_sheet.write(row, col, 'Records', bold)
    results_sheet.write(row, col + 1, trailer.record_count)
