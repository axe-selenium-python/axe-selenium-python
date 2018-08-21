# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from os import path

import pytest
from selenium import webdriver

from ..axe import Axe

_DEFAULT_TEST_FILE = path.join(path.dirname(__file__), 'test_page.html')


@pytest.fixture(params=('Firefox', pytest.mark.xfail('Chrome', reason="issue #118")))
def driver(request):
    driver = getattr(webdriver, request.param)()
    yield driver
    driver.close()


@pytest.mark.nondestructive
def test_run_axe_sample_page(driver):
    """Run axe against sample page and verify JSON output is as expected."""
    driver.get('file://' + _DEFAULT_TEST_FILE)
    axe = Axe(driver)
    axe.inject()
    data = axe.execute()

    assert len(data["inapplicable"]) == 46
    assert len(data["incomplete"]) == 0
    assert len(data["passes"]) == 7
    assert len(data["violations"]) == 8
