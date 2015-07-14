# -*- encoding: utf-8 -*-

import StringIO

import xlsxwriter

"""
Web app module.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


def generate_match_report_excel(matches, filename):
    output = StringIO.StringIO()
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})

    generate_match_report_excel_summary(workbook, filename)
    generate_match_report_excel_queries_list(workbook, matches)
    generate_match_report_excel_queries_results_all(workbook, matches)
    generate_match_report_excel_queries_results_matched(workbook, matches)
    generate_match_report_excel_queries_results_not_matched(workbook, matches)

    workbook.close()

    output.seek(0)
    return output.read()


def generate_match_report_excel_queries_results_all(workbook, matches):
    results_sheet = workbook.add_worksheet('All queries results')

    bold = workbook.add_format({'bold': 1})

    row = 1
    col = 0

    for match in (matches):
        results_sheet.write(row, col, 'Query', bold)
        results_sheet.write(row, col + 1, match['query'])
        row += 1
        results_sheet.write(row, col, 'ISWC', bold)
        results_sheet.write(row, col + 1, match['iswc'])
        row += 1
        results_sheet.write(row, col, 'Type', bold)
        results_sheet.write(row, col + 1, match['type_of_query'])
        row += 1

        results = match['results']
        if len(results) > 0:
            results_sheet.write(row, col, 'Results', bold)
            row += 1
            for result in results:
                results_sheet.write(row, col + 1, 'Entity', bold)
                results_sheet.write(row, col + 2, result['entity'])
                row += 1
                results_sheet.write(row, col + 1, 'ISRC', bold)
                results_sheet.write(row, col + 2, result['isrc'])
                row += 1
                results_sheet.write(row, col + 1, 'USO Transaction ID', bold)
                results_sheet.write(row, col + 2, result['usos_transaction_id'])
                row += 1
                results_sheet.write(row, col + 1, 'Refined score', bold)
                results_sheet.write(row, col + 2, result['refined_score'])
                row += 1
                results_sheet.write(row, col + 1, 'Raw score', bold)
                results_sheet.write(row, col + 2, result['raw_score'])
                row += 1
                results_sheet.write(row, col + 1, 'Matched forms:', bold)
                for key, value in result['matched_forms'].iteritems():
                    row += 1
                    results_sheet.write(row, col + 2, 'Form', bold)
                    results_sheet.write(row, col + 3, key)
                    row += 1
                    results_sheet.write(row, col + 2, 'Rating', bold)
                    results_sheet.write(row, col + 3, value)
                row += 1
                results_sheet.write(row, col + 1, 'Refinements:', bold)
                for refinement in (result['refinements']):
                    row += 1
                    results_sheet.write(row, col + 2, 'Content', bold)
                    results_sheet.write(row, col + 3, refinement['content'])
                    row += 1
                    results_sheet.write(row, col + 2, 'Type', bold)
                    results_sheet.write(row, col + 3, refinement['type'])
                    row += 1
                    results_sheet.write(row, col + 2, 'Relevance', bold)
                    results_sheet.write(row, col + 3, refinement['relevance'])
                    row += 1
                    results_sheet.write(row, col + 2, 'Matched forms', bold)
                    for form in (result['matched_forms']):
                        row += 1
                        results_sheet.write(row, col + 2, form)
                row += 1

        row += 1


def generate_match_report_excel_queries_results_matched(workbook, matches):
    results_sheet = workbook.add_worksheet('Queries results (matched)')

    bold = workbook.add_format({'bold': 1})

    row = 1
    col = 0

    for match in (matches):

        results = match['results']
        if len(results) > 0:

            results_sheet.write(row, col, 'Query', bold)
            results_sheet.write(row, col + 1, match['query'])
            row += 1
            results_sheet.write(row, col, 'ISWC', bold)
            results_sheet.write(row, col + 1, match['iswc'])
            row += 1
            results_sheet.write(row, col, 'Type', bold)
            results_sheet.write(row, col + 1, match['type_of_query'])
            row += 1

            results_sheet.write(row, col, 'Results', bold)
            row += 1
            for result in results:
                results_sheet.write(row, col + 1, 'Entity', bold)
                results_sheet.write(row, col + 2, result['entity'])
                row += 1
                results_sheet.write(row, col + 1, 'ISRC', bold)
                results_sheet.write(row, col + 2, result['isrc'])
                row += 1
                results_sheet.write(row, col + 1, 'USO Transaction ID', bold)
                results_sheet.write(row, col + 2, result['usos_transaction_id'])
                row += 1
                results_sheet.write(row, col + 1, 'Refined score', bold)
                results_sheet.write(row, col + 2, result['refined_score'])
                row += 1
                results_sheet.write(row, col + 1, 'Raw score', bold)
                results_sheet.write(row, col + 2, result['raw_score'])
                row += 1
                results_sheet.write(row, col + 1, 'Matched forms:', bold)
                for key, value in result['matched_forms'].iteritems():
                    row += 1
                    results_sheet.write(row, col + 2, 'Form', bold)
                    results_sheet.write(row, col + 3, key)
                    row += 1
                    results_sheet.write(row, col + 2, 'Rating', bold)
                    results_sheet.write(row, col + 3, value)
                row += 1
                results_sheet.write(row, col + 1, 'Refinements:', bold)
                for refinement in (result['refinements']):
                    row += 1
                    results_sheet.write(row, col + 2, 'Content', bold)
                    results_sheet.write(row, col + 3, refinement['content'])
                    row += 1
                    results_sheet.write(row, col + 2, 'Type', bold)
                    results_sheet.write(row, col + 3, refinement['type'])
                    row += 1
                    results_sheet.write(row, col + 2, 'Relevance', bold)
                    results_sheet.write(row, col + 3, refinement['relevance'])
                    row += 1
                    results_sheet.write(row, col + 2, 'Matched forms', bold)
                    for form in (result['matched_forms']):
                        row += 1
                        results_sheet.write(row, col + 2, form)
                row += 1

            row += 1


def generate_match_report_excel_queries_results_not_matched(workbook, matches):
    results_sheet = workbook.add_worksheet('Queries results (not matched)')

    bold = workbook.add_format({'bold': 1})

    row = 1
    col = 0

    for match in (matches):

        results = match['results']
        if len(results) == 0:
            results_sheet.write(row, col, 'Query', bold)
            results_sheet.write(row, col + 1, match['query'])
            row += 1
            results_sheet.write(row, col, 'ISWC', bold)
            results_sheet.write(row, col + 1, match['iswc'])
            row += 1
            results_sheet.write(row, col, 'Type', bold)
            results_sheet.write(row, col + 1, match['type_of_query'])
            row += 1

            row += 1


def generate_match_report_excel_queries_list(workbook, matches):
    queries_sheet = workbook.add_worksheet('Queries list')

    bold = workbook.add_format({'bold': 1})

    queries_sheet.write('A1', 'Query', bold)
    queries_sheet.write('B1', 'ISWC', bold)
    queries_sheet.write('C1', 'Type of Query', bold)

    row = 1
    col = 0

    for match in (matches):
        queries_sheet.write(row, col, match['query'])
        queries_sheet.write(row, col + 1, match['iswc'])
        queries_sheet.write(row, col + 2, match['type_of_query'])
        row += 1

    queries_sheet.write(row, 0, 'Count', bold)
    queries_sheet.write(row, 1, '=ROWS(B2:B%s)' % row)


def generate_match_report_excel_summary(workbook, filename):
    queries_sheet = workbook.add_worksheet('Summary')

    bold = workbook.add_format({'bold': 1})

    queries_sheet.write('A1', 'Filename', bold)
    queries_sheet.write('B1', filename)
