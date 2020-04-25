=======
History
=======

**unreleased**
**v1.1.1**

v1.1.0 (2020-04-25)
-------------------

* Removed unused imports and variables and conformed to the pep 8 style guide
* Updated docs
* Added tests for the new modules
* Fixed the wait after the call to the page in the modules
* Added new module for linkedin
* Added new module for github
* Added new module for gitlab
* Added new module for netflix
* Added new module for spotify
* Fixed instagram module
* Fixed twitter module
* Fixed the check_user function of the hotmail module
* Fixed facebook module
* Added wait for page loaded
* Updated travis
* Fixes #7
* Fixed unused variable in run method
* Added new make command to test releases
* Fixed unused variable in cli method
* Updated makefile
* Fixed tag name on bump2version

v1.0.2 (2019-10-27)
-------------------

* Added socialbrute tests for each module
* Check if the browser has been started on travis
* Added release-notes make command to generate history from the latest commits
* Added chromedriver installation and jobs environments on travis
* Fixed the installation of codecov in travis
* Removed unused imports and variables and conformed to the PEP 8 style guide
* Removed setuptools-changelog package, use only bump2version to change history
* Added installation of codecov in travis
* Added develop requirements
* Fixed phony and added other commands in makefile
* Fixed duplicate language in travis configuration

v1.0.1 (2019-10-21)
-------------------

* Added sudo and python language parameters
* Fixed packages inside setup.py
* Added --no-sandbox chrome option argument
* Fixed missing dependency

1.0.0 (2019-10-14)
------------------

* First release on PyPI.
