# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import json
from os import getcwd, getenv, path

import pytest
from selenium import webdriver

from ..axe import Axe

_DEFAULT_TEST_FILE = path.join(path.dirname(__file__), "test_page.html")


@pytest.fixture
def firefox_driver():
    driver = webdriver.Firefox()
    yield driver
    driver.close()


@pytest.fixture
def chrome_driver():
    opts = webdriver.ChromeOptions()
    opts.headless = True
    opts.add_argument("--no-sandbox")
    driver_path = getenv("CHROMEDRIVER_PATH")
    driver = (
        webdriver.Chrome(options=opts, executable_path=driver_path)
        if driver_path
        else webdriver.Chrome(options=opts)
    )
    yield driver
    driver.close()


@pytest.mark.nondestructive
def test_run_axe_sample_page_firefox(firefox_driver):
    """Run axe against sample page and verify JSON output is as expected."""
    data = _perform_axe_run(firefox_driver)

    assert len(data["inapplicable"]) == 60
    assert len(data["incomplete"]) == 0
    assert len(data["passes"]) == 7
    assert len(data["violations"]) == 8


@pytest.mark.nondestructive
def test_run_axe_sample_page_chrome(chrome_driver):
    """Run axe against sample page and verify JSON output is as expected."""
    data = _perform_axe_run(chrome_driver)

    assert len(data["inapplicable"]) == 60
    assert len(data["incomplete"]) == 0
    assert len(data["passes"]) == 7
    assert len(data["violations"]) == 8


def _perform_axe_run(driver):
    driver.get("file://" + _DEFAULT_TEST_FILE)
    axe = Axe(driver)
    axe.inject()
    data = axe.run()
    return data


def test_write_results_to_file(tmpdir, mocker):
    axe = Axe(mocker.MagicMock())
    data = {"testKey": "testValue"}
    filename = path.join(str(tmpdir), "results.json")

    axe.write_results(data, filename)

    with open(filename) as f:
        actual_file_contents = json.loads(f.read())

    assert data == actual_file_contents


def test_write_results_without_filepath(mocker):
    axe = Axe(mocker.MagicMock())
    data = {"testKey": "testValue"}
    cwd = getcwd()
    filename = path.join(cwd, "results.json")

    axe.write_results(data, filename)
    with open(filename) as f:
        actual_file_contents = json.loads(f.read())

    assert data == actual_file_contents
    assert path.dirname(filename) == cwd
