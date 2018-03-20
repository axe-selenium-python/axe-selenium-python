# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from os import path
import pytest


@pytest.mark.nondestructive
def test_get_rules(axe):
    """Assert number of rule tests matches number of available rules."""
    axe.inject()
    rules = axe.get_rules()
    assert len(rules) == 58, len(rules)


@pytest.mark.nondestructive
def test_execute(axe):
    """Run axe against base_url and verify JSON output."""
    axe.inject()
    data = axe.execute()
    assert data is not None, data


@pytest.mark.nondestructive
def test_run(base_url, axe):
    """Assert that run method returns results."""
    violations = axe.run()
    assert violations is not None


@pytest.mark.nondestructive
def test_report(axe):
    """Test that report exists."""
    violations = axe.run()

    report = axe.report(violations)
    assert report is not None, report


@pytest.mark.nondestructive
def test_write_results(base_url, axe):
    """Assert that write results method creates a file."""
    axe.inject()
    data = axe.execute()
    filename = 'results.json'
    axe.write_results(filename, data)
    # check that file exists and is not empty
    assert path.exists(filename), 'Output file not found.'
    assert path.getsize(filename) > 0, 'File contains no data.'
