# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from fixture.navigation import Navigation
from fixture.helpers import Helpers
from fixture.contact_operations import ContactOps
from fixture.group_operations import GroupOps


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.select = webdriver.support.ui.Select
        self.wd.implicitly_wait(2)
        self.navigation = Navigation(self)
        self.helpers = Helpers(self)
        self.go = GroupOps(self)
        self.co = ContactOps(self)

    def destroy(self):
        self.wd.quit()

