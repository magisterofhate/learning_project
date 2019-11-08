import random
import string
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Helpers:

    def __init__(self, app):
        self.app = app

    def choose_rnd_el(self):
        wd = self.app.wd
        # Gather all elements in the list
        list_elements = wd.find_elements_by_name("selected[]")
        # Choose rnd element in the list
        del_el = random.choice(list_elements)
        # Clicking on chosen element
        del_el.click()

    def confirm_on_popup(self):
        wd = self.app.wd
        wd.switch_to.alert.accept()

    def rnd_string(self, length):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(length))

    def wait_for_element(self, path, timeout=10):
        wait = WebDriverWait(self.app.wd, timeout)
        wait.until(ec.visibility_of_element_located((By.XPATH, path)))

    def is_session_valid(self):
        try:
            self.app.wd.current_url
            return True
        except:
            return False

    def check_elements_presented(self):
        wd = self.app.wd
        self.wait_for_element("//body")
        if len(wd.find_elements_by_xpath("//input[@name='selected[]']")) == 0:
            return False
