# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
from unittest import TestCase

from axe_selenium_python import Axe

class TestGetScriptContents(TestCase):

    def test_is_string(self):
        a = Axe()
        script = a.get_contents('axe_selenium_python/src/test/resources/axe.min.js')
        self.assertTrue(isinstance(script, basestring))
