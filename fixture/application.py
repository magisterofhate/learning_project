# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from fixture.navigation import Navigation
from fixture.helpers import Helpers
from fixture.contact_operations import ContactOps
from fixture.group_operations import GroupOps
import warnings


class Application:

    def __init__(self, browser="ff", base_url="http://10.201.48.35/addressbook/"):
        if browser == "ff":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            warnings.warn("Unrecognized browser %s. Used default" % browser, Warning)
            self.wd = webdriver.Firefox()
        self.select = webdriver.support.ui.Select
        self.wd.implicitly_wait(2)
        self.navigation = Navigation(self)
        self.helpers = Helpers(self)
        self.go = GroupOps(self)
        self.co = ContactOps(self)
        self.base_url = base_url

    def destroy(self):
        self.wd.quit()

