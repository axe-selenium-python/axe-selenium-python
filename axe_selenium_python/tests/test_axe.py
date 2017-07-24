# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import re
import time
import os
import sys


@pytest.mark.nondestructive
def test_rules(selenium, axe):
    """Assert number of rule tests matches number of available rules."""
    rules = axe.get_rules(selenium)
    assert len(rules) == 58, len(rules)


@pytest.mark.nondestructive
def test_execute(selenium, axe, pytestconfig):
    """Run axe against base_url and verify JSON output."""

    pytestconfig.data = axe.execute(selenium)

    # convert array to dictionary
    pytestconfig.violations = dict((k['id'], k) for k in pytestconfig.data['violations'])
    # assert data exists
    assert pytestconfig.data is not None, pytestconfig.data


@pytest.mark.nondestructive
def test_write_results(base_url, axe, pytestconfig):
    """Write JSON results to file."""
    # get string of current python version
    version = 'v' + str(sys.version_info[0]) + '_' + \
        str(sys.version_info[1]) + '_' + str(sys.version_info[2])
    # strip protocol and dots
    filename = re.sub('(http:\/\/|https:\/\/|\.php|\.asp|\.html)', '', base_url)
    # replace slashes with underscores
    filename = re.sub('(\/|\.)', '_', filename)
    # create filename "examplecom-datetime-python-version.json"
    filename += '-' + time.strftime('%m-%d-%y-%X') + '-' + version + '.json'
    axe.write_results(filename, pytestconfig.data)
    # check that file exists and is not empty
    assert os.path.exists(filename) and os.path.getsize(filename) > 0, \
        'Output file not found.'


@pytest.mark.nondestructive
def test_violations(axe, pytestconfig):
    """Assert that no violations were found."""
    report = axe.report(pytestconfig.violations)
    assert len(pytestconfig.violations) == 0, report


@pytest.mark.nondestructive
def test_report(axe, pytestconfig):
    """Test that report exists"""
    report = axe.report(pytestconfig.violations)
    assert report is not None, report
