# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from datetime import datetime

import pytest
from py.xml import html


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    """Add description and sortable time header to HTML report."""
    cells.insert(2, html.th("Description"))
    cells.insert(0, html.th("Time", class_="sortable time", col="time"))


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    """Add description and sortable time column to HTML report."""
    cells.insert(2, html.td(report.description))
    cells.insert(1, html.td(datetime.utcnow(), class_="col-time"))


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    """Make HTML report using test-function docstrings as description."""
    outcome = yield
    report = outcome.get_result()
    # add docstring to 'description' column
    report.description = str(item.function.__doc__)
