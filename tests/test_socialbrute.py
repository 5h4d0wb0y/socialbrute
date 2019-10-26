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

    def test_check_aol_user(self):
        """Test Aol."""
        sb = socialbrute.Aol(self.browser)
        sb.set_config('socialbrute_username', 'wordlist.txt', 1)
        assert sb.check_user() == 0

    def test_check_facebook_user(self):
        """Test Facebook."""
        sb = socialbrute.Facebook(self.browser)
        sb.set_config('socialbrute_username', 'wordlist.txt', 1)
        assert sb.check_user() == 0

    def test_check_gmail_user(self):
        """Test GMail."""
        sb = socialbrute.Gmail(self.browser)
        sb.set_config('socialbrute_username', 'wordlist.txt', 1)
        assert sb.check_user() == 0

    def test_check_hotmail_user(self):
        """Test Hotmail."""
        sb = socialbrute.Hotmail(self.browser)
        sb.set_config('socialbrute_username', 'wordlist.txt', 1)
        assert sb.check_user() == 0

    def test_check_instagram_user(self):
        """Test Instagram."""
        sb = socialbrute.Instagram(self.browser)
        sb.set_config('socialbrute_username', 'wordlist.txt', 1)
        assert sb.check_user() == 0

    def test_check_twitter_user(self):
        """Test Twitter."""
        sb = socialbrute.Twitter(self.browser)
        sb.set_config('socialbrute_username', 'wordlist.txt', 1)
        assert sb.check_user() == 0

    def test_check_vk_user(self):
        """Test Vk."""
        sb = socialbrute.Vk(self.browser)
        sb.set_config('socialbrute_username', 'wordlist.txt', 1)
        assert sb.check_user() == 0

    def test_check_yahoo_user(self):
        """Test Yahoo."""
        sb = socialbrute.Yahoo(self.browser)
        sb.set_config('socialbrute_username', 'wordlist.txt', 1)
        assert sb.check_user() == 0

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert 'Show this message and exit.' in help_result.output
