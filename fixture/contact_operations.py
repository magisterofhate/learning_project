import random
from model.contact import Contact
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class ContactOps:

    def __init__(self, app):
        self.app = app

    contacts_cache = None

    def generate_contact(self, c_id=None, c_type=True):
        if c_type:
            new_f_name = self.app.helpers.rnd_string(7)
            new_l_name = self.app.helpers.rnd_string(12)
            new_id = c_id
        else:
            new_f_name = 'Andrey'
            new_l_name = 'Romanov'
            new_id = c_id
        return Contact(id=new_id, f_name=new_f_name, l_name=new_l_name)

    def create_contact(self, contact):
        wd = self.app.wd
        select = self.app.select

        # creation initialization
        wd.find_element_by_link_text("add new").click()
        # form fulfilment
        wd.find_element_by_name("firstname").send_keys(contact.f_name)
        wd.find_element_by_name("lastname").send_keys(contact.l_name)
        wd.find_element_by_name("address").send_keys(contact.addr)
        wd.find_element_by_name("home").send_keys(contact.h_phone)
        wd.find_element_by_name("mobile").send_keys(contact.m_phone)
        wd.find_element_by_name("email").send_keys(contact.e_mail)
        select(wd.find_element_by_name("bday")).select_by_visible_text(contact.day_dob)
        select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.month_dob)
        wd.find_element_by_name("byear").send_keys(contact.year_dob)
        # submitting form
        wd.find_element_by_name("submit").click()
        self.contacts_cache = None

    def modify_contact(self, contact):
        wd = self.app.wd
        select = self.app.select

        # Form fulfilment
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.f_name)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.l_name)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.addr)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.h_phone)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.m_phone)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.e_mail)
        select(wd.find_element_by_name("bday")).select_by_visible_text(contact.day_dob)
        select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.month_dob)
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.year_dob)
        # Submitting form
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.contacts_cache = None

    def delete_contact(self):
        wd = self.app.wd
        # Submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contacts_cache = None

    def choose_rnd_user_for_edit(self):
        wd = self.app.wd
        # Gather all elements in the list
        list_users = wd.find_elements_by_name("selected[]")
        # Choose rnd user in the list
        chosen_el = random.choice(list_users)
        rnd_el_id = int(chosen_el.get_attribute("value"))
        return rnd_el_id

    def click_rnd_user_for_edit(self, u_id):
        wd = self.app.wd
        rnd_el = wd.find_element_by_xpath("//a[@href='edit.php?id=" + str(u_id) + "']")
        rnd_el.click()

    def get_contact_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.app.navigation.home_page()
            c_list = wd.find_elements_by_xpath("//tr[@name='entry']")
            self.contacts_cache = []
            for each in c_list:
                c_id = int(each.find_element_by_xpath(".//td/input[@name='selected[]']").get_attribute("id"))
                c_f_name = each.find_element_by_xpath("td[3]").text
                c_l_name = each.find_element_by_xpath("td[2]").text
                self.contacts_cache.append(Contact(id=c_id, f_name=c_f_name, l_name=c_l_name))
        return list(self.contacts_cache)

    def find_usr_by_id(self, u_id):
        wd = self.app.wd
        self.app.navigation.home_page()
        u_f_name = wd.find_element_by_xpath("//tr[.//input[contains(@value," + str(u_id) + ")]]/td[3]").text
        u_l_name = wd.find_element_by_xpath("//tr[.//input[contains(@value," + str(u_id) + ")]]/td[2]").text
        return Contact(id=u_id, l_name=u_l_name, f_name=u_f_name)

    def wait_for_usr_del(self):
        wait = WebDriverWait(self.app.wd, 10)
        wait.until(ec.text_to_be_present_in_element((By.XPATH, "//div[@class='msgbox']"), "Record successful deleted"))
