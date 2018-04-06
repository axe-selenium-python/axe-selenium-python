# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from os import path

import pytest


@pytest.mark.nondestructive
def test_execute(axe):
    """Run axe against base_url and verify JSON output."""
    axe.inject()
    data = axe.execute()
    assert data is not None, data


@pytest.mark.nondestructive
def test_report(axe):
    """Test that report exists."""
    axe.inject()
    results = axe.execute()
    violations = results["violations"]
    report = axe.report(violations)
    assert report is not None, report


@pytest.mark.nondestructive
def test_write_results(base_url, axe):
    """Assert that write results method creates a non-empty file."""
    axe.inject()
    data = axe.execute()
    filename = 'results.json'
    axe.write_results(filename, data)
    # check that file exists and is not empty
    assert path.exists(filename), 'Output file not found.'
    assert path.getsize(filename) > 0, 'File contains no data.'
