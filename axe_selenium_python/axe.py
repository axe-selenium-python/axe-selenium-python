# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import json
import os

_DEFAULT_SCRIPT = os.path.join(os.path.dirname(__file__), 'src', 'axe.min.js')


# style: if the code works for py2 and 3, always inherit from object
class Axe(object):

    # design: it looks like you are passing selenium to the constructor
    # if it stays the same throughout the life of the instance
    # I would set it as an attribute of the class and simplify your
    # methods signatures so you don't have to pass around "selenium"
    # when calling inject() , get_rule() and execute()
    #
    def __init__(self, selenium, script_url=_DEFAULT_SCRIPT):
        self.script_url = script_url
        self.inject(selenium, self.script_url)

    def inject(self, selenium, script_url):
        """
        Recursively inject aXe into all iframes and the top level document.

        :param script_url: location of the axe-core script.
        :type script_url: string
        """
        # python pattern : when you open a file, you are opening
        # a file object on the system. Here you never close it
        # so you are leaking a file descriptor
        #
        # The pattern to use is:
        #
        # with open(script_url) as f:
        #     selenium.execute_script(f.read())
        #
        #
        # the with statement will call f.close()
        selenium.execute_script(open(script_url).read())

    def get_rules(self, selenium):
        """Return array of accessibility rules."""
        response = selenium.execute_script('return axe.getRules();')
        return response

    def execute(self, selenium, context=None, options=None):
        """
        Run axe against the current page.

        :param context: which part of the page to analyze and/or what to exclude.
        :param options: dictionary of aXe options.
        """
        # design: you are building a JS string with small pieces,
        # and it's hard to read and see what's going on.
        #
        # you could use a template here, something like:
        #
        # e.g.:
        #
        # tmpl = 'return axe.run(%s).then(function(result){return result;});'
        #
        # if context is not None:
        #     args = '%r' % context   # %r will add the '' if context is a string
        # if options is not None:
        #     args += ',%s' options
        # command = tmpl % args
        #
        command = 'return axe.run('
        if context is not None:
            command += '\'' + context + '\''
        if context is not None and options is not None:
            command += ','
        if options is not None:
            command += options
        command += ').then(function(result){return result;});'

        response = selenium.execute_script(command)
        return response

    def report(self, violations):
        """
        Return readable report of accessibility violations found.

        :param violations: Dictionary of violations.
        :type violations: dict
        :return report: Readable report of violations.
        :rtype: string
        """
        # design: same remark than in execute().
        # when string templates get complicated with loops,
        # maybe its time to use a template engine
        # like mako or jinja2
        # it may sound overkill but it's much better in the long term
        # and avoids a lot of string manipulation errors
        string = ''
        string += 'Found ' + str(len(violations)) + ' accessibility violations:'
        for rule in violations:
            string += '\n\n\nRule Violated:\n' + rule['id'] + ' - ' + rule['description'] + \
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

    def write_results(self, name, output):
        """
        Write JSON to file with the specified name.

        :param name: Name of file to be written to.
        :param output: JSON object.
        """
        # python: this needs a try...finally block to make sure
        # close is always called.
        #
        # that's what with does, so the right pattern is:
        #
        # with open(name, 'w+') as f:
        #     f.write(json.dumps(output, indent=4))
        #
        file = open(name, 'w+')
        file.write(json.dumps(output, indent=4))
        file.close
