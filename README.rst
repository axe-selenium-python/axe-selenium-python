axe-selenium-python
====================

axe-selenium-python integrates aXe and selenium to enable automated web accessibility testing.

*This version of axe-selenium-python is using axe-core@3.0.0.*

.. image:: https://img.shields.io/badge/license-MPL%202.0-blue.svg?style=for-the-badge
   :target: https://github.com/mozilla-services/axe-selenium-python/blob/master/LICENSE.txt
   :alt: License
.. image:: https://img.shields.io/pypi/v/axe-selenium-python.svg?style=for-the-badge
   :target: https://pypi.org/project/axe-selenium-python/
   :alt: PyPI
.. image:: https://img.shields.io/travis/mozilla-services/axe-selenium-python.svg?style=for-the-badge
   :target: https://travis-ci.org/mozilla-services/axe-selenium-python
   :alt: Travis
.. image:: https://img.shields.io/pypi/wheel/axe-selenium-python.svg?style=for-the-badge
   :target: https://pypi.org/project/axe-selenium-python/
   :alt: wheel
.. image:: https://img.shields.io/github/issues-raw/mozilla-services/axe-selenium-python.svg?style=for-the-badge
   :target: https://github.com/mozilla-services/axe-selenium-python/issues
   :alt: Issues


Requirements
------------

You will need the following prerequisites in order to use axe-selenium-python:

- selenium >= 3.0.0
- Python 2.7 or 3.6
- `geckodriver <https://github.com/mozilla/geckodriver/releases>`_ downloaded and `added to your PATH <https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path#answer-40208762>`_

Installation
------------

To install axe-selenium-python:

.. code-block:: bash

  $ pip install axe-selenium-python


Usage
------

.. code-block:: python

 import pytest
  from selenium import webdriver
  from axe_selenium_python import Axe

  def test_google():
      driver = webdriver.Firefox()
      driver.get("http://www.google.com")
      axe = Axe(driver)
      # Inject axe-core javascript into page.
      axe.inject()
      # Run axe accessibility checks.
      results = axe.execute()
      # Write results to file
      axe.write_results('a11y.json', results)
      driver.close()
      # Assert no violations are found
      assert len(results["violations"]) == 0, axe.report(results["violations"])

The method ``axe.execute()`` accepts two parameters: ``context`` and ``options``.

For more information on ``context`` and ``options``, view the `aXe documentation here <https://github.com/dequelabs/axe-core/blob/master/doc/API.md#parameters-axerun>`_.

Resources
---------

- `Issue Tracker <http://github.com/mozilla-services/axe-selenium-python/issues>`_
- `Code <http://github.com/mozilla-services/axe-selenium-python/>`_
- `pytest-axe <http://github.com/kimberlythegeek/pytest-axe/>`_
