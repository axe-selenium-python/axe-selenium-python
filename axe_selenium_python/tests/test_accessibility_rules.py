# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


import pytest
from axe_selenium_python import Axe


class TestAccessibility:

    @pytest.mark.nondestructive
    def test_run_axe(self, base_url, selenium):
        """Run axe against base_url and verify JSON output."""

        script_url = 'src/axe.min.js'
        global a
        a = Axe(selenium, script_url)
        response = a.execute(selenium)
        # parsed = json.loads(response)

        global test_results
        # convert array to dictionary
        test_results = dict((k['id'], k) for k in response['violations'])

        assert response is not None, response

    @pytest.mark.nondestructive
    def test_report(self):
        report = a.report(test_results)
        assert report is None, report

    @pytest.mark.nondestructive
    def test_accesskeys(self):
        """Ensures every accesskey attribute value is unique."""
        assert test_results.get('accesskeys') is None, test_results['accesskeys']['help']

    @pytest.mark.nondestructive
    def test_area_alt(self):
        """Ensures <area> elements of image maps have alternate text."""
        assert test_results.get('area-alt') is None, test_results['area-alt']['help']

    @pytest.mark.nondestructive
    def test_aria_allowed_attr(self):
        """Ensures ARIA attributes are allowed for an element's role."""
        assert test_results.get('aria-allowed-attr') is None, test_results['aria-allowed-attr']['help']

    @pytest.mark.nondestructive
    def test_aria_required_attr(self):
        """Ensures elements with ARIA roles have all required ARIA attributes."""
        assert test_results.get('aria-required-attr') is None, test_results['aria-required-attr']['help']

    @pytest.mark.nondestructive
    def test_aria_required_children(self):
        """Ensures elements with an ARIA role that require child roles contain them."""
        assert test_results.get('aria-required-children') is None, test_results['aria-required-children']['help']

    @pytest.mark.nondestructive
    def test_aria_required_parent(self):
        """Ensures elements with an ARIA role that require parent roles are contained by them."""
        assert test_results.get('aria-required-parent') is None, test_results['aria-required-parent']['help']

    @pytest.mark.nondestructive
    def test_aria_roles(self):
        """Ensures all elements with a role attribute use a valid value."""
        assert test_results.get('aria-roles') is None, test_results['aria-roles']['help']

    @pytest.mark.nondestructive
    def test_aria_valid_attr_value(self):
        """Ensures all ARIA attributes have valid values."""
        assert test_results.get('aria-valid-attr-value') is None, test_results['aria-valid-attr-value']['help']

    @pytest.mark.nondestructive
    def test_aria_valid_attr(self):
        """Ensures attributes that begin with aria- are valid ARIA attributes."""
        assert test_results.get('aria-valid-attr') is None, test_results['aria-valid-attr']['help']

    @pytest.mark.nondestructive
    def test_audio_caption(self):
        """Ensures <audio> elements have captions."""
        assert test_results.get('audio-caption') is None, test_results['audio-caption']['help']

    @pytest.mark.nondestructive
    def test_blink(self):
        """Ensures <blink> elements are not used."""
        assert test_results.get('blink') is None, test_results['blink']['help']

    @pytest.mark.nondestructive
    def test_button_name(self):
        """Ensures buttons have discernible text."""
        assert test_results.get('button-name') is None, test_results['button-name']['help']

    @pytest.mark.nondestructive
    def test_bypass(self):
        """Ensures each page has at least one mechanism for a user to bypass navigation and jump straight to the content."""
        assert test_results.get('bypass') is None, test_results['bypass']['help']

    @pytest.mark.nondestructive
    def test_checkboxgroup(self):
        """Ensures related <input type="checkbox"> elements have a group and that that group designation is consistent."""
        assert test_results.get('checkboxgroup') is None, test_results['checkboxgroup']['help']

    @pytest.mark.nondestructive
    def test_color_contrast(self):
        """Ensures the contrast between foreground and background colors meets WCAG 2 AA contrast ratio thresholds."""
        assert test_results.get('color-contrast') is None, test_results['color-contrast']['help']

    @pytest.mark.nondestructive
    def test_definition_list(self):
        """Ensures <dl> elements are structured correctly."""
        assert test_results.get('definition-list') is None, test_results['definition-list']['help']

    @pytest.mark.nondestructive
    def test_dlitem(self):
        """Ensures <dt> and <dd> elements are contained by a <dl>."""
        assert test_results.get('dlitem') is None, test_results['dlitem']['help']

    @pytest.mark.nondestructive
    def test_document_title(self):
        """Ensures each HTML document contains a non-empty <title> element."""
        assert test_results.get('document-title') is None, test_results['document-title']['help']

    @pytest.mark.nondestructive
    def test_duplicate_id(self):
        """Ensures every id attribute value is unique."""
        assert test_results.get('duplicate-id') is None, test_results['duplicate-id']['help']

    @pytest.mark.nondestructive
    def test_empty_heading(self):
        """Ensures headings have discernible text."""
        assert test_results.get('empty-heading') is None, test_results['empty-heading']['help']

    @pytest.mark.nondestructive
    def test_frame_title_unique(self):
        """Ensures <iframe> and <frame> elements contain a unique title attribute."""
        assert test_results.get('frame-title-unique') is None, test_results['frame-title-unique']['help']

    @pytest.mark.nondestructive
    def test_frame_title(self):
        """Ensures <iframe> and <frame> elements contain a non-empty title attribute."""
        assert test_results.get('frame-title') is None, test_results['frame-title']['help']

    @pytest.mark.nondestructive
    def test_heading_order(self):
        """Ensures the order of headings is semantically correct."""
        assert test_results.get('heading-order') is None, test_results['heading-order']['help']

    @pytest.mark.nondestructive
    def test_href_no_hash(self):
        """Ensures that href values are valid link references to promote only using anchors as links."""
        assert test_results.get('href-no-hash') is None, test_results['href-no-hash']['help']

    @pytest.mark.nondestructive
    def test_html_has_lang(self):
        """Ensures every HTML document has a lang attribute."""
        assert test_results.get('html-has-lang') is None, test_results['html-has-lang']['help']

    @pytest.mark.nondestructive
    def test_html_lang_valid(self):
        """Ensures the lang attribute of the <html> element has a valid value."""
        assert test_results.get('html-lang-valid') is None, test_results['html-lang-valid']['help']

    @pytest.mark.nondestructive
    def test_image_alt(self):
        """Ensures <img> elements have alternate text or a role of none or presentation."""
        assert test_results.get('image-alt') is None, test_results['image-alt']['help']

    @pytest.mark.nondestructive
    def test_image_redundant_alt(self):
        """Ensure button and link text is not repeated as image alternative."""
        assert test_results.get('image-redundant-alt') is None, test_results['image-redundant-alt']['help']

    @pytest.mark.nondestructive
    def test_input_image_alt(self):
        """Ensures <input type="image"> elements have alternate text."""
        assert test_results.get('input-image-alt') is None, test_results['input-image-alt']['help']

    @pytest.mark.nondestructive
    def test_label_title_only(self):
        """Ensures that every form element is not solely labeled using the title or aria-describedby attributes."""
        assert test_results.get('label-title-only') is None, test_results['label-title-only']['help']

    @pytest.mark.nondestructive
    def test_label(self):
        """Ensures every form element has a label."""
        assert test_results.get('label') is None, test_results['label']['help']

    @pytest.mark.nondestructive
    def test_layout_table(self):
        """Ensures presentational <table> elements do not use <th>, <caption> elements or the summary attribute."""
        assert test_results.get('layout-table') is None, test_results['layout-table']['help']

    @pytest.mark.nondestructive
    def test_link_in_text_block(self):
        """Ensures presentational <table> elements do not use <th>, <caption> elements or the summary attribute."""
        assert test_results.get('link-in-text-block') is None, test_results['link-in-text-block']['help']

    @pytest.mark.nondestructive
    def test_link_name(self):
        """Ensures links have discernible text."""
        assert test_results.get('link-name') is None, test_results['link-name']['help']

    @pytest.mark.nondestructive
    def test_list(self):
        """Ensures that lists are structured correctly."""
        assert test_results.get('list') is None, test_results['list']['help']

    @pytest.mark.nondestructive
    def test_listitem(self):
        """Ensures <li> elements are used semantically."""
        assert test_results.get('listitem') is None, test_results['listitem']['help']

    @pytest.mark.nondestructive
    def test_marquee(self):
        """Ensures <marquee> elements are not used."""
        assert test_results.get('marquee') is None, test_results['marquee']['help']

    @pytest.mark.nondestructive
    def test_meta_refresh(self):
        """Ensures <meta http-equiv="refresh"> is not used."""
        assert test_results.get('meta-refresh') is None, test_results['meta-refresh']['help']

    @pytest.mark.nondestructive
    def test_meta_viewport_large(self):
        """Ensures <meta name="viewport"> can scale a significant amount."""
        assert test_results.get('meta-viewport-large') is None, test_results['meta-viewport-large']['help']

    @pytest.mark.nondestructive
    def test_meta_viewport(self):
        """Ensures <meta name="viewport"> does not disable text scaling and zooming."""
        assert test_results.get('meta-viewport') is None, test_results['meta-viewport']['help']

    @pytest.mark.nondestructive
    def test_object_alt(self):
        """Ensures <object> elements have alternate text."""
        assert test_results.get('object-alt') is None, test_results['object-alt']['help']

    @pytest.mark.nondestructive
    def test_p_as_heading(self):
        """Ensure p elements are not used to style headings."""
        assert test_results.get('p-as-heading') is None, test_results['p-as-heading']['help']

    @pytest.mark.nondestructive
    def test_radiogroup(self):
        """Ensures related <input type="radio"> elements have a group and that the group designation is consistent."""
        assert test_results.get('radiogroup') is None, test_results['radiogroup']['help']

    @pytest.mark.nondestructive
    def test_region(self):
        """Ensures all content is contained within a landmark region."""
        assert test_results.get('region') is None, test_results['region']['help']

    @pytest.mark.nondestructive
    def test_scope_attr_valid(self):
        """Ensures the scope attribute is used correctly on tables."""
        assert test_results.get('scope-attr-valid') is None, test_results['scope-attr-valid']['help']

    @pytest.mark.nondestructive
    def test_server_side_image_map(self):
        """Ensures that server-side image maps are not used."""
        assert test_results.get('server-side-image-map') is None, test_results['server-side-image-map']['help']

    @pytest.mark.nondestructive
    def test_skip_link(self):
        """Ensures the first link on the page is a skip link."""
        assert test_results.get('skip-link') is None, test_results['skip-link']['help']

    @pytest.mark.nondestructive
    def test_tabindex(self):
        """Ensures tabindex attribute values are not greater than 0."""
        assert test_results.get('tabindex') is None, test_results['tabindex']['help']

    @pytest.mark.nondestructive
    def test_table_duplicate_name(self):
        """Ensure that tables do not have the same summary and caption."""
        assert test_results.get('table-duplicate-name') is None, test_results['table-duplicate-name']['help']

    @pytest.mark.nondestructive
    def test_table_fake_caption(self):
        """Ensure that tables with a caption use the <caption> element.."""
        assert test_results.get('table-fake-caption') is None, test_results['table-fake-caption']['help']

    @pytest.mark.nondestructive
    def test_td_has_header(self):
        """Ensure that each non-empty data cell in a large table has one or more table headers."""
        assert test_results.get('td-has-header') is None, test_results['td-has-header']['help']

    @pytest.mark.nondestructive
    def test_td_headers_attr(self):
        """Ensure that each cell in a table using the headers refers to another cell in that table."""
        assert test_results.get('td-headers-attr') is None, test_results['td-headers-attr']['help']

    @pytest.mark.nondestructive
    def test_th_has_data_cells(self):
        """Ensure that each table header in a data table refers to data cells."""
        assert test_results.get('th-has-data-cells') is None, test_results['th-has-data-cells']['help']

    @pytest.mark.nondestructive
    def test_valid_lang(self):
        """Ensures lang attributes have valid values."""
        assert test_results.get('valid-lang') is None, test_results['valid-lang']['help']

    @pytest.mark.nondestructive
    def test_video_caption(self):
        """Ensures <video> elements have captions."""
        assert test_results.get('video-caption') is None, test_results['video-caption']['help']

    @pytest.mark.nondestructive
    def test_video_description(self):
        """Ensures <video> elements have audio descriptions."""
        assert test_results.get('video-description') is None, test_results['video-description']['help']
