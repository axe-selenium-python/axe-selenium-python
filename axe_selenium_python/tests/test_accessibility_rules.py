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

    @pytest.mark.nondestructive
    def test_write_results(self, base_url, pytestconfig):
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
        pytestconfig.axe.write_results(filename, pytestconfig.test_results)
        # check that file exists and is not empty
        assert os.path.exists(filename) and os.path.getsize(filename) > 0, \
            'Output file not found.'

    @pytest.mark.nondestructive
    def test_violations(self, pytestconfig):
        """Assert that no violations were found."""
        assert len(pytestconfig.violations) == 0, pytestconfig.axe.report(pytestconfig.violations)

    @pytest.mark.nondestructive
    def test_report(self, pytestconfig):
        """Test that report exists"""
        report = pytestconfig.axe.report(pytestconfig.violations)
        assert report is not None, report

    @pytest.mark.nondestructive
    def test_accesskeys(self, pytestconfig):
        """Ensures every accesskey attribute value is unique."""
        assert pytestconfig.violations.get('accesskeys') is None, pytestconfig.violations['accesskeys']['help']

    @pytest.mark.nondestructive
    def test_area_alt(self, pytestconfig):
        """Ensures <area> elements of image maps have alternate text."""
        assert pytestconfig.violations.get('area-alt') is None, pytestconfig.violations['area-alt']['help']

    @pytest.mark.nondestructive
    def test_aria_allowed_attr(self, pytestconfig):
        """Ensures ARIA attributes are allowed for an element's role."""
        assert pytestconfig.violations.get('aria-allowed-attr') is None, pytestconfig.violations['aria-allowed-attr']['help']

    @pytest.mark.nondestructive
    def test_aria_required_attr(self, pytestconfig):
        """Ensures elements with ARIA roles have all required ARIA attributes."""
        assert pytestconfig.violations.get('aria-required-attr') is None, pytestconfig.violations['aria-required-attr']['help']

    @pytest.mark.nondestructive
    def test_aria_required_children(self, pytestconfig):
        """Ensures elements with an ARIA role that require child roles contain them."""
        assert pytestconfig.violations.get('aria-required-children') is None, pytestconfig.violations['aria-required-children']['help']

    @pytest.mark.nondestructive
    def test_aria_required_parent(self, pytestconfig):
        """Ensures elements with an ARIA role that require parent roles are contained by them."""
        assert pytestconfig.violations.get('aria-required-parent') is None, pytestconfig.violations['aria-required-parent']['help']

    @pytest.mark.nondestructive
    def test_aria_roles(self, pytestconfig):
        """Ensures all elements with a role attribute use a valid value."""
        assert pytestconfig.violations.get('aria-roles') is None, pytestconfig.violations['aria-roles']['help']

    @pytest.mark.nondestructive
    def test_aria_valid_attr_value(self, pytestconfig):
        """Ensures all ARIA attributes have valid values."""
        assert pytestconfig.violations.get('aria-valid-attr-value') is None, pytestconfig.violations['aria-valid-attr-value']['help']

    @pytest.mark.nondestructive
    def test_aria_valid_attr(self, pytestconfig):
        """Ensures attributes that begin with aria- are valid ARIA attributes."""
        assert pytestconfig.violations.get('aria-valid-attr') is None, pytestconfig.violations['aria-valid-attr']['help']

    @pytest.mark.nondestructive
    def test_audio_caption(self, pytestconfig):
        """Ensures <audio> elements have captions."""
        assert pytestconfig.violations.get('audio-caption') is None, pytestconfig.violations['audio-caption']['help']

    @pytest.mark.nondestructive
    def test_blink(self, pytestconfig):
        """Ensures <blink> elements are not used."""
        assert pytestconfig.violations.get('blink') is None, pytestconfig.violations['blink']['help']

    @pytest.mark.nondestructive
    def test_button_name(self, pytestconfig):
        """Ensures buttons have discernible text."""
        assert pytestconfig.violations.get('button-name') is None, pytestconfig.violations['button-name']['help']

    @pytest.mark.nondestructive
    def test_bypass(self, pytestconfig):
        """Ensures each page has at least one mechanism for a user to bypass navigation and jump straight to the content."""
        assert pytestconfig.violations.get('bypass') is None, pytestconfig.violations['bypass']['help']

    @pytest.mark.nondestructive
    def test_checkboxgroup(self, pytestconfig):
        """Ensures related <input type="checkbox"> elements have a group and that that group designation is consistent."""
        assert pytestconfig.violations.get('checkboxgroup') is None, pytestconfig.violations['checkboxgroup']['help']

    @pytest.mark.nondestructive
    def test_color_contrast(self, pytestconfig):
        """Ensures the contrast between foreground and background colors meets WCAG 2 AA contrast ratio thresholds."""
        assert pytestconfig.violations.get('color-contrast') is None, pytestconfig.violations['color-contrast']['help']

    @pytest.mark.nondestructive
    def test_definition_list(self, pytestconfig):
        """Ensures <dl> elements are structured correctly."""
        assert pytestconfig.violations.get('definition-list') is None, pytestconfig.violations['definition-list']['help']

    @pytest.mark.nondestructive
    def test_dlitem(self, pytestconfig):
        """Ensures <dt> and <dd> elements are contained by a <dl>."""
        assert pytestconfig.violations.get('dlitem') is None, pytestconfig.violations['dlitem']['help']

    @pytest.mark.nondestructive
    def test_document_title(self, pytestconfig):
        """Ensures each HTML document contains a non-empty <title> element."""
        assert pytestconfig.violations.get('document-title') is None, pytestconfig.violations['document-title']['help']

    @pytest.mark.nondestructive
    def test_duplicate_id(self, pytestconfig):
        """Ensures every id attribute value is unique."""
        assert pytestconfig.violations.get('duplicate-id') is None, pytestconfig.violations['duplicate-id']['help']

    @pytest.mark.nondestructive
    def test_empty_heading(self, pytestconfig):
        """Ensures headings have discernible text."""
        assert pytestconfig.violations.get('empty-heading') is None, pytestconfig.violations['empty-heading']['help']

    @pytest.mark.nondestructive
    def test_frame_title_unique(self, pytestconfig):
        """Ensures <iframe> and <frame> elements contain a unique title attribute."""
        assert pytestconfig.violations.get('frame-title-unique') is None, pytestconfig.violations['frame-title-unique']['help']

    @pytest.mark.nondestructive
    def test_frame_title(self, pytestconfig):
        """Ensures <iframe> and <frame> elements contain a non-empty title attribute."""
        assert pytestconfig.violations.get('frame-title') is None, pytestconfig.violations['frame-title']['help']

    @pytest.mark.nondestructive
    def test_heading_order(self, pytestconfig):
        """Ensures the order of headings is semantically correct."""
        assert pytestconfig.violations.get('heading-order') is None, pytestconfig.violations['heading-order']['help']

    @pytest.mark.nondestructive
    def test_href_no_hash(self, pytestconfig):
        """Ensures that href values are valid link references to promote only using anchors as links."""
        assert pytestconfig.violations.get('href-no-hash') is None, pytestconfig.violations['href-no-hash']['help']

    @pytest.mark.nondestructive
    def test_html_has_lang(self, pytestconfig):
        """Ensures every HTML document has a lang attribute."""
        assert pytestconfig.violations.get('html-has-lang') is None, pytestconfig.violations['html-has-lang']['help']

    @pytest.mark.nondestructive
    def test_html_lang_valid(self, pytestconfig):
        """Ensures the lang attribute of the <html> element has a valid value."""
        assert pytestconfig.violations.get('html-lang-valid') is None, pytestconfig.violations['html-lang-valid']['help']

    @pytest.mark.nondestructive
    def test_image_alt(self, pytestconfig):
        """Ensures <img> elements have alternate text or a role of none or presentation."""
        assert pytestconfig.violations.get('image-alt') is None, pytestconfig.violations['image-alt']['help']

    @pytest.mark.nondestructive
    def test_image_redundant_alt(self, pytestconfig):
        """Ensure button and link text is not repeated as image alternative."""
        assert pytestconfig.violations.get('image-redundant-alt') is None, pytestconfig.violations['image-redundant-alt']['help']

    @pytest.mark.nondestructive
    def test_input_image_alt(self, pytestconfig):
        """Ensures <input type="image"> elements have alternate text."""
        assert pytestconfig.violations.get('input-image-alt') is None, pytestconfig.violations['input-image-alt']['help']

    @pytest.mark.nondestructive
    def test_label_title_only(self, pytestconfig):
        """Ensures that every form element is not solely labeled using the title or aria-describedby attributes."""
        assert pytestconfig.violations.get('label-title-only') is None, pytestconfig.violations['label-title-only']['help']

    @pytest.mark.nondestructive
    def test_label(self, pytestconfig):
        """Ensures every form element has a label."""
        assert pytestconfig.violations.get('label') is None, pytestconfig.violations['label']['help']

    @pytest.mark.nondestructive
    def test_layout_table(self, pytestconfig):
        """Ensures presentational <table> elements do not use <th>, <caption> elements or the summary attribute."""
        assert pytestconfig.violations.get('layout-table') is None, pytestconfig.violations['layout-table']['help']

    @pytest.mark.nondestructive
    def test_link_in_text_block(self, pytestconfig):
        """Ensures presentational <table> elements do not use <th>, <caption> elements or the summary attribute."""
        assert pytestconfig.violations.get('link-in-text-block') is None, pytestconfig.violations['link-in-text-block']['help']

    @pytest.mark.nondestructive
    def test_link_name(self, pytestconfig):
        """Ensures links have discernible text."""
        assert pytestconfig.violations.get('link-name') is None, pytestconfig.violations['link-name']['help']

    @pytest.mark.nondestructive
    def test_list(self, pytestconfig):
        """Ensures that lists are structured correctly."""
        assert pytestconfig.violations.get('list') is None, pytestconfig.violations['list']['help']

    @pytest.mark.nondestructive
    def test_listitem(self, pytestconfig):
        """Ensures <li> elements are used semantically."""
        assert pytestconfig.violations.get('listitem') is None, pytestconfig.violations['listitem']['help']

    @pytest.mark.nondestructive
    def test_marquee(self, pytestconfig):
        """Ensures <marquee> elements are not used."""
        assert pytestconfig.violations.get('marquee') is None, pytestconfig.violations['marquee']['help']

    @pytest.mark.nondestructive
    def test_meta_refresh(self, pytestconfig):
        """Ensures <meta http-equiv="refresh"> is not used."""
        assert pytestconfig.violations.get('meta-refresh') is None, pytestconfig.violations['meta-refresh']['help']

    @pytest.mark.nondestructive
    def test_meta_viewport_large(self, pytestconfig):
        """Ensures <meta name="viewport"> can scale a significant amount."""
        assert pytestconfig.violations.get('meta-viewport-large') is None, pytestconfig.violations['meta-viewport-large']['help']

    @pytest.mark.nondestructive
    def test_meta_viewport(self, pytestconfig):
        """Ensures <meta name="viewport"> does not disable text scaling and zooming."""
        assert pytestconfig.violations.get('meta-viewport') is None, pytestconfig.violations['meta-viewport']['help']

    @pytest.mark.nondestructive
    def test_object_alt(self, pytestconfig):
        """Ensures <object> elements have alternate text."""
        assert pytestconfig.violations.get('object-alt') is None, pytestconfig.violations['object-alt']['help']

    @pytest.mark.nondestructive
    def test_p_as_heading(self, pytestconfig):
        """Ensure p elements are not used to style headings."""
        assert pytestconfig.violations.get('p-as-heading') is None, pytestconfig.violations['p-as-heading']['help']

    @pytest.mark.nondestructive
    def test_radiogroup(self, pytestconfig):
        """Ensures related <input type="radio"> elements have a group and that the group designation is consistent."""
        assert pytestconfig.violations.get('radiogroup') is None, pytestconfig.violations['radiogroup']['help']

    @pytest.mark.nondestructive
    def test_region(self, pytestconfig):
        """Ensures all content is contained within a landmark region."""
        assert pytestconfig.violations.get('region') is None, pytestconfig.violations['region']['help']

    @pytest.mark.nondestructive
    def test_scope_attr_valid(self, pytestconfig):
        """Ensures the scope attribute is used correctly on tables."""
        assert pytestconfig.violations.get('scope-attr-valid') is None, pytestconfig.violations['scope-attr-valid']['help']

    @pytest.mark.nondestructive
    def test_server_side_image_map(self, pytestconfig):
        """Ensures that server-side image maps are not used."""
        assert pytestconfig.violations.get('server-side-image-map') is None, pytestconfig.violations['server-side-image-map']['help']

    @pytest.mark.nondestructive
    def test_skip_link(self, pytestconfig):
        """Ensures the first link on the page is a skip link."""
        assert pytestconfig.violations.get('skip-link') is None, pytestconfig.violations['skip-link']['help']

    @pytest.mark.nondestructive
    def test_tabindex(self, pytestconfig):
        """Ensures tabindex attribute values are not greater than 0."""
        assert pytestconfig.violations.get('tabindex') is None, pytestconfig.violations['tabindex']['help']

    @pytest.mark.nondestructive
    def test_table_duplicate_name(self, pytestconfig):
        """Ensure that tables do not have the same summary and caption."""
        assert pytestconfig.violations.get('table-duplicate-name') is None, pytestconfig.violations['table-duplicate-name']['help']

    @pytest.mark.nondestructive
    def test_table_fake_caption(self, pytestconfig):
        """Ensure that tables with a caption use the <caption> element.."""
        assert pytestconfig.violations.get('table-fake-caption') is None, pytestconfig.violations['table-fake-caption']['help']

    @pytest.mark.nondestructive
    def test_td_has_header(self, pytestconfig):
        """Ensure that each non-empty data cell in a large table has one or more table headers."""
        assert pytestconfig.violations.get('td-has-header') is None, pytestconfig.violations['td-has-header']['help']

    @pytest.mark.nondestructive
    def test_td_headers_attr(self, pytestconfig):
        """Ensure that each cell in a table using the headers refers to another cell in that table."""
        assert pytestconfig.violations.get('td-headers-attr') is None, pytestconfig.violations['td-headers-attr']['help']

    @pytest.mark.nondestructive
    def test_th_has_data_cells(self, pytestconfig):
        """Ensure that each table header in a data table refers to data cells."""
        assert pytestconfig.violations.get('th-has-data-cells') is None, pytestconfig.violations['th-has-data-cells']['help']

    @pytest.mark.nondestructive
    def test_valid_lang(self, pytestconfig):
        """Ensures lang attributes have valid values."""
        assert pytestconfig.violations.get('valid-lang') is None, pytestconfig.violations['valid-lang']['help']

    @pytest.mark.nondestructive
    def test_video_caption(self, pytestconfig):
        """Ensures <video> elements have captions."""
        assert pytestconfig.violations.get('video-caption') is None, pytestconfig.violations['video-caption']['help']

    @pytest.mark.nondestructive
    def test_video_description(self, pytestconfig):
        """Ensures <video> elements have audio descriptions."""
        assert pytestconfig.violations.get('video-description') is None, pytestconfig.violations['video-description']['help']
