# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


import pytest
import re
import time
import os
import sys

from axe_selenium_python import Axe


class TestAccessibility:

    @pytest.mark.nondestructive
    def test_execute(self, base_url, selenium):
        """Run axe against base_url and verify JSON output."""

        script_url = 'src/axe.min.js'
        global a
        selenium.get(base_url)
        a = Axe(selenium, script_url)
        response = a.execute(selenium)

        global test_results
        global violations
        test_results = response
        # convert array to dictionary
        violations = dict((k['id'], k) for k in response['violations'])
        # assert response exists
        assert response is not None, response

    @pytest.mark.nondestructive
    def test_write_results(self, base_url):
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
        a.write_results(filename, test_results)
        # check that file exists and is not empty
        assert os.path.exists(filename) and os.path.getsize(filename) > 0, \
            'Output file not found.'

    @pytest.mark.nondestructive
    def test_violations(self):
        """Assert that no violations were found."""
        assert len(violations) == 0, a.report(violations)

    @pytest.mark.nondestructive
    def test_report(self):
        """Test that report exists"""
        report = a.report(violations)
        assert report is not None, report

    @pytest.mark.nondestructive
    def test_accesskeys(self):
        """Ensures every accesskey attribute value is unique."""
        assert violations.get('accesskeys') is None, violations['accesskeys']['help']

    @pytest.mark.nondestructive
    def test_area_alt(self):
        """Ensures <area> elements of image maps have alternate text."""
        assert violations.get('area-alt') is None, violations['area-alt']['help']

    @pytest.mark.nondestructive
    def test_aria_allowed_attr(self):
        """Ensures ARIA attributes are allowed for an element's role."""
        assert violations.get('aria-allowed-attr') is None, violations['aria-allowed-attr']['help']

    @pytest.mark.nondestructive
    def test_aria_required_attr(self):
        """Ensures elements with ARIA roles have all required ARIA attributes."""
        assert violations.get('aria-required-attr') is None, violations['aria-required-attr']['help']

    @pytest.mark.nondestructive
    def test_aria_required_children(self):
        """Ensures elements with an ARIA role that require child roles contain them."""
        assert violations.get('aria-required-children') is None, violations['aria-required-children']['help']

    @pytest.mark.nondestructive
    def test_aria_required_parent(self):
        """Ensures elements with an ARIA role that require parent roles are contained by them."""
        assert violations.get('aria-required-parent') is None, violations['aria-required-parent']['help']

    @pytest.mark.nondestructive
    def test_aria_roles(self):
        """Ensures all elements with a role attribute use a valid value."""
        assert violations.get('aria-roles') is None, violations['aria-roles']['help']

    @pytest.mark.nondestructive
    def test_aria_valid_attr_value(self):
        """Ensures all ARIA attributes have valid values."""
        assert violations.get('aria-valid-attr-value') is None, violations['aria-valid-attr-value']['help']

    @pytest.mark.nondestructive
    def test_aria_valid_attr(self):
        """Ensures attributes that begin with aria- are valid ARIA attributes."""
        assert violations.get('aria-valid-attr') is None, violations['aria-valid-attr']['help']

    @pytest.mark.nondestructive
    def test_audio_caption(self):
        """Ensures <audio> elements have captions."""
        assert violations.get('audio-caption') is None, violations['audio-caption']['help']

    @pytest.mark.nondestructive
    def test_blink(self):
        """Ensures <blink> elements are not used."""
        assert violations.get('blink') is None, violations['blink']['help']

    @pytest.mark.nondestructive
    def test_button_name(self):
        """Ensures buttons have discernible text."""
        assert violations.get('button-name') is None, violations['button-name']['help']

    @pytest.mark.nondestructive
    def test_bypass(self):
        """Ensures each page has at least one mechanism for a user to bypass navigation and jump straight to the content."""
        assert violations.get('bypass') is None, violations['bypass']['help']

    @pytest.mark.nondestructive
    def test_checkboxgroup(self):
        """Ensures related <input type="checkbox"> elements have a group and that that group designation is consistent."""
        assert violations.get('checkboxgroup') is None, violations['checkboxgroup']['help']

    @pytest.mark.nondestructive
    def test_color_contrast(self):
        """Ensures the contrast between foreground and background colors meets WCAG 2 AA contrast ratio thresholds."""
        assert violations.get('color-contrast') is None, violations['color-contrast']['help']

    @pytest.mark.nondestructive
    def test_definition_list(self):
        """Ensures <dl> elements are structured correctly."""
        assert violations.get('definition-list') is None, violations['definition-list']['help']

    @pytest.mark.nondestructive
    def test_dlitem(self):
        """Ensures <dt> and <dd> elements are contained by a <dl>."""
        assert violations.get('dlitem') is None, violations['dlitem']['help']

    @pytest.mark.nondestructive
    def test_document_title(self):
        """Ensures each HTML document contains a non-empty <title> element."""
        assert violations.get('document-title') is None, violations['document-title']['help']

    @pytest.mark.nondestructive
    def test_duplicate_id(self):
        """Ensures every id attribute value is unique."""
        assert violations.get('duplicate-id') is None, violations['duplicate-id']['help']

    @pytest.mark.nondestructive
    def test_empty_heading(self):
        """Ensures headings have discernible text."""
        assert violations.get('empty-heading') is None, violations['empty-heading']['help']

    @pytest.mark.nondestructive
    def test_frame_title_unique(self):
        """Ensures <iframe> and <frame> elements contain a unique title attribute."""
        assert violations.get('frame-title-unique') is None, violations['frame-title-unique']['help']

    @pytest.mark.nondestructive
    def test_frame_title(self):
        """Ensures <iframe> and <frame> elements contain a non-empty title attribute."""
        assert violations.get('frame-title') is None, violations['frame-title']['help']

    @pytest.mark.nondestructive
    def test_heading_order(self):
        """Ensures the order of headings is semantically correct."""
        assert violations.get('heading-order') is None, violations['heading-order']['help']

    @pytest.mark.nondestructive
    def test_href_no_hash(self):
        """Ensures that href values are valid link references to promote only using anchors as links."""
        assert violations.get('href-no-hash') is None, violations['href-no-hash']['help']

    @pytest.mark.nondestructive
    def test_html_has_lang(self):
        """Ensures every HTML document has a lang attribute."""
        assert violations.get('html-has-lang') is None, violations['html-has-lang']['help']

    @pytest.mark.nondestructive
    def test_html_lang_valid(self):
        """Ensures the lang attribute of the <html> element has a valid value."""
        assert violations.get('html-lang-valid') is None, violations['html-lang-valid']['help']

    @pytest.mark.nondestructive
    def test_image_alt(self):
        """Ensures <img> elements have alternate text or a role of none or presentation."""
        assert violations.get('image-alt') is None, violations['image-alt']['help']

    @pytest.mark.nondestructive
    def test_image_redundant_alt(self):
        """Ensure button and link text is not repeated as image alternative."""
        assert violations.get('image-redundant-alt') is None, violations['image-redundant-alt']['help']

    @pytest.mark.nondestructive
    def test_input_image_alt(self):
        """Ensures <input type="image"> elements have alternate text."""
        assert violations.get('input-image-alt') is None, violations['input-image-alt']['help']

    @pytest.mark.nondestructive
    def test_label_title_only(self):
        """Ensures that every form element is not solely labeled using the title or aria-describedby attributes."""
        assert violations.get('label-title-only') is None, violations['label-title-only']['help']

    @pytest.mark.nondestructive
    def test_label(self):
        """Ensures every form element has a label."""
        assert violations.get('label') is None, violations['label']['help']

    @pytest.mark.nondestructive
    def test_layout_table(self):
        """Ensures presentational <table> elements do not use <th>, <caption> elements or the summary attribute."""
        assert violations.get('layout-table') is None, violations['layout-table']['help']

    @pytest.mark.nondestructive
    def test_link_in_text_block(self):
        """Ensures presentational <table> elements do not use <th>, <caption> elements or the summary attribute."""
        assert violations.get('link-in-text-block') is None, violations['link-in-text-block']['help']

    @pytest.mark.nondestructive
    def test_link_name(self):
        """Ensures links have discernible text."""
        assert violations.get('link-name') is None, violations['link-name']['help']

    @pytest.mark.nondestructive
    def test_list(self):
        """Ensures that lists are structured correctly."""
        assert violations.get('list') is None, violations['list']['help']

    @pytest.mark.nondestructive
    def test_listitem(self):
        """Ensures <li> elements are used semantically."""
        assert violations.get('listitem') is None, violations['listitem']['help']

    @pytest.mark.nondestructive
    def test_marquee(self):
        """Ensures <marquee> elements are not used."""
        assert violations.get('marquee') is None, violations['marquee']['help']

    @pytest.mark.nondestructive
    def test_meta_refresh(self):
        """Ensures <meta http-equiv="refresh"> is not used."""
        assert violations.get('meta-refresh') is None, violations['meta-refresh']['help']

    @pytest.mark.nondestructive
    def test_meta_viewport_large(self):
        """Ensures <meta name="viewport"> can scale a significant amount."""
        assert violations.get('meta-viewport-large') is None, violations['meta-viewport-large']['help']

    @pytest.mark.nondestructive
    def test_meta_viewport(self):
        """Ensures <meta name="viewport"> does not disable text scaling and zooming."""
        assert violations.get('meta-viewport') is None, violations['meta-viewport']['help']

    @pytest.mark.nondestructive
    def test_object_alt(self):
        """Ensures <object> elements have alternate text."""
        assert violations.get('object-alt') is None, violations['object-alt']['help']

    @pytest.mark.nondestructive
    def test_p_as_heading(self):
        """Ensure p elements are not used to style headings."""
        assert violations.get('p-as-heading') is None, violations['p-as-heading']['help']

    @pytest.mark.nondestructive
    def test_radiogroup(self):
        """Ensures related <input type="radio"> elements have a group and that the group designation is consistent."""
        assert violations.get('radiogroup') is None, violations['radiogroup']['help']

    @pytest.mark.nondestructive
    def test_region(self):
        """Ensures all content is contained within a landmark region."""
        assert violations.get('region') is None, violations['region']['help']

    @pytest.mark.nondestructive
    def test_scope_attr_valid(self):
        """Ensures the scope attribute is used correctly on tables."""
        assert violations.get('scope-attr-valid') is None, violations['scope-attr-valid']['help']

    @pytest.mark.nondestructive
    def test_server_side_image_map(self):
        """Ensures that server-side image maps are not used."""
        assert violations.get('server-side-image-map') is None, violations['server-side-image-map']['help']

    @pytest.mark.nondestructive
    def test_skip_link(self):
        """Ensures the first link on the page is a skip link."""
        assert violations.get('skip-link') is None, violations['skip-link']['help']

    @pytest.mark.nondestructive
    def test_tabindex(self):
        """Ensures tabindex attribute values are not greater than 0."""
        assert violations.get('tabindex') is None, violations['tabindex']['help']

    @pytest.mark.nondestructive
    def test_table_duplicate_name(self):
        """Ensure that tables do not have the same summary and caption."""
        assert violations.get('table-duplicate-name') is None, violations['table-duplicate-name']['help']

    @pytest.mark.nondestructive
    def test_table_fake_caption(self):
        """Ensure that tables with a caption use the <caption> element.."""
        assert violations.get('table-fake-caption') is None, violations['table-fake-caption']['help']

    @pytest.mark.nondestructive
    def test_td_has_header(self):
        """Ensure that each non-empty data cell in a large table has one or more table headers."""
        assert violations.get('td-has-header') is None, violations['td-has-header']['help']

    @pytest.mark.nondestructive
    def test_td_headers_attr(self):
        """Ensure that each cell in a table using the headers refers to another cell in that table."""
        assert violations.get('td-headers-attr') is None, violations['td-headers-attr']['help']

    @pytest.mark.nondestructive
    def test_th_has_data_cells(self):
        """Ensure that each table header in a data table refers to data cells."""
        assert violations.get('th-has-data-cells') is None, violations['th-has-data-cells']['help']

    @pytest.mark.nondestructive
    def test_valid_lang(self):
        """Ensures lang attributes have valid values."""
        assert violations.get('valid-lang') is None, violations['valid-lang']['help']

    @pytest.mark.nondestructive
    def test_video_caption(self):
        """Ensures <video> elements have captions."""
        assert violations.get('video-caption') is None, violations['video-caption']['help']

    @pytest.mark.nondestructive
    def test_video_description(self):
        """Ensures <video> elements have audio descriptions."""
        assert violations.get('video-description') is None, violations['video-description']['help']
