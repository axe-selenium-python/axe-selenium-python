# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


import pytest
import time
from selenium.webdriver.common.keys import Keys
from axe_selenium_python import Axe


class TestAxeConfig:

    # @pytest.mark.nondestructive
    @pytest.mark.xfail
    def test_mozillians_full(self, axe):
        """Run axe against mozillians.org and assert no violations found."""

        response = axe.execute()
        violations = response['violations']

        # write result to file
        axe.write_results('mozillians_full.json', response)
        # assert response exists
        assert len(violations) == 0, axe.report(violations)

    # @pytest.mark.nondestructive
    @pytest.mark.xfail
    def test_mozillians_context(self, axe):
        """Run axe against a specific element of mozillians.org."""

        response = axe.execute('#language')
        violations = response['violations']

        # write result to file
        axe.write_results('mozillians_context.json', response)
        # assert response exists
        assert len(violations) == 0, axe.report(violations)

    @pytest.mark.nondestructive
    # @pytest.mark.xfail
    def test_mozillians_search_full(self, selenium, base_url):
        """
        Perform search using keystrokes, and run axe on results page.
        """
        selenium.get(base_url)
        html = selenium.switch_to.active_element
        elem = html['value']
        elem.send_keys(Keys.TAB)
        elem.send_keys('mbrandt')
        elem.send_keys(Keys.ENTER)

        time.sleep(1)
        axe = Axe(selenium)
        response = axe.execute()
        violations = response['violations']

        axe.write_results('mozillians_search_full.json', response)
        assert len(violations) == 0, axe.report(violations)

    @pytest.mark.nondestructive
    # @pytest.mark.xfail
    def test_mozillians_search_context(self, selenium, base_url):
        """
        Perform search using keystrokes, and run axe on single element of page.
        """
        selenium.get(base_url)
        html = selenium.switch_to.active_element
        elem = html['value']
        elem.send_keys(Keys.TAB)
        elem.send_keys('mbrandt')
        elem.send_keys(Keys.ENTER)

        time.sleep(1)
        axe = Axe(selenium)
        response = axe.execute('#main > p.alert > a')
        violations = response['violations']

        axe.write_results('mozillians_search_context.json', response)
        assert len(violations) == 0, axe.report(violations)
