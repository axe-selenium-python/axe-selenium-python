axe-selenium-python
====================

axe-selenium-python integrates aXe and selenium to enable automated web accessibility testing.

*This version of axe-selenium-python is using axe-core@2.6.1.*

.. image:: https://img.shields.io/badge/license-MPL%202.0-blue.svg?style=for-the-badge
   :target: https://github.com/kimberlythegeek/axe-selenium-python/blob/master/LICENSE.txt
   :alt: License
.. image:: https://img.shields.io/pypi/v/axe-selenium-python.svg?style=for-the-badge
   :target: https://pypi.org/project/axe-selenium-python/
   :alt: PyPI
.. image:: https://img.shields.io/pypi/wheel/axe-selenium-python.svg?style=for-the-badge
   :target: https://pypi.org/project/axe-selenium-python/
   :alt: wheel
.. image:: https://img.shields.io/travis/kimberlythegeek/axe-selenium-python.svg?style=for-the-badge
   :target: https://travis-ci.org/kimberlythegeek/axe-selenium-python/
   :alt: Travis
.. image:: https://img.shields.io/github/issues-raw/kimberlythegeek/axe-selenium-python.svg?style=for-the-badge
   :target: https://github.com/kimberlythegeek/axe-selenium-python/issues
   :alt: Issues


Requirements
------------

You will need the following prerequisites in order to use axe-selenium-python:

- Python 2.7 or 3.6
- pytest-selenium >= 3.0.0
- `geckodriver <https://github.com/mozilla/geckodriver/releases>`_ downloaded and `added to your PATH <https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path#answer-40208762>`_

Optional
^^^^^^^^
- tox

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
``test_accessibility.py``

.. code-block:: python

   import pytest

    @pytest.mark.nondestructive
    def test_header_accessibility(axe):
        violations = axe.run('header', None, 'critical')
        assert len(violations) == 0, axe.report(violations)



The above example runs aXe against only the content within the *<header>* tag, and filters for violations labeled ``critical``.

The method ``axe.run()`` accepts three parameters: ``context``, ``options``, and
``impact``.

For more information on ``context`` and ``options``, view the `aXe
documentation here <https://github.com/dequelabs/axe-core/blob/master/doc/API.md#parameters-axerun>`_.

The third parameter, ``impact``, allows you to filter violations by their impact
level. The options are ``'critical'``, ``'serious'`` and ``'minor'``, with the
default value set to ``None``.

This will filter violations for the impact level specified, and **all violations with a higher impact level**.

To run the above test you will need to specify the browser instance to be invoked, and the **base_url**.

.. code-block:: bash

  $ pytest --base-url http://www.mozilla.com --driver Firefox test_accessibility.py



Resources
---------

- `Issue Tracker <http://github.com/kimberlythegeek/axe-selenium-python/issues>`_
- `Code <http://github.com/kimberlythegeek/axe-selenium-python/>`_
- `pytest-axe <http://github.com/kimberlythegeek/pytest-axe/>`_
