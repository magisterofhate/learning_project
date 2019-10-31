from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Navigation:

    def __init__(self, app):
        self.app = app

    def login(self):
        self.app.wd.find_element_by_name("user").send_keys('admin')
        self.app.wd.find_element_by_name("pass").send_keys('secret')
        self.app.wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        self.app.wd.find_element_by_link_text("Logout").click()
        wait = WebDriverWait(self.app.wd, 10)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@value='Login']")))

    def home_page(self):
        self.app.wd.get("http://10.201.48.35/addressbook/")

    def group_list(self):
        self.app.wd.find_element_by_link_text("groups").click()
