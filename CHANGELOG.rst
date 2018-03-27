CHANGELOG
^^^^^^^^^^^^^^

version 2.0.0
**************
- All functionalities that are not part of axe-core have been moved into a separate package, ``pytest-axe``. This includes:
  - ``run_axe`` helper method
  - ``get_rules`` Axe class method
  - ``run`` Axe class method
  - ``impact_included`` Axe class method
  - ``analyze`` Axe class method.
  
The purpose of this change is to separate implementations that are specific to the Mozilla Firefox Test Engineering team, and leave the base ``axe-selenium-python`` package for a more broad use case. This package was modeled off of Deque's Java package, axe-selenium-java, and will now more closely mirror it.

All functionalities can still be utilized when using ``axe-selenium-python`` in conjunction with ``pytest-axe``.

version 1.2.3
**************
- Added the analyze method to the Axe class. This method runs accessibility checks, and writes the JSON results to file based on the page URL and the timestamp.
- Writing results to file can be enabled by setting the environment variable ``ACCESSIBILITY_REPORTING=true``. The files will be written to ``results/`` directory, which must be created if it does not already exist.
- Accessibility checks can be disabled by setting the environment variable ``ACCESSIBILITY_DISABLED=true``.

version 1.2.1
**************
- Updated axe.min.js to ``axe-core@2.6.1``
- Modified impact_included class method to reflect changes to the aXe API:
- There are now only 3 impact levels: 'critical', 'serious', and 'minor'

version 1.0.0
**************
- Updated usage examples in README
- Added docstrings to methods lacking documentation
- Removed unused files

version 0.0.3
**************
- Added run method to Axe class to simplify the usage in existing test suites
- run method includes the ability to set what impact level to test for: 'minor', 'moderate', 'severe', 'critical'

version 0.0.276
****************
- Added pytest-axe usage example to README

version 0.0.275
****************
- Added usage example to README

version 0.0.273
****************
- Added selenium instance as a class attribute
- Changed file paths to OS independent structure
- Fixed file read operations to use with keyword


version 0.0.21
***************
- Fixed include of aXe API file and references to it
- Updated README
