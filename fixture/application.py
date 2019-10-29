# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from fixture.create_items import CreateItems


class Application:

    def __init__(self):
        self.wd = webdriver()
        self.wd.implicitly_wait(30)
        self.create_items = CreateItems(self)

    def open_group_list(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://10.201.48.35/addressbookv4.1.4/")

    def destroy(self):
        self.wd.quit()