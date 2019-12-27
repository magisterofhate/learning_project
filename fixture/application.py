# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from fixture.navigation import Navigation
import warnings


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
            self.wd = webdriver.Firefox()
        elif self.browser == "chrome":
            self.wd = webdriver.Chrome()
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

