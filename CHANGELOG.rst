CHANGELOG
^^^^^^^^^^^^^^

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
