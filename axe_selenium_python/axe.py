# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from os import path
import json

_DEFAULT_SCRIPT = path.join(path.dirname(__file__), 'src', 'axe.min.js')


class Axe(object):

    def __init__(self, selenium, script_url=_DEFAULT_SCRIPT):
        self.script_url = script_url
        self.selenium = selenium

    def inject(self):
        """
        Recursively inject aXe into all iframes and the top level document.

        :param script_url: location of the axe-core script.
        :type script_url: string
        """
        with open(self.script_url) as f:
            self.selenium.execute_script(f.read())

    def execute(self, context=None, options=None):
        """
        Run axe against the current page.

        :param context: which page part(s) to analyze and/or what to exclude.
        :param options: dictionary of aXe options.
        """
        template = 'return axe.run(%s).then(function(result){return result;});'
        args = ''

        # If context parameter is passed, add to args
        if context is not None:
            args += '%r' % context
        # Add comma delimiter only if both parameters are passed
        if context is not None and options is not None:
            args += ','
        # If options parameter is passed, add to args
        if options is not None:
            args += '%s' % options

        command = template % args
        response = self.selenium.execute_script(command)
        return response

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
        for violation in violations:
            string += '\n\n\nRule Violated:\n' + violation['id'] + ' - ' + violation['description'] + \
                '\n\tURL: ' + violation['helpUrl'] + \
                '\n\tImpact Level: ' + violation['impact'] + \
                '\n\tTags:'
            for tag in violation['tags']:
                string += ' ' + tag
            string += '\n\tElements Affected:'
            i = 1
            for node in violation['nodes']:
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

    def write_results(self, name, output):
        """
        Write JSON to file with the specified name.

        :param name: Name of file to be written to.
        :param output: JSON object.
        """
        with open(name, 'w+') as f:
            f.write(json.dumps(output, indent=4))
