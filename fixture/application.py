# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from fixture.create_items import CreateItems
from fixture.navigation import Navigation
from fixture.delete_items import DeleteItems
from fixture.modify_items import ModifyItems
from fixture.helpers import Helpers


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.select = webdriver.support.ui.Select
        self.wd.implicitly_wait(30)
        self.create_items = CreateItems(self)
        self.navigation = Navigation(self)
        self.delete_items = DeleteItems(self)
        self.modify_items = ModifyItems(self)
        self.helpers = Helpers(self)

    def destroy(self):
        self.wd.quit()
