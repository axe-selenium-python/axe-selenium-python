# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


class Axe:

    def get_contents(script):
        """
        Return contents of the axe.js or axe.min.js script.

        :param script: URL of the axe-core script.
        :type script: string
        :return: contents of script.
        :rtype: string
        """

    def inject(driver, script_url):
        """
        Recursively inject aXe into all iframes and the top level document.

        :param driver: WebDriver instance to inject script into.
        :param script_url: URL of the axe-core script.
        :type driver: WebDriver
        :type script_url: string
        """

    def inject_into_frames(driver, script, parents):
        """
        Recursively find frames and inject a script into them.

        :param driver: WebDriver instance to inject script into.
        :param script: Script to inject.
        :type driver: WebDriver
        :type script: string
        """

    def report(violations):
        """
        ??? Do we want this functionality in our package?

        Return readable report of accessibility violations found.

        :param violations: Dictionary of violations.
        :type violations: dict
        :return report: Readable report of violations.
        :rtype: string
        """

    def write_results(name, output):
        """
        Write JSON to file with the specified name.

        :param name: Name of file to be written to.
        :param output: JSON object.
        """

    class Builder:
        """
        Chainable builder for invoking aXe. Instantiate a new Builder and
        configure testing with the include(), exclude(), and options() methods
        before calling analyze() to run.

        driver (WebDriver)
        script (string): URL of script
        includes (list): list of selectors to include.
        excludes (list): list of selectors to exclude.
        options (dict): Dictionary of aXe configuration options.
        """

        def __init__(driver, script):
            """
            Inject the aXe script into the WebDriver.
            :param driver: An intialized WebDriver.
            :param script: URL of aXe script.
            :type driver: WebDriver
            :type script: string
            """"

        def options(options):
            """
            Set the aXe options.

            :param options: Dictionary of aXe configuration options.
            :type options: dict
            """

        def include(selector):
            """
            Include a selector.

            :param selector: any valid CSS selector.
            :type selector: string
            """

        def exclude(selector):
            """
            Exclude a selector.

            :param selector: any valid CSS selector.
            :type selector: string
            """

        def analyze():
            """
            Run aXe against the page.

            :return results: Dictionary of JSON results.
            :rtype results: dict
            """

        def analyze_element(context):
            """
            Rune aXe against a specific WebElement.

            :param context: Web element to be analyzed.
            :type context: WebElement
            :return results: aXe JSON results
            :rtype: dict
            """
