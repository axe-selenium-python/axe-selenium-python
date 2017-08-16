axe-selenium-python
====================

axe-selenium-python integrates aXe and selenium to enable automated web accessibility testing.

.. image:: https://img.shields.io/badge/license-MPL%202.0-blue.svg?style=plastic
   :target: https://github.com/kimberlythegeek/axe-selenium-python/blob/master/LICENSE.txt
   :alt: License
.. image:: https://img.shields.io/pypi/v/axe-selenium-python.svg?style=plastic
   :target: https://pypi.org/project/axe-selenium-python/
   :alt: PyPI
.. image:: https://img.shields.io/pypi/wheel/axe-selenium-python.svg?style=plastic
   :target: https://pypi.org/project/axe-selenium-python/
   :alt: wheel
.. image:: https://img.shields.io/travis/kimberlythegeek/axe-selenium-python.svg?style=plastic
   :target: https://travis-ci.org/kimberlythegeek/axe-selenium-python/
   :alt: Travis
.. image:: https://img.shields.io/github/issues-raw/kimberlythegeek/axe-selenium-python.svg?style=plastic
   :target: https://github.com/kimberlythegeek/axe-selenium-python/issues
   :alt: Issues


Requirements
------------

You will need the following prerequisites in order to use axe-selenium-python:

- Python 2.7 or 3.6
- pytest-selenium >= 3.0.0
- tox
- geckodriver downloaded and added to your PATH

Installation
------------

To install axe-selenium-python:

.. code-block:: bash

  $ pip install axe-selenium-python

To install pytest-axe:

.. code-block:: bash

  $ pip install pytest-axe


Usage
------
*test_accessibility.py*

.. code-block:: python

    import pytest

    from axe_selenium_python.test_accessibility import rules, report


    @pytest.mark.nondestructive
    def test_header_run_axe(selenium, axe, pytestconfig):
        pytestconfig.violations = axe.run('header', None, 'critical')
        assert pytestconfig.violations is not None


    @pytest.mark.nondestructive
    @pytest.mark.parametrize('rule', rules)
    def test_header_accessibility(rule, pytestconfig):
        violations = pytestconfig.violations
        assert rule not in violations, report(violations[rule])


The above example is currently the recommended approach. The first test runs axe
against the selenium instance, with the context set to *<header>* and stores
the results in pytestconfig.

The second test uses pytest parametrize to generate tests for each rule in the
provided list *rules*.

The method **axe.run()** accepts three parameters: *context*, *options*, and
*impact*. For more information on **context** and **options**, view the `aXe
documentation here <https://github.com/dequelabs/axe-core/blob/master/doc/API.md#parameters-axerun>`_.

The third parameter, *impact*, allows you to filter violations by their impact
level. The options are *critical*, *severe*, *moderate*, and *minor*, with the
default value set to **None**.

This will filter violations for the impact level specified, and **all violations with a higher impact level**.

Command Line Argument
*********************

.. code-block:: bash

  $ pytest --base-url http://www.mozilla.com --driver Firefox test_accessibility.py



Resources
---------

- `Issue Tracker <http://github.com/kimberlythegeek/axe-selenium-python/issues>`_
- `Code <http://github.com/kimberlythegeek/axe-selenium-python/>`_
- `pytest-axe <http://github.com/kimberlythegeek/pytest-axe/>`_
