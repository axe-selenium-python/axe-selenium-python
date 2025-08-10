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

        Args:
            context: which page part(s) to analyze and/or what to exclude.
            options: dictionary of aXe options.

        Raises:
            RuntimeError: If axe is not injected or analysis fails
        """

        if not self._is_injected:
            msg = "Axe not injected. Call inject() first."
            raise RuntimeError(msg)

        args = []
        if context is not None:
            args.append(json.dumps(context))
        if options is not None:
            if context is None:
                args.append("document")
            args.append(json.dumps(options))

        js_args = ", ".join(args) if args else ""

        command = f"""
        var callback = arguments[arguments.length - 1];
        axe.run({js_args})
            .then(results => callback(results))
            .catch(error => callback({{error: error.message}}));
        """

        try:
            response = self.selenium.execute_async_script(command)

            if "error" in response:
                msg = f"Axe analysis failed: {response['error']}"
                raise RuntimeError(msg)

            return response
        except Exception as e:
            msg = f"Failed to execute axe analysis: {e}"
            raise RuntimeError(msg) from e

    def report(self, violations):
        """
        Return readable report of accessibility violations found.

        Args:
            violations: List of violations from axe results.

        Returns:
            Formatted string report.
        """
        if not violations:
            return "No accessibility violations found!"

        lines = [f"Found {len(violations)} accessibility violations:"]

        for i, violation in enumerate(violations, 1):
            lines.append(f"\n{i}. Rule: {violation['id']} - {violation['description']}")
            lines.append(f"   Impact Level: {violation['impact']}")
            lines.append(f"   Help URL: {violation['helpUrl']}")
            lines.append(f"   Tags: {', '.join(violation['tags'])}")
            lines.append("   Elements Affected:")

            for node_idx, node in enumerate(violation["nodes"], 1):
                lines.extend(
                    f"     {node_idx}) Target: {target}" for target in node["target"]
                )

                for message_list in [
                    node.get("all", []),
                    node.get("any", []),
                    node.get("none", []),
                ]:
                    lines.extend(
                        f"        - {item['message']}"
                        for item in message_list
                        if item.get("message")
                    )

            lines.append("")

        return "\n".join(lines)

    def write_results(self, data, name=None):
        """
        Write JSON to file with the specified name.

        param name: Path to the file to be written to. If no path is passed
                    a new JSON file "results.json" will be created in the
                    current working directory.
        :param data: JSON object.
        """
        filepath = Path(name).resolve() if name else Path.cwd() / "results.json"

        try:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            logger.info("Results saved to: %s", filepath)
        except Exception as e:
            msg = f"Failed to save results to {filepath}: {e}"
            raise OSError(msg) from e
