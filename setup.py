# -*- coding: utf-8 -*-
import ast
import re
from codecs import open
from os import path

from setuptools import setup, find_packages

"""
PyPI configuration module.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'

_version_re = re.compile(r'__version__\s+=\s+(.*)')
_tests_require = ['mock']

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open('cwr_webclient/__init__.py', 'rb', encoding='utf-8') as f:
    version = f.read()
    version = _version_re.search(version).group(1)
    version = str(ast.literal_eval(version.rstrip()))

setup(
    name='CWR-WebClient',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'data': ['data_web/*.properties']
    },
    version=version,
    description='Web client for CWR services',
    author='WESO',
    author_email='weso@weso.es',
    license='MIT',
    url='https://github.com/weso/CWR-WebClient',
    download_url='https://github.com/weso/CWR-WebClient',
    keywords=['CWR', 'commonworks', 'web', 'client', 'CISAC'],
    platforms='any',
    classifiers=['Environment :: Web Environment',
                 'License :: OSI Approved :: MIT License',
                 'Development Status :: 3 - Alpha', 'Framework :: Flask',
                 'Intended Audience :: End Users/Desktop',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: Implementation :: PyPy'
                 'Topic :: Software Development :: Libraries :: Python Modules'],
    long_description=long_description,
    install_requires=[
        'Flask',
        'Jinja2',
        'wsgiref',
        'werkzeug',
        'gunicorn',
        'whitenoise',
        'CWR-API',
        'enum34',
    ],
    tests_require=_tests_require,
    extras_require={'test': _tests_require},
)
