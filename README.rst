CWR Web Client
===================

This projects offers a web UI to handle CWR files.

For this the `CWR Data Model API`_ is used, as a way both to represent
the contents of these files and to communicate with the services being used.

For more information about the CWR standard consult that same projects. It 
should suffice to say that it is a standard for registering musical works
created by `CISAC`_, while this application has been developed by `WESO`_ 
independently, with help from `BMAT`_.

Documentation
-------------

The current version is under development. No public documentation is still offered.

Status
------

The project is still in the development phase.

Issues management
~~~~~~~~~~~~~~~~~

Issues are managed at the GitHub `project issues page`_.

Building the code
-----------------

The application has been coded in Python, using the Flask framework.

Prerequisites
~~~~~~~~~~~~~

The project has been tested in the following versions of the interpreter:

- Python 2.6
- Python 2.7
- Pypy

Al other dependencies are indicated on requirements.txt, which can be installed with the command:

``pip install -r requirements.txt``

Getting the code
~~~~~~~~~~~~~~~~

The code can be found at the GitHub `project page`_.

License
-------

The project is released under the `MIT License`_.

.. _CISAC: http://www.cisac.org/
.. _BMAT: http://www.bmat.com/
.. _CWR Data Model API: https://github.com/weso/CWR-DataApi
.. _WESO: http://www.weso.es/
.. _project issues page: https://github.com/weso/CWR-WebClient/issues
.. _project page: https://github.com/weso/CWR-WebClient
.. _MIT License: http://www.opensource.org/licenses/mit-license.php
