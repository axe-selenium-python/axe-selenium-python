# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


import pytest
import re
import time
import os
import sys
import json

from axe_selenium_python import Axe

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

@pytest.mark.nondestructive
def test_violations(axe, selenium, pytestconfig):
    """Run axe against base_url and assert that no violations were found."""

    response = axe.execute(selenium)

    pytestconfig.test_results = response
    # convert array to dictionary
    pytestconfig.violations = dict((k['id'], k) for k in response['violations'])

    assert len(pytestconfig.violations) == 0, axe.report(pytestconfig.violations)

@pytest.mark.nondestructive
def test_accesskeys(pytestconfig):
    """Ensures every accesskey attribute value is unique."""
    assert 'accesskeys' not in pytestconfig.violations, report(pytestconfig.violations['accesskeys'])

@pytest.mark.nondestructive
def test_area_alt(pytestconfig):
    """Ensures <area> elements of image maps have alternate text."""
    assert 'area-alt' not in pytestconfig.violations, pytestconfig.violations['area-alt']['help']

@pytest.mark.nondestructive
def test_aria_allowed_attr(pytestconfig):
    """Ensures ARIA attributes are allowed for an element's role."""
    assert 'aria-allowed-attr' not in pytestconfig.violations, pytestconfig.violations['aria-allowed-attr']['help']

@pytest.mark.nondestructive
def test_aria_required_attr(pytestconfig):
    """Ensures elements with ARIA roles have all required ARIA attributes."""
    assert 'aria-required-attr' not in pytestconfig.violations, pytestconfig.violations['aria-required-attr']['help']

@pytest.mark.nondestructive
def test_aria_required_children(pytestconfig):
    """Ensures elements with an ARIA role that require child roles contain them."""
    assert 'aria-required-children' not in pytestconfig.violations, pytestconfig.violations['aria-required-children']['help']

@pytest.mark.nondestructive
def test_aria_required_parent(pytestconfig):
    """Ensures elements with an ARIA role that require parent roles are contained by them."""
    assert 'aria-required-parent' not in pytestconfig.violations, pytestconfig.violations['aria-required-parent']['help']

@pytest.mark.nondestructive
def test_aria_roles(pytestconfig):
    """Ensures all elements with a role attribute use a valid value."""
    assert 'aria-roles' not in pytestconfig.violations, pytestconfig.violations['aria-roles']['help']

@pytest.mark.nondestructive
def test_aria_valid_attr_value(pytestconfig):
    """Ensures all ARIA attributes have valid values."""
    assert 'aria-valid-attr-value' not in pytestconfig.violations, pytestconfig.violations['aria-valid-attr-value']['help']

@pytest.mark.nondestructive
def test_aria_valid_attr(pytestconfig):
    """Ensures attributes that begin with aria- are valid ARIA attributes."""
    assert 'aria-valid-attr' not in pytestconfig.violations, pytestconfig.violations['aria-valid-attr']['help']

@pytest.mark.nondestructive
def test_audio_caption(pytestconfig):
    """Ensures <audio> elements have captions."""
    assert 'audio-caption' not in pytestconfig.violations, pytestconfig.violations['audio-caption']['help']

@pytest.mark.nondestructive
def test_blink(pytestconfig):
    """Ensures <blink> elements are not used."""
    assert 'blink' not in pytestconfig.violations, pytestconfig.violations['blink']['help']

@pytest.mark.nondestructive
def test_button_name(pytestconfig):
    """Ensures buttons have discernible text."""
    assert 'button-name' not in pytestconfig.violations, pytestconfig.violations['button-name']['help']

@pytest.mark.nondestructive
def test_bypass(pytestconfig):
    """Ensures each page has at least one mechanism for a user to bypass navigation and jump straight to the content."""
    assert 'bypass' not in pytestconfig.violations, pytestconfig.violations['bypass']['help']

@pytest.mark.nondestructive
def test_checkboxgroup(pytestconfig):
    """Ensures related <input type="checkbox"> elements have a group and that that group designation is consistent."""
    assert 'checkboxgroup' not in pytestconfig.violations, pytestconfig.violations['checkboxgroup']['help']

@pytest.mark.nondestructive
def test_color_contrast(pytestconfig):
    """Ensures the contrast between foreground and background colors meets WCAG 2 AA contrast ratio thresholds."""
    assert 'color-contrast' not in pytestconfig.violations, pytestconfig.violations['color-contrast']['help']

@pytest.mark.nondestructive
def test_definition_list(pytestconfig):
    """Ensures <dl> elements are structured correctly."""
    assert 'definition-list' not in pytestconfig.violations, pytestconfig.violations['definition-list']['help']

@pytest.mark.nondestructive
def test_dlitem(pytestconfig):
    """Ensures <dt> and <dd> elements are contained by a <dl>."""
    assert 'dlitem' not in pytestconfig.violations, pytestconfig.violations['dlitem']['help']

@pytest.mark.nondestructive
def test_document_title(pytestconfig):
    """Ensures each HTML document contains a non-empty <title> element."""
    assert 'document-title' not in pytestconfig.violations, pytestconfig.violations['document-title']['help']

@pytest.mark.nondestructive
def test_duplicate_id(pytestconfig):
    """Ensures every id attribute value is unique."""
    assert 'duplicate-id' not in pytestconfig.violations, pytestconfig.violations['duplicate-id']['help']

@pytest.mark.nondestructive
def test_empty_heading(pytestconfig):
    """Ensures headings have discernible text."""
    assert 'empty-heading' not in pytestconfig.violations, pytestconfig.violations['empty-heading']['help']

@pytest.mark.nondestructive
def test_frame_title_unique(pytestconfig):
    """Ensures <iframe> and <frame> elements contain a unique title attribute."""
    assert 'frame-title-unique' not in pytestconfig.violations, pytestconfig.violations['frame-title-unique']['help']

@pytest.mark.nondestructive
def test_frame_title(pytestconfig):
    """Ensures <iframe> and <frame> elements contain a non-empty title attribute."""
    assert 'frame-title' not in pytestconfig.violations, pytestconfig.violations['frame-title']['help']

@pytest.mark.nondestructive
def test_heading_order(pytestconfig):
    """Ensures the order of headings is semantically correct."""
    assert 'heading-order' not in pytestconfig.violations, pytestconfig.violations['heading-order']['help']

@pytest.mark.nondestructive
def test_href_no_hash(pytestconfig):
    """Ensures that href values are valid link references to promote only using anchors as links."""
    assert 'href-no-hash' not in pytestconfig.violations, pytestconfig.violations['href-no-hash']['help']

@pytest.mark.nondestructive
def test_html_has_lang(pytestconfig):
    """Ensures every HTML document has a lang attribute."""
    assert 'html-has-lang' not in pytestconfig.violations, pytestconfig.violations['html-has-lang']['help']

@pytest.mark.nondestructive
def test_html_lang_valid(pytestconfig):
    """Ensures the lang attribute of the <html> element has a valid value."""
    assert 'html-lang-valid' not in pytestconfig.violations, pytestconfig.violations['html-lang-valid']['help']

@pytest.mark.nondestructive
def test_image_alt(pytestconfig):
    """Ensures <img> elements have alternate text or a role of none or presentation."""
    assert 'image-alt' not in pytestconfig.violations, pytestconfig.violations['image-alt']['help']

@pytest.mark.nondestructive
def test_image_redundant_alt(pytestconfig):
    """Ensure button and link text is not repeated as image alternative."""
    assert 'image-redundant-alt' not in pytestconfig.violations, pytestconfig.violations['image-redundant-alt']['help']

@pytest.mark.nondestructive
def test_input_image_alt(pytestconfig):
    """Ensures <input type="image"> elements have alternate text."""
    assert 'input-image-alt' not in pytestconfig.violations, pytestconfig.violations['input-image-alt']['help']

@pytest.mark.nondestructive
def test_label_title_only(pytestconfig):
    """Ensures that every form element is not solely labeled using the title or aria-describedby attributes."""
    assert 'label-title-only' not in pytestconfig.violations, pytestconfig.violations['label-title-only']['help']

@pytest.mark.nondestructive
def test_label(pytestconfig):
    """Ensures every form element has a label."""
    assert 'label' not in pytestconfig.violations, report(pytestconfig.violations['label'])

@pytest.mark.nondestructive
def test_layout_table(pytestconfig):
    """Ensures presentational <table> elements do not use <th>, <caption> elements or the summary attribute."""
    assert 'layout-table' not in pytestconfig.violations, pytestconfig.violations['layout-table']['help']

@pytest.mark.nondestructive
def test_link_in_text_block(pytestconfig):
    """Ensures presentational <table> elements do not use <th>, <caption> elements or the summary attribute."""
    assert 'link-in-text-block' not in pytestconfig.violations, pytestconfig.violations['link-in-text-block']['help']

@pytest.mark.nondestructive
def test_link_name(pytestconfig):
    """Ensures links have discernible text."""
    assert 'link-name' not in pytestconfig.violations, pytestconfig.violations['link-name']['help']

@pytest.mark.nondestructive
def test_list(pytestconfig):
    """Ensures that lists are structured correctly."""
    assert 'list' not in pytestconfig.violations, pytestconfig.violations['list']['help']

@pytest.mark.nondestructive
def test_listitem(pytestconfig):
    """Ensures <li> elements are used semantically."""
    assert 'listitem' not in pytestconfig.violations, pytestconfig.violations['listitem']['help']

@pytest.mark.nondestructive
def test_marquee(pytestconfig):
    """Ensures <marquee> elements are not used."""
    assert 'marquee' not in pytestconfig.violations, pytestconfig.violations['marquee']['help']

@pytest.mark.nondestructive
def test_meta_refresh(pytestconfig):
    """Ensures <meta http-equiv="refresh"> is not used."""
    assert 'meta-refresh' not in pytestconfig.violations, pytestconfig.violations['meta-refresh']['help']

@pytest.mark.nondestructive
def test_meta_viewport_large(pytestconfig):
    """Ensures <meta name="viewport"> can scale a significant amount."""
    assert 'meta-viewport-large' not in pytestconfig.violations, pytestconfig.violations['meta-viewport-large']['help']

@pytest.mark.nondestructive
def test_meta_viewport(pytestconfig):
    """Ensures <meta name="viewport"> does not disable text scaling and zooming."""
    assert 'meta-viewport' not in pytestconfig.violations, pytestconfig.violations['meta-viewport']['help']

@pytest.mark.nondestructive
def test_object_alt(pytestconfig):
    """Ensures <object> elements have alternate text."""
    assert 'object-alt' not in pytestconfig.violations, pytestconfig.violations['object-alt']['help']

@pytest.mark.nondestructive
def test_p_as_heading(pytestconfig):
    """Ensure p elements are not used to style headings."""
    assert 'p-as-heading' not in pytestconfig.violations, pytestconfig.violations['p-as-heading']['help']

@pytest.mark.nondestructive
def test_radiogroup(pytestconfig):
    """Ensures related <input type="radio"> elements have a group and that the group designation is consistent."""
    assert 'radiogroup' not in pytestconfig.violations, pytestconfig.violations['radiogroup']['help']

@pytest.mark.nondestructive
def test_region(pytestconfig):
    """Ensures all content is contained within a landmark region."""
    assert 'region' not in pytestconfig.violations, pytestconfig.violations['region']['help']

@pytest.mark.nondestructive
def test_scope_attr_valid(pytestconfig):
    """Ensures the scope attribute is used correctly on tables."""
    assert 'scope-attr-valid' not in pytestconfig.violations, pytestconfig.violations['scope-attr-valid']['help']

@pytest.mark.nondestructive
def test_server_side_image_map(pytestconfig):
    """Ensures that server-side image maps are not used."""
    assert 'server-side-image-map' not in pytestconfig.violations, pytestconfig.violations['server-side-image-map']['help']

@pytest.mark.nondestructive
def test_skip_link(pytestconfig):
    """Ensures the first link on the page is a skip link."""
    assert 'skip-link' not in pytestconfig.violations, pytestconfig.violations['skip-link']['help']

@pytest.mark.nondestructive
def test_tabindex(pytestconfig):
    """Ensures tabindex attribute values are not greater than 0."""
    assert 'tabindex' not in pytestconfig.violations, pytestconfig.violations['tabindex']['help']

@pytest.mark.nondestructive
def test_table_duplicate_name(pytestconfig):
    """Ensure that tables do not have the same summary and caption."""
    assert 'table-duplicate-name' not in pytestconfig.violations, pytestconfig.violations['table-duplicate-name']['help']

@pytest.mark.nondestructive
def test_table_fake_caption(pytestconfig):
    """Ensure that tables with a caption use the <caption> element.."""
    assert 'table-fake-caption' not in pytestconfig.violations, pytestconfig.violations['table-fake-caption']['help']

@pytest.mark.nondestructive
def test_td_has_header(pytestconfig):
    """Ensure that each non-empty data cell in a large table has one or more table headers."""
    assert 'td-has-header' not in pytestconfig.violations, pytestconfig.violations['td-has-header']['help']

@pytest.mark.nondestructive
def test_td_headers_attr(pytestconfig):
    """Ensure that each cell in a table using the headers refers to another cell in that table."""
    assert 'td-headers-attr' not in pytestconfig.violations, pytestconfig.violations['td-headers-attr']['help']

@pytest.mark.nondestructive
def test_th_has_data_cells(pytestconfig):
    """Ensure that each table header in a data table refers to data cells."""
    assert 'th-has-data-cells' not in pytestconfig.violations, pytestconfig.violations['th-has-data-cells']['help']

@pytest.mark.nondestructive
def test_valid_lang(pytestconfig):
    """Ensures lang attributes have valid values."""
    assert 'valid-lang' not in pytestconfig.violations, pytestconfig.violations['valid-lang']['help']

@pytest.mark.nondestructive
def test_video_caption(pytestconfig):
    """Ensures <video> elements have captions."""
    assert 'video-caption' not in pytestconfig.violations, pytestconfig.violations['video-caption']['help']

@pytest.mark.nondestructive
def test_video_description(pytestconfig):
    """Ensures <video> elements have audio descriptions."""
    assert 'video-description' not in pytestconfig.violations, pytestconfig.violations['video-description']['help']
