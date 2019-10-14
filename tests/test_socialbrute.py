#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `socialbrute` package."""


import unittest
from click.testing import CliRunner

from socialbrute import socialbrute
from socialbrute import browser
from socialbrute import cli


class TestSocialbrute(unittest.TestCase):
    """Tests for `socialbrute` package."""

    def setUp(self):
        """Start browser."""
        self.browser = browser.Browser()
        self.browser.start(headless=False)

    def tearDown(self):
        """Stop browser."""
        self.browser.stop()

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help                          Show this message and exit.' in help_result.output
