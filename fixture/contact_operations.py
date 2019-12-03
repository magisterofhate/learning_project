from model.contact import Contact
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import re
from fixture.helpers import Helpers as helpers
from fixture.common import clear_data, pick_rnd_contact_id_from_db, pick_rnd_group_id_from_db


class ContactOps:

    def __init__(self, app):
        self.app = app
        self.helpers = helpers(self.app)

    contacts_cache = None
    contacts_full_cache = None

    def create_contact(self, contact):
        wd = self.app.wd
        select = self.app.select

        # creation initialization
        wd.find_element_by_link_text("add new").click()
        # form fulfilment
        wd.find_element_by_name("firstname").send_keys(contact.f_name)
        wd.find_element_by_name("lastname").send_keys(contact.l_name)
        wd.find_element_by_name("middlename").send_keys(contact.m_name)
        wd.find_element_by_name("address").send_keys(contact.addr)
        wd.find_element_by_name("home").send_keys(contact.h_phone)
        wd.find_element_by_name("mobile").send_keys(contact.m_phone)
        wd.find_element_by_name("work").send_keys(contact.w_phone)
        wd.find_element_by_name("phone2").send_keys(contact.s_phone)
        wd.find_element_by_name("email").send_keys(contact.e_mail1)
        wd.find_element_by_name("email2").send_keys(contact.e_mail2)
        wd.find_element_by_name("email3").send_keys(contact.e_mail3)
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
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.m_name)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.addr)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.h_phone)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.m_phone)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.w_phone)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.s_phone)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.e_mail1)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.e_mail2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.e_mail3)
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

    def click_user_for_edit(self, u_id):
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

    def get_full_contact_info_from_edit_page(self, c_id):
        wd = self.app.wd
        self.app.navigation.home_page()
        self.click_user_for_edit(c_id)
        id = wd.find_element_by_name("id").get_attribute("value")
        fname = wd.find_element_by_name("firstname").get_attribute("value")
        lname = wd.find_element_by_name("lastname").get_attribute("value")
        mname = wd.find_element_by_name("middlename").get_attribute("value")
        addr = wd.find_element_by_name("address").get_attribute("value")
        hphone = wd.find_element_by_name("home").get_attribute("value")
        mphone = wd.find_element_by_name("mobile").get_attribute("value")
        wphone = wd.find_element_by_name("work").get_attribute("value")
        sphone = wd.find_element_by_name("phone2").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(id=id, f_name=fname, l_name=lname, m_name=mname, addr=addr, h_phone=hphone, m_phone=mphone,
                       w_phone=wphone, s_phone=sphone, e_mail1=email1, e_mail2=email2, e_mail3=email3)

    def get_full_contact_info_from_main_page(self, c_id):
        wd = self.app.wd
        self.app.navigation.home_page()
        fname = wd.find_element_by_xpath("//tr[.//input[contains(@value," + str(c_id) + ")]]/td[3]").text
        lname = wd.find_element_by_xpath("//tr[.//input[contains(@value," + str(c_id) + ")]]/td[2]").text
        addr = wd.find_element_by_xpath("//tr[.//input[contains(@value," + str(c_id) + ")]]/td[4]").text
        e_mails = wd.find_element_by_xpath("//tr[.//input[contains(@value," + str(c_id) + ")]]/td[5]").text
        phones = wd.find_element_by_xpath("//tr[.//input[contains(@value," + str(c_id) + ")]]/td[6]").text
        info = [fname, lname, addr, e_mails, phones]
        return info

    def clear_addresses(self, s):
        return re.sub("\n", "", s)

    def clear_phones(self, s):
        return re.sub("[() -]", "", s)

    def get_contact_email_list(self, contact):
        return '\n'.join(filter(lambda x: x != '',
                                filter(lambda x: x is not None, [contact.e_mail1, contact.e_mail2, contact.e_mail3])))

    def get_contact_phone_list(self, contact):
        return '\n'.join(filter(lambda x: x != '',
                                map(lambda x: self.clear_phones(x),
                                    filter(lambda x: x is not None,
                                           [contact.h_phone, contact.m_phone, contact.w_phone, contact.s_phone]))))

    def contacts_presented(self):
        return self.helpers.check_elements_presented()

    def choose_rnd_contact(self):
        co_id = self.helpers.choose_rnd_el()
        self.helpers.click_rnd_el(co_id)
        return co_id

    def get_full_info_contact_list(self):
        if self.contacts_full_cache is None:
            wd = self.app.wd
            self.app.navigation.home_page()
            c_list = wd.find_elements_by_xpath("//tr[@name='entry']")
            self.contacts_full_cache = []
            for each in c_list:
                c_id = int(each.find_element_by_xpath(".//td/input[@name='selected[]']").get_attribute("id"))
                c_f_name = each.find_element_by_xpath("td[3]").text
                c_l_name = each.find_element_by_xpath("td[2]").text
                addr = self.clear_addresses(each.find_element_by_xpath("td[4]").text)
                e_mails = each.find_element_by_xpath("td[5]").text
                phones = each.find_element_by_xpath("td[6]").text
                info = {'id': c_id, 'f_name': c_f_name, 'l_name': c_l_name, 'addr': addr,
                        'e_mails': e_mails, 'phones': phones}
                self.contacts_full_cache.append(info)
        return list(self.contacts_full_cache)

    def reorganize_contact_full_info(self, contact):
        cont_phones = self.get_contact_phone_list(contact)
        cont_emails = self.get_contact_email_list(contact)
        cont_dict = {'id': contact.id, 'f_name': clear_data(contact.f_name), 'l_name': clear_data(contact.l_name),
                     'addr': clear_data(self.clear_addresses(re.sub("\r", "\n", contact.addr))),
                     'e_mails': cont_emails, 'phones': cont_phones}
        return cont_dict

    def add_contact_to_group(self, group_id):
        wd = self.app.wd
        select = self.app.select
        dropdown = select(wd.find_element_by_xpath("//select[@name='to_group']"))
        gr_id = group_id
        dropdown.select_by_value(str(gr_id))
        wd.find_element_by_xpath("//input[@value='Add to']").click()

    def add_rnd_contact_to_rnd_group(self, database):
        wd = self.app.wd
        select = self.app.select
        self.app.navigation.home_page()
        group_id_to_add_to = pick_rnd_group_id_from_db(database)
        user_id_to_add = pick_rnd_contact_id_from_db(database)
        self.helpers.click_rnd_el(user_id_to_add)
        dropdown = select(wd.find_element_by_xpath("//select[@name='to_group']"))
        dropdown.select_by_value(str(group_id_to_add_to))
        wd.find_element_by_xpath("//input[@value='Add to']").click()
        return {'g_id': group_id_to_add_to, 'u_id': user_id_to_add}

    def remove_contact_from_group(self):
        wd = self.app.wd
        # Submit deletion
        wd.find_element_by_xpath("//input[@name='remove']").click()



