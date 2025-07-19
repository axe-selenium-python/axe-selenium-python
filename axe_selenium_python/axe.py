# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from __future__ import annotations

import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

_DEFAULT_SCRIPT = Path(__file__).parent / "node_modules" / "axe-core" / "axe.min.js"


class Axe:
    def __init__(
        self, selenium_driver, script_url: str | Path = _DEFAULT_SCRIPT
    ) -> None:
        """
        Initialize Axe instance.

        Args:
            selenium_driver: Selenium WebDriver instance
            script_url: Path to axe-core JavaScript file

        Raises:
            FileNotFoundError: If script file doesn't exist
        """
        self.script_url = Path(script_url)
        self.selenium = selenium_driver
        self._is_injected = False

        if not self.script_url.exists():
            msg = f"Axe script not found at: {self.script_url}"
            raise FileNotFoundError(msg)

    def inject(self) -> None:
        """
        Inject axe-core script into the current page and all iframes.

        Raises:
            RuntimeError: If injection fails
        """
        try:
            script_content = self.script_url.read_text(encoding="utf-8")
            self.selenium.execute_script(script_content)
            self._is_injected = True
            logger.info("Axe-core successfully injected into page")
        except Exception as e:
            msg = f"Failed to inject axe-core script: {e}"
            raise RuntimeError(msg) from e

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

        param name: Path to the file to be written to. If no path is passed
                    a new JSON file "results.json" will be created in the
                    current working directory.
        :param data: JSON object.
        """
        if name:
            filepath = Path(name).resolve()
        else:
            filepath = Path.cwd() / "results.json"

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
