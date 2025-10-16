# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import json
from os import getcwd
from os import getenv
from os import path

import pytest
from selenium import webdriver

from axe_selenium_python import Axe

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
    opts.add_argument("--headless")
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

    assert len(data["inapplicable"]) == 75
    assert len(data["incomplete"]) == 0
    assert len(data["passes"]) == 6
    assert len(data["violations"]) == 9


@pytest.mark.nondestructive
def test_run_axe_sample_page_chrome(chrome_driver):
    """Run axe against sample page and verify JSON output is as expected."""
    data = _perform_axe_run(chrome_driver)

    assert len(data["inapplicable"]) == 75
    assert len(data["incomplete"]) == 0
    assert len(data["passes"]) == 6
    assert len(data["violations"]) == 9


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


def test_inject_reads_and_executes_script(tmp_path, mocker):
    mock_selenium = mocker.MagicMock()
    script_file = tmp_path / "axe.min.js"
    script_file.write_text("console.log('axe injected');")

    axe = Axe(mock_selenium, str(script_file))
    axe.inject()

    mock_selenium.execute_script.assert_called_once_with("console.log('axe injected');")


def test_inject_missing_script_raises_error(mocker):
    mock_selenium = mocker.MagicMock()
    axe = Axe(mock_selenium, "nonexistent.js")

    with pytest.raises(FileNotFoundError):
        axe.inject()


def test_run_with_context_and_options(mocker):
    mock_selenium = mocker.MagicMock()
    mock_selenium.execute_async_script.return_value = {"passes": []}

    axe = Axe(mock_selenium)
    context = {"include": [["#main"]]}
    options = {"runOnly": {"type": "tag", "values": ["wcag2a"]}}

    result = axe.run(context, options)

    assert result == {"passes": []}
    assert mock_selenium.execute_async_script.called
    command = mock_selenium.execute_async_script.call_args[0][0]
    assert "axe.run" in command
    assert "wcag2a" in command


@pytest.mark.parametrize("context,options", [
    ({"include": [["#main"]]}, None),
    (None, {"runOnly": {"type": "tag", "values": ["wcag2aa"]}}),
])
def test_run_with_single_arg_cases(mocker, context, options):
    mock_selenium = mocker.MagicMock()
    mock_selenium.execute_async_script.return_value = {"result": "ok"}
    axe = Axe(mock_selenium)
    axe.run(context, options)
    called_script = mock_selenium.execute_async_script.call_args[0][0]
    assert "axe.run" in called_script


def test_run_with_invalid_script_raises(mocker):
    mock_selenium = mocker.MagicMock()
    mock_selenium.execute_async_script.side_effect = Exception("JS failed")

    axe = Axe(mock_selenium)
    with pytest.raises(Exception, match="JS failed"):
        axe.run()


def test_report_generates_expected_string(mocker):
    axe = Axe(mocker.MagicMock())
    violations = [{
        "id": "color-contrast",
        "description": "Elements must have sufficient color contrast",
        "helpUrl": "https://example.com",
        "impact": "serious",
        "tags": ["wcag2aa", "contrast"],
        "nodes": [{
            "target": ["#header"],
            "all": [{"message": "Check color contrast"}],
            "any": [],
            "none": []
        }]
    }]

    report = axe.report(violations)
    assert "Found 1 accessibility violations" in report
    assert "color-contrast" in report
    assert "#header" in report
    assert "serious" in report


def test_report_with_empty_list_returns_no_violation_text(mocker):
    axe = Axe(mocker.MagicMock())
    report = axe.report([])
    assert "Found 0 accessibility violations" in report


def test_write_results_default_name(tmp_path, mocker, monkeypatch):
    axe = Axe(mocker.MagicMock())
    monkeypatch.chdir(tmp_path)
    data = {"k": "v"}
    axe.write_results(data)
    default_file = tmp_path / "results.json"
    assert default_file.exists()


def test_write_results_with_invalid_path(mocker):
    axe = Axe(mocker.MagicMock())
    data = {"key": "value"}

    # Attempt writing to directory that does not exist
    bad_path = "/invalid_dir/results.json"
    with pytest.raises(OSError):
        axe.write_results(data, bad_path)


def test_write_results_with_unserializable_data(mocker, tmp_path):
    axe = Axe(mocker.MagicMock())
    filename = tmp_path / "results.json"

    # Functions are not JSON-serializable
    data = {"func": lambda x: x}
    with pytest.raises(TypeError):
        axe.write_results(data, str(filename))
