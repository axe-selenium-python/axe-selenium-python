# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import json
import os
from io import open

_DEFAULT_SCRIPT = os.path.join(
    os.path.dirname(__file__), "node_modules", "axe-core", "axe.min.js"
)


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
        with open(self.script_url, "r", encoding="utf8") as f:
            self.selenium.execute_script(f.read())

    def run(self, context=None, options=None):
        """
        Run axe against the current page.

        :param context: which page part(s) to analyze and/or what to exclude.
        :param options: dictionary of aXe options.
        """
        template = (
            "var callback = arguments[arguments.length - 1];"
            + "axe.run(%s).then(results => callback(results))"
        )
        args = ""

        # If context parameter is passed, add to args
        if context is not None:
            args += "%r" % context
        # Add comma delimiter only if both parameters are passed
        if context is not None and options is not None:
            args += ","
        # If options parameter is passed, add to args
        if options is not None:
            args += "%s" % options

        command = template % args
        response = self.selenium.execute_async_script(command)
        return response

    def report(self, violations):
        """
        Return readable report of accessibility violations found.

        :param violations: Dictionary of violations.
        :type violations: dict
        :return report: Readable report of violations.
        :rtype: string
        """
        string = ""
        string += "Found " + str(len(violations)) + " accessibility violations:"
        for violation in violations:
            string += (
                "\n\n\nRule Violated:\n"
                + violation["id"]
                + " - "
                + violation["description"]
                + "\n\tURL: "
                + violation["helpUrl"]
                + "\n\tImpact Level: "
                + violation["impact"]
                + "\n\tTags:"
            )
            for tag in violation["tags"]:
                string += " " + tag
            string += "\n\tElements Affected:"
            i = 1
            for node in violation["nodes"]:
                for target in node["target"]:
                    string += "\n\t" + str(i) + ") Target: " + target
                    i += 1
                for item in node["all"]:
                    string += "\n\t\t" + item["message"]
                for item in node["any"]:
                    string += "\n\t\t" + item["message"]
                for item in node["none"]:
                    string += "\n\t\t" + item["message"]
            string += "\n\n\n"
        return string

    def write_results(self, data, name=None):
        """
        Write JSON to file with the specified name.

        :param name: Path to the file to be written to. If no path is passed
                     a new JSON file "results.json" will be created in the
                     current working directory.
        :param output: JSON object.
        """

        if name:
            filepath = os.path.abspath(name)
        else:
            filepath = os.path.join(os.path.getcwd(), "results.json")

        with open(filepath, "w", encoding="utf8") as f:
            try:
                f.write(unicode(json.dumps(data, indent=4)))
            except NameError:
                f.write(json.dumps(data, indent=4))
