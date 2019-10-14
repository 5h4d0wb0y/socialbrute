import zipfile
import json
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class Browser:

    def __init__(self):
        pass

    def start(self, headless=False, proxy=None, user_agent=None):
        global driver
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        if proxy:
            proxy = json.loads(proxy)
            manifest_json = """
            {
                "version": "1.0.0",
                "manifest_version": 2,
                "name": "Chrome Proxy",
                "permissions": [
                    "proxy",
                    "tabs",
                    "unlimitedStorage",
                    "storage",
                    "<all_urls>",
                    "webRequest",
                    "webRequestBlocking"
                ],
                "background": {
                    "scripts": ["background.js"]
                },
                "minimum_chrome_version":"22.0.0"
            }
            """

            background_js = """
            var config = {
                    mode: "fixed_servers",
                    rules: {
                      singleProxy: {
                        scheme: "http",
                        host: "%s",
                        port: parseInt(%s)
                      },
                      bypassList: ["localhost"]
                    }
                  };

            chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

            function callbackFn(details) {
                return {
                    authCredentials: {
                        username: "%s",
                        password: "%s"
                    }
                };
            }

            chrome.webRequest.onAuthRequired.addListener(
                        callbackFn,
                        {urls: ["<all_urls>"]},
                        ['blocking']
            );
            """ % (proxy['host'], proxy['port'], proxy['user'], proxy['pass'])
            pluginfile = 'proxy_auth_plugin.zip'
            with zipfile.ZipFile(pluginfile, 'w') as zp:
                zp.writestr("manifest.json", manifest_json)
                zp.writestr("background.js", background_js)
            chrome_options.add_extension(pluginfile)
            chrome_options.add_argument('--proxy-server=%s' % proxy)
            #chrome_options.add_argument('--proxy-server=%s' % hostname + ":" + port)
        if user_agent:
            chrome_options.add_argument('--user-agent=%s' % user_agent)
        chrome_options.add_argument("--lang=en")
        self.driver = Chrome(options=chrome_options)

    def stop(self):
        self.driver.quit()

    def get_driver(self):
        return self.driver

    def wait_until_element_exists(self, by, value):
        sec = 120
        if by == 'xpath':
            elem = WebDriverWait(self.driver, sec).until(EC.presence_of_element_located((By.XPATH, value)))
        elif by == 'id':
            elem = WebDriverWait(self.driver, sec).until(EC.presence_of_element_located((By.ID, value)))
        elif by == 'name':
            elem = WebDriverWait(self.driver, sec).until(EC.presence_of_element_located((By.NAME, value)))
        elif by == 'css':
            elem = WebDriverWait(self.driver, sec).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        return elem

    def select_dropdown_by(self, by, value):
        if by == 'xpath':
            elem = Select(self.driver.find_element_by_xpath(value))
        elif by == 'id':
            elem = Select(self.driver.find_element_by_id(value))
        elif by == 'name':
            elem = Select(self.driver.find_element_by_name(value))
        elif by == 'css':
            elem = Select(self.driver.find_element_by_css_selector(value))
        return elem