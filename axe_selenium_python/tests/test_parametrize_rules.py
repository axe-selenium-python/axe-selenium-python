# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from axe_selenium_python import Axe


@pytest.mark.nondestructive
def test_get_rules(selenium, axe, pytestconfig):
    """Assert that axe.get_rules returns a non-null object"""
    pytestconfig.data = axe.execute(selenium)
    pytestconfig.violations = dict((k['id'], k) for k in pytestconfig.data['violations'])

    assert pytestconfig.data is not None, pytestconfig.data

@pytest.mark.parametrize("rule", [
    'accesskeys',
    'area-alt',
    'aria-allowed-attr',
    'aria-hidden-body',
    'aria-required-attr',
    'aria-required-children',
    'aria-required-parent',
    'aria-roles',
    'aria-valid-attr-value',
    'aria-valid-attr',
    'audio-caption',
    'blink',
    'button-name',
    'bypass',
    'checkboxgroup',
    'color-contrast',
    'definition-list',
    'dlitem',
    'document-title',
    'duplicate-id',
    'empty-heading',
    'frame-title-unique',
    'frame-title',
    'heading-order',
    'hidden-content',
    'href-no-hash',
    'html-has-lang',
    'html-lang-valid',
    'image-alt',
    'image-redundant-alt',
    'input-image-alt',
    'label-title-only',
    'label',
    'layout-table',
    'link-in-text-block',
    'link-name',
    'list',
    'listitem',
    'marquee',
    'meta-refresh',
    'meta-viewport-large',
    'meta-viewport',
    'object-alt',
    'p-as-heading',
    'radiogroup',
    'region',
    'scope-attr-valid',
    'server-side-image-map',
    'skip-link',
    'tabindex',
    'table-duplicate-name',
    'table-fake-caption',
    'td-has-header',
    'td-headers-attr',
    'th-has-data-cells',
    'valid-lang',
    'video-caption',
    'video-description',
])
@pytest.mark.nondestructive
def test_parametrize(pytestconfig, rule):
    assert rule not in pytestconfig.violations, pytestconfig.violations[rule]['help']
