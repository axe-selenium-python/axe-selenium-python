# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest


class TestAccessibility:

    def report(rule):
        # return json.dumps(rule, indent=4, sort_keys=True)
        string = '\n\n\nRule Violated:\n' + rule['id'] + ' - ' + rule['description'] + \
            '\n\tURL: ' + rule['helpUrl'] + \
            '\n\tImpact Level: ' + rule['impact'] + \
            '\n\tTags:'
        for tag in rule['tags']:
            string += ' ' + tag
        string += '\n\tElements Affected:'
        i = 1
        for node in rule['nodes']:
            for target in node['target']:
                string += '\n\t' + str(i) + ') Target: ' + target
                i += 1
            for item in node['all']:
                string += '\n\t\t' + item['message']
            for item in node['any']:
                string += '\n\t\t' + item['message']
            for item in node['none']:
                string += '\n\t\t' + item['message']
        string += '\n\n\n'
        return string

    _rules = [
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
        'video-description'
    ]

    @pytest.mark.nondestructive
    def test_execute(self, axe, pytestconfig):
        """Run axe against base_url and verify JSON output."""

        pytestconfig.data = axe.execute()

        # convert array to dictionary
        pytestconfig.violations = dict((k['id'], k) for k in pytestconfig.data['violations'])
        # assert data exists
        assert pytestconfig.data is not None, pytestconfig.data

    @pytest.mark.parametrize("rule", _rules)
    @pytest.mark.nondestructive
    def test_accessibility_rules(self, pytestconfig, rule):
        assert rule not in pytestconfig.violations, pytestconfig.violations[rule]['help']
