import random
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from sys import maxsize


class Helpers:

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd

    def choose_rnd_el(self):
        wd = self.wd
        # Gather all elements in the list
        list_elements = wd.find_elements_by_name("selected[]")
        # Choose rnd element in the list
        chosen_el = random.choice(list_elements)
        rnd_el_id = int(chosen_el.get_attribute("value"))
        return rnd_el_id

    def click_rnd_el(self, e_id):
        wd = self.wd
        rnd_el = wd.find_element_by_xpath("//input[@value=" + str(e_id) + "]")
        rnd_el.click()

    def confirm_on_popup(self):
        wd = self.wd
        wd.switch_to.alert.accept()

    def wait_for_element(self, path, timeout=10):
        wd = self.wd
        wait = WebDriverWait(wd, timeout)
        wait.until(ec.visibility_of_element_located((By.XPATH, path)))

    def check_elements_presented(self):
        wd = self.wd
        self.wait_for_element("//body")
        if len(wd.find_elements_by_xpath("//input[@name='selected[]']")) != 0:
            return True

    def find_max_id(self, item_list):
        return sorted(item_list, reverse=True)[0].id

    def eval_max_id(self, item_list):
        if not item_list:
            new_id = maxsize
        else:
            new_id = self.app.helpers.find_max_id(item_list) + 1
        return new_id
