# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import selenium
import time

class Axe:

    def __init__(self, selenium, script_url):
        self.selenium = selenium
        self.script_url = script_url
        self.inject(selenium, script_url)

    def inject(self, selenium, script_url):
        """
        Recursively inject aXe into all iframes and the top level document.

        :param script_url: location of the axe-core script.
        :type script_url: string
        """
        selenium.execute_script(open(script_url).read())

    def execute(self, selenium):
        command = 'return axe.run().then(function(result){return result;});'
        response = selenium.execute_script(command)
        return response

    # Skip iframes for now!
    # def inject_into_frames(self, script, parents, selenium):
    #     """
    #     Recursively find frames and inject a script into them.
    #
    #     :param script: Script to inject.
    #     :param parents: list of parent elements
    #     :type script: string
    #     :type parents: list of WebElements
    #     """
    #     # Find all iframes within current document or iframe
    #     frames = selenium.find_elements_by_tag_name('iframe')
    #     # For each frame
    #     for frame in frames:
    #         # Switch to top level element (current frame)
    #         selenium.switch_to.default_content
    #
    #         # If parents list exists
    #         if (parents is not None):
    #             # for each parent
    #             for parent in parents:
    #                 # Focus the parent
    #                 selenium.switch_to.frame(parent)
    #                 # (Selenium can't select iframes within iframes)
    #                 # This focuses the innermost frame this iteration
    #
    #         # Focus next frame and inject javascript
    #         selenium.switch_to.frame(frame)
    #         selenium.execute_script(script)
    #
    #         # Make a local copy of parents list
    #         local_parents = list(parents)
    #         # Add current frame as a parent for next iteration
    #         local_parents.append(frame)
    #         # Recurse and search for frames within current frame
    #         self.inject_into_frames(script, local_parents)

    def report(self, violations):
        """
        Return readable report of accessibility violations found.

        :param violations: Dictionary of violations.
        :type violations: dict
        :return report: Readable report of violations.
        :rtype: string
        """
        string = ''
        string += 'Found ' + str(len(violations)) + ' accessibility violations:'
        for index, item in enumerate(violations):
            string += '\n' + str(index + 1) + ') ' + violations[item]['help']
        return string

    def write_results(name, output):
        """
        Write JSON to file with the specified name.

        :param name: Name of file to be written to.
        :param output: JSON object.
        """
