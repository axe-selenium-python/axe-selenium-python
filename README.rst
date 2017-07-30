axe-selenium-python
====================

axe-selenium-python integrates aXe and selenium to enable automated web accessibility testing.

.. image:: https://img.shields.io/badge/license-MPL%202.0-blue.svg
   :target: https://github.com/kimberlythegeek/axe-selenium-python/blob/master/LICENSE.txt
   :alt: License
.. image:: https://img.shields.io/pypi/v/axe-selenium-python.svg
   :target: https://pypi.org/project/axe-selenium-python/
   :alt: PyPI
.. image:: https://img.shields.io/github/issues-raw/kimberlythegeek/axe-selenium-python.svg
   :target: https://github.com/kimberlythegeek/axe-selenium-python/issues
   :alt: Issues

Requirements
------------

You will need the following prerequisites in order to use pytest-html:

- Python 2.7 or 3.6
- pytest-selenium >= 3.0.0

Installation
------------

To install axe-selenium-python:

.. code-block:: bash

  $ pip install axe-selenium-python

Usage
-----
To run tests using pytest-selenium (a dependency of axe-selenium-python), tests must be marked with the non-destructive pytest decorator:

.. code-block:: python

 @pytest.mark.nondestructive
  def test_my_test_function:
    . . .

Test suites using axe-selenium-python must import pytest and the Axe class.

Tests not using the axe pytest fixture must use the selenium pytest fixture.

pytest-selenium relies on the `**base_url** <https://github.com/pytest-dev/pytest-base-url>`_ fixture, which can be set in a configuration file, or as a command line argument.

Configuration File
******************

.. code-block:: ini

 [pytest]
  base_url = http://www.example.com

Command Line Argument
*********************

.. code-block:: bash

  $ pytest --base-url http://www.example.com

Example Test Function
*********************

*test_accessibility.py*

.. code-block:: python

 import pytest
  from axe_selenium_python import Axe

  @pytest.mark.nondestructive
  def test_accessibility(self, selenium):

    axe = Axe(selenium)
    response = axe.execute()

    assert len(response['violations']) == 0, axe.report()


Resources
---------

- `Issue Tracker <http://github.com/kimberlythegeek/axe-selenium-python/issues>`_
- `Code <http://github.com/kimberlythegeek/axe-selenium-python/>`_
