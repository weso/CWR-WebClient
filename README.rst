CWR Web Client
===================

This projects offers a web UI to handle CWR files.

For this the `CWR Data Model API`_ is used, as a way both to represent
the contents of these files and to communicate with the services being used.

For more information about the CWR standard consult that same projects. It 
should suffice to say that it is a standard for registering musical works
created by `CISAC`_, while this application has been developed by `WESO`_ 
independently, with help from `BMAT`_.

Status
------

The project is still in the development phase.

Issues management
~~~~~~~~~~~~~~~~~

Issues are managed at the GitHub `project issues page`_.

Documentation
-------------

Documentation for the project can be found at the GitHub `project
wiki`_.

Building the code
-----------------

The application has been coded in Python, and tested for various
versions of the Python 2 interpreter.

Dependencies are indicated on requirements.txt.

Prerequisites
~~~~~~~~~~~~~

Requires Python, and has been tested on the following interpreters:

- Python 2 (2.6, 2.7)

The dependencies can be acquired using the list on requirements.txt,
with the command:

``pip install -r requirements.txt``

Getting the code
~~~~~~~~~~~~~~~~

The code can be found at the GitHub `project page`_.

To acquire it through Git use the following clone URI:

``git clone https://github.com/weso/CWR-WebClient.git``

Continuous integration
----------------------

The continuous integration information can be found at the `project CI
page`_ based on Travis CI.

License
-------

The project is released under the `MIT License`_.

.. _CISAC: http://www.cisac.org/
.. _BMAT: http://www.bmat.com/
.. _CWR Data Model API: http://www.bmat.com/
.. _WESO: http://www.weso.es/
.. _project issues page: https://github.com/weso/CWR-WebClient/issues
.. _project wiki: https://github.com/weso/CWR-WebClient/wiki
.. _project page: https://github.com/weso/CWR-WebClient
.. _project CI page: 
.. _MIT License: http://www.opensource.org/licenses/mit-license.php
