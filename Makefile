.PHONY: all
all: help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

.PHONY: help
help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

.PHONY: clean
clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

.PHONY: clean-build
clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

.PHONY: clean-pyc
clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

.PHONY: clean-test
clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

.PHONY: flake8
flake8: ## check format style with flake8
	flake8 socialbrute tests

.PHONY: test-lint
test-lint: clean-pyc flake8 ## test format style with flake8

autoflake:
	autoflake -ir --remove-all-unused-imports --remove-unused-variables ./socialbrute
	autoflake -ir --remove-all-unused-imports --remove-unused-variables ./tests

autopep8:
	autopep8 -ir --aggressive --max-line-length=120 ./socialbrute
	autopep8 -ir --aggressive --max-line-length=120 ./tests

.PHONY: auto-lint
auto-lint: autoflake autopep8 ## automatically remove all unused imports and variables and conform to the PEP 8 style guide

.PHONY: test
test: ## run tests quickly with the default Python
	python3 setup.py test

.PHONY: test-all
test-all: ## run tests on every Python version with tox
	tox

.PHONY: coverage
coverage: ## check code coverage quickly with the default Python
	coverage run --source socialbrute setup.py test
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

.PHONY: docs
docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/socialbrute.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ socialbrute
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

.PHONY: servedocs
servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

.PHONY: dist
dist: clean ## builds source and wheel package
	python3 setup.py sdist
	python3 setup.py bdist_wheel
	ls -l dist

.PHONY: install
install: clean ## install the package to the active Python's site-packages
	python3 setup.py install
	
VERSION = $(shell cat socialbrute/__init__.py| grep '__version__ = ' | cut -d "'" -f 2)

.PHONY: bump-patch
bump-patch: ## bump the patch version
	bump2version patch
	@echo Bumped to version $(VERSION)

.PHONY: bump-minor
bump-minor: ## bump the minor version
	bump2version minor
	@echo Bumped to version $(VERSION)

.PHONY: bump-major
bump-major: ## bump the major version
	bump2version major
	@echo Bumped to version $(VERSION)

.PHONY: changelog
changelog: ## update changelog to the latest release
	python3 setup.py changelog

.PHONY: release
release: dist ## package and upload a release
	twine upload dist/*
