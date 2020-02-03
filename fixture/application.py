# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from fixture.navigation import Navigation
import warnings
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options as ChromeO


class Application:

    def __init__(self, browser="ff", base_url="http://10.201.48.35/addressbook/", username="admin", password="secret"):
        self.browser = browser
        self.wd = None
        self.select = None
        self.navigation = None
        self.base_url = base_url
        self.username = username
        self.password = password

    def initialize(self):
        if self.browser == "ff":
            options = Options()
            options.headless = True
            self.wd = webdriver.Firefox(options=options)
        elif self.browser == "chrome":
            options = ChromeO()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-gpu')
            self.wd = webdriver.Chrome(options=options)
            # self.wd = webdriver.Chrome()
        elif self.browser == "ie":
            self.wd = webdriver.Ie()
        else:
            warnings.warn("Unrecognized browser %s. Used default" % self.browser, Warning)
            self.wd = webdriver.Firefox()
        self.navigation = Navigation(self)
        self.select = webdriver.support.ui.Select
        self.wd.implicitly_wait(2)
        self.navigation.int_login(self.username, self.password)

    def destroy(self):
        self.wd.quit()

    def is_session_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

