# -*- encoding: utf-8 -*-
from flask import render_template, redirect, url_for, abort, request, session
import flask as f

from webapp.view import app
from webapp.config import app_conf, view_conf
from webapp.model.pagination import Paginator
from webapp.utils.file_manager import FileManager


__author__ = 'Bernardo'

PER_PAGE = view_conf.per_page

fileManager = FileManager

"""
Basic routes.
"""


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', app_title=app_conf.title)


"""
Upload routes.
"""


@app.route('/cwr/upload', methods=['GET'])
def upload_cwr():
    return render_template('cwr/upload.html')


@app.route('/upload/cwr', methods=['POST'])
def upload_cwr_handler():
    # Get the name of the uploaded file
    sent_file = request.files['file']

    if sent_file:
        fileManager.save_file_cwr(sent_file)
        session['cwr_file_name'] = sent_file.filename
        ctx = app.app_context()
        f.cwr = fileManager.read_cwr(sent_file.filename)

        return redirect(url_for('cwr_validation_report'))
    else:
        return redirect(url_for('upload_cwr'))


@app.route('/uso/upload', methods=['GET'])
def upload_uso():
    return render_template('uso/upload.html')


"""
CWR matching routes.
"""


@app.route('/cwr/match', methods=['GET'])
def cwr_match():
    uso = (
        {'id': 'USO_1', 'name': 'USO_1', 'matched': True},
        {'id': 'USO_2', 'name': 'USO_2', 'matched': False},
        {'id': 'USO_3', 'name': 'USO_3', 'matched': True},
        {'id': 'USO_4', 'name': 'USO_4', 'matched': True},
    )
    cwr = (
        {'id': 'CWR_1', 'name': 'CWR_1', 'matched': True},
        {'id': 'CWR_2', 'name': 'CWR_2', 'matched': False},
        {'id': 'CWR_3', 'name': 'CWR_3', 'matched': True},
        {'id': 'CWR_4', 'name': 'CWR_4', 'matched': True},
    )

    sources = {'uso': uso, 'cwr': cwr}
    return render_template('cwr/match.html', sources=sources)


@app.route('/cwr/match/report', methods=['GET'])
def cwr_match_report():
    result = {}

    pairs = (
        {'cwr': 'The Beatles', 'match': 'The Beatels', 'source': 'Music Database'},
        {'cwr': 'The Beatles', 'match': 'Los Bitels', 'source': 'Music Database'},
        {'cwr': 'The Beatles', 'match': 'The Beatel', 'source': 'Music Database'},
        {'cwr': 'The Beatles', 'match': 'Beatles Lennon', 'source': 'Music Database'},
        {'cwr': 'Shakira', 'match': 'Shikira', 'source': 'Music Database'},
        {'cwr': 'Shakira', 'match': 'Shaquira', 'source': 'Music Database'},
    )

    result['pairs'] = pairs

    return render_template('cwr/match_result.html', result=result)


@app.route('/cwr/match/report/download', methods=['GET'])
def cwr_match_report_download():
    return redirect(url_for('match_report'))


@app.route('/cwr/match/edit', methods=['GET'])
def cwr_match_edit():
    result = {}

    pairs = (
        {'cwr': 'The Beatles', 'match': 'The Beatels', 'source': 'Music Database'},
        {'cwr': 'The Beatles', 'match': 'Los Bitels', 'source': 'Music Database'},
        {'cwr': 'The Beatles', 'match': 'The Beatel', 'source': 'Music Database'},
        {'cwr': 'The Beatles', 'match': 'Beatles Lennon', 'source': 'Music Database'},
        {'cwr': 'Shakira', 'match': 'Shikira', 'source': 'Music Database'},
        {'cwr': 'Shakira', 'match': 'Shaquira', 'source': 'Music Database'},
    )

    result['pairs'] = pairs

    options = (
        {'value': 'The Beatels', 'name': 'The Beatels'},
        {'value': 'Los Bitels', 'name': 'Los Bitels'},
        {'value': 'The Beatel', 'name': 'The Beatel'},
        {'value': 'Beatles Lennon', 'name': 'Beatles Lennon'},
        {'value': 'Shikira', 'name': 'Shikira'},
        {'value': 'Shaquira', 'name': 'Shaquira'},
    )

    return render_template('cwr/match_edit.html', result=result, options=options)


"""
CWR validation routes.
"""


@app.route('/cwr/validation/report', methods=['GET'])
def cwr_validation_report():
    cwr = f.cwr

    return render_template('cwr/validation/summary.html', cwr=cwr, current_tab='summary_item')


@app.route('/cwr/validation/report/agreements', defaults={'page': 1}, methods=['GET'])
@app.route('/cwr/validation/report/agreements/page/<int:page>', methods=['GET'])
def cwr_validation_report_agreements(page):
    cwr = f.cwr

    if not cwr and page != 1:
        abort(404)

    group = cwr.transmission.groups[0]

    pos = (page - 1) * PER_PAGE
    transactions = group.transactions[pos:pos + PER_PAGE]

    total_entries = len(group.transactions)

    pagination = Paginator(page, PER_PAGE, total_entries)

    return render_template('cwr/validation/agreements.html', paginator=pagination, group=group,
                           transactions=transactions, current_tab='agreements_item')


@app.route('/cwr/validation/report/new_regs', defaults={'page': 1}, methods=['GET'])
@app.route('/cwr/validation/report/new_regs/page/<int:page>', methods=['GET'])
def cwr_validation_report_new_registrations(page):
    total_entries = 50

    new_works = []

    artists = []

    artists.append({'first_name': 'John', 'last_name': 'Doe'})

    publishers = []

    publishers.append({'name': 'The Publisher', 'controlled': False, 'role': 'Original Publisher', 'ownership': 0.2})
    publishers.append({'name': 'Another Publisher', 'controlled': True, 'role': 'Acquirer', 'ownership': 0.3})
    publishers.append({'name': 'Third Publisher', 'controlled': False, 'role': 'Subpublisher', 'ownership': 0.5})

    writers = []

    writers.append({'first_name': 'John', 'last_name': 'Doe', 'controlled': False})
    writers.append({'first_name': 'John', 'last_name': 'Smith', 'controlled': True})

    new_works.append(
        {'id': '146', 'title': 'The Musical Work', 'language': 'EN', 'publishers': publishers, 'writers': writers,
         'artists': artists})
    new_works.append(
        {'id': '146', 'title': 'The Musical Work', 'language': 'EN', 'publishers': publishers, 'writers': writers,
         'artists': artists})
    new_works.append(
        {'id': '146', 'title': 'The Musical Work', 'language': 'EN', 'publishers': publishers, 'writers': writers,
         'artists': artists})
    new_works.append(
        {'id': '146', 'title': 'The Musical Work', 'language': 'EN', 'publishers': publishers, 'writers': writers,
         'artists': artists})
    new_works.append(
        {'id': '146', 'title': 'The Musical Work', 'language': 'EN', 'publishers': publishers, 'writers': writers,
         'artists': artists})
    new_works.append(
        {'id': '146', 'title': 'The Musical Work', 'language': 'EN', 'publishers': publishers, 'writers': writers,
         'artists': artists})
    new_works.append(
        {'id': '146', 'title': 'The Musical Work', 'language': 'EN', 'publishers': publishers, 'writers': writers,
         'artists': artists})
    new_works.append(
        {'id': '146', 'title': 'The Musical Work', 'language': 'EN', 'publishers': publishers, 'writers': writers,
         'artists': artists})
    new_works.append(
        {'id': '146', 'title': 'The Musical Work', 'language': 'EN', 'publishers': publishers, 'writers': writers,
         'artists': artists})
    new_works.append(
        {'id': '146', 'title': 'The Musical Work', 'language': 'EN', 'publishers': publishers, 'writers': writers,
         'artists': artists})
    new_works.append(
        {'id': '146', 'title': 'The Musical Work', 'language': 'EN', 'publishers': publishers, 'writers': writers,
         'artists': artists})

    if not new_works and page != 1:
        abort(404)

    pagination = Paginator(page, PER_PAGE, total_entries)

    return render_template('cwr/validation/works.html', works=new_works, total_entries=total_entries,
                           paginator=pagination, current_tab='new_reg_item')


@app.route('/cwr/validation/report/revisions', defaults={'page': 1}, methods=['GET'])
@app.route('/cwr/validation/report/revisions/page/<int:page>', methods=['GET'])
def cwr_validation_report_revisions(page):
    total_entries = 0

    revisions = []

    if not revisions and page != 1:
        abort(404)

    pagination = Paginator(page, PER_PAGE, total_entries)

    return render_template('cwr/validation/works.html', works=revisions, total_entries=total_entries,
                           paginator=pagination, current_tab='revisions_item')


@app.route('/cwr/validation/report/download', methods=['GET'])
def cwr_validation_report_download():
    return redirect(url_for('validation_report'))


"""
CWR acknowledgement routes.
"""


@app.route('/cwr/acknowledgement', methods=['GET'])
def cwr_acknowledgement_generation():
    return render_template('cwr/acknowledgement.html')