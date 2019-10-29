# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from fixture.create_items import CreateItems
from fixture.navigation import Navigation
from fixture.delete_items import DeleteItems


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.select = webdriver.support.ui.Select
        self.wd.implicitly_wait(30)
        self.create_items = CreateItems(self)
        self.navigation = Navigation(self)
        self.delete_items = DeleteItems(self)

    def destroy(self):
        self.wd.quit()
