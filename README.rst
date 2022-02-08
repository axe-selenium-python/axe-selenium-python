axe-selenium-python
====================

axe-selenium-python integrates aXe and selenium to enable automated web accessibility testing.


**This version of axe-selenium-python is using axe-core@4.3.5.**


.. image:: https://img.shields.io/badge/license-MPL%202.0-blue.svg
   :target: https://github.com/mozilla-services/axe-selenium-python/blob/master/LICENSE.txt
   :alt: License
.. image:: https://img.shields.io/pypi/v/axe-selenium-python.svg
   :target: https://pypi.org/project/axe-selenium-python/
   :alt: PyPI
.. image:: https://img.shields.io/travis/mozilla-services/axe-selenium-python.svg
   :target: https://travis-ci.org/mozilla-services/axe-selenium-python
   :alt: Travis
.. image:: https://img.shields.io/github/issues-raw/mozilla-services/axe-selenium-python.svg
   :target: https://github.com/mozilla-services/axe-selenium-python/issues
   :alt: Issues
.. image:: https://api.dependabot.com/badges/status?host=github&repo=mozilla-services/axe-selenium-python
   :target: https://dependabot.com
   :alt: Dependabot
.. image:: https://coveralls.io/repos/github/mozilla-services/axe-selenium-python/badge.svg?branch=master
   :target: https://coveralls.io/github/mozilla-services/axe-selenium-python?branch=master
   :alt: Coveralls



Requirements
------------

You will need the following prerequisites in order to use axe-selenium-python:

- selenium >= 3.0.0
- Python 2.7 or 3.6
- The appropriate driver for the browser you intend to use, downloaded and added to your path, e.g. geckodriver for Firefox:

  - `geckodriver <https://github.com/mozilla/geckodriver/releases>`_ downloaded and `added to your PATH <https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path#answer-40208762>`_

Installation
------------

To install axe-selenium-python:

.. code-block:: bash

  $ pip install axe-selenium-python


Usage
------

.. code-block:: python

  from selenium import webdriver
  from axe_selenium_python import Axe

  def test_google():
      driver = webdriver.Firefox()
      driver.get("http://www.google.com")
      axe = Axe(driver)
      # Inject axe-core javascript into page.
      axe.inject()
      # Run axe accessibility checks.
      results = axe.run()
      # Write results to file
      axe.write_results(results, 'a11y.json')
      driver.close()
      # Assert no violations are found
      assert len(results["violations"]) == 0, axe.report(results["violations"])

The method ``axe.run()`` accepts two parameters: ``context`` and ``options``.

For more information on ``context`` and ``options``, view the `aXe documentation here <https://github.com/dequelabs/axe-core/blob/master/doc/API.md#parameters-axerun>`_.

Contributing
------------

Fork the repository and submit PRs with bug fixes and enhancements;
contributions are very welcome.

Node dependencies must be installed by running `npm install` inside the axe-selenium-python directory.

You can run the tests using
`tox <https://tox.readthedocs.io/en/latest/>`_:

.. code-block:: bash

  $ tox

Resources
---------

- `Issue Tracker <http://github.com/mozilla-services/axe-selenium-python/issues>`_
- `Code <http://github.com/mozilla-services/axe-selenium-python/>`_
- `pytest-axe <http://github.com/mozilla-services/pytest-axe/>`_

CHANGELOG
^^^^^^^^^^^^^^

version 2.1.5
*************
**Breaks backwards compatibility**:

- The Axe class method ``execute`` has been renamed to ``run`` to mirror the method in the axe-core API.

version 2.1.0
**************
- Created package.json file to maintain axe-core dependency
- Replaced unit tests with more meaningful integration tests
  - included a sample html file for integration tests

version 2.0.0
**************
- All functionalities that are not part of axe-core have been moved into a separate package, ``pytest-axe``. This includes:

  - ``run_axe`` helper method
  - ``get_rules`` Axe class method
  - ``run`` Axe class method
  - ``impact_included`` Axe class method
  - ``analyze`` Axe class method.

The purpose of this change is to separate implementations that are specific to the Mozilla Firefox Test Engineering team, and leave the base ``axe-selenium-python`` package for a more broad use case. This package was modeled off of Deque's Java package, axe-selenium-java, and will now more closely mirror it.

All functionalities can still be utilized when using ``axe-selenium-python`` in conjunction with ``pytest-axe``.

version 1.2.3
**************
- Added the analyze method to the Axe class. This method runs accessibility checks, and writes the JSON results to file based on the page URL and the timestamp.
- Writing results to file can be enabled by setting the environment variable ``ACCESSIBILITY_REPORTING=true``. The files will be written to ``results/`` directory, which must be created if it does not already exist.
- Accessibility checks can be disabled by setting the environment variable ``ACCESSIBILITY_DISABLED=true``.

version 1.2.1
**************
- Updated axe to ``axe-core@2.6.1``
- Modified impact_included class method to reflect changes to the aXe API:
- There are now only 3 impact levels: 'critical', 'serious', and 'minor'

version 1.0.0
**************
- Updated usage examples in README
- Added docstrings to methods lacking documentation
- Removed unused files

version 0.0.3
**************
- Added run method to Axe class to simplify the usage in existing test suites
- run method includes the ability to set what impact level to test for: 'minor', 'moderate', 'severe', 'critical'

version 0.0.28
****************
- Added selenium instance as a class attribute
- Changed file paths to OS independent structure
- Fixed file read operations to use with keyword


version 0.0.21
***************
- Fixed include of aXe API file and references to it
- Updated README

How to upgrade to new version of axe-core
-----------------------------------------

- Updates to axe-selenium-python/axe_selenium_python/package.json
    - Update the dependencies to the needed version of axe core
    - Example code below

.. code-block:: bash

    "dependencies": {
        "axe-core": ">=4.3.5"
    }


- Updates to axe-selenium-python/axe_selenium_python/package-lock.json
    - In the axe-core blob, update version and resolved to the version needed.
    - Navigate to registry using https://registry.npmjs.org/axe-core/ and search for resolved .tgz and copy the integrity key.
        and update in package-lock.json file
    - Example code below

.. code-block:: bash

    "axe-core": {
      "version": "4.3.5",
      "resolved": "https://registry.npmjs.org/axe-core/-/axe-core-4.3.5.tgz",
      "integrity": "sha512-WKTW1+xAzhMS5dJsxWkliixlO/PqC4VhmO9T4juNYcaTg9jzWiJsou6m5pxWYGfigWbwzJWeFY6z47a+4neRXA=="
    }

- Get the latest axe.min.js
    - cd into axe-selenium-python/axe_selenium_python
    - Run `npm install` inside the axe-selenium-python directory.
    - Copy axe-selenium-python/axe_selenium_python/node_modules/axe-core/axe.min.js file and replace
        axe-selenium-python/axe_selenium_python/tests/src/axe.min.js.
    - Open axe-selenium-python/axe_selenium_python/tests/src/axe.min.js file and validate the needed version is available.
    - Delete the axe-selenium-python/axe_selenium_python/node_modules folder.

- Push the branch up and PR.
- To test, add the below to a req.txt file and try to pip install. Validate that axe-selenium-python/axe_selenium_python/tests/src/axe.min.js file
    is pointing to the needed version. Also compare the web plugin and automated test results should match.

.. code-block:: bash

    axe-selenium-python @ git+https://github.com/QualityEnablement/axe-selenium-python.git@PR_111#egg=axe-selenium-python