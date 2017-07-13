# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


import pytest
import re
import time
import os
import sys

from axe_selenium_python import Axe


class TestAxe:

    @pytest.mark.nondestructive
    def test_execute(self, selenium, base_url, pytestconfig):
        """Run axe against base_url and verify JSON output."""

        script_url = './axe_selenium_python/tests/src/axe.min.js'
        selenium.get(base_url)
        axe = Axe(selenium, script_url)
        response = axe.execute(selenium)

        pytestconfig.axe = axe
        pytestconfig.test_results = response
        # convert array to dictionary
        pytestconfig.violations = dict((k['id'], k) for k in response['violations'])
        # assert response exists
        assert response is not None, response
