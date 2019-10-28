# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from contact import Contact

class AddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def create_new_contact(self, wd, contact):
        # creation initialization
        wd.find_element_by_link_text("add new").click()
        # form fulfilment
        wd.find_element_by_name("firstname").send_keys(contact.f_name)
        wd.find_element_by_name("lastname").send_keys(contact.l_name)
        wd.find_element_by_name("address").send_keys(contact.addr)
        wd.find_element_by_name("home").send_keys(contact.h_phone)
        wd.find_element_by_name("mobile").send_keys(contact.m_phone)
        wd.find_element_by_name("email").send_keys(contact.e_mail)
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.day_dob)
        # wd.find_element_by_xpath("//div[@id='content']/form/select/option[8]").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.month_dob)
        # wd.find_element_by_xpath("//div[@id='content']/form/select[2]/option[5]").click()
        wd.find_element_by_name("byear").send_keys(contact.year_dob)
        # submitting form
        wd.find_element_by_name("submit").click()

    def open_home_page(self, wd):
        wd.get("http://10.201.48.35/addressbookv4.1.4/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.create_new_contact(wd, Contact(f_name="First_Name", l_name="Last_Name", m_phone="+7888996755", day_dob="15", month_dob="May", year_dob="1987"))
        self.open_home_page(wd)


if __name__ == "__main__":
    unittest.main()
