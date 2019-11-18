import random
from model.contact import Contact
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import re


class ContactOps:

    def __init__(self, app):
        self.app = app

    contacts_cache = None

    def generate_contact(self, c_id=None, c_type=True):
        if c_type:
            new_f_name = self.app.helpers.rnd_string(7)
            new_l_name = self.app.helpers.rnd_string(12)
            new_m_name = self.app.helpers.rnd_string(4)
            new_id = c_id
            new_addr = self.app.helpers.rnd_big_text_field()
            phone_numbers = []
            e_mails = []
            for i in range(1, 5):
                gen_phone_num = '+7' + str(random.randint(1111111111, 9999999999))
                phone_numbers.append(random.choice([gen_phone_num, ""]))

            for i in range(1, 5):
                gen_e_mail = self.app.helpers.rnd_string(7) + '@' + self.app.helpers.rnd_string(4) + '.' \
                         + self.app.helpers.rnd_string(2)
                e_mails.append(random.choice([gen_e_mail, ""]))
        else:
            new_f_name = 'Andrey'
            new_l_name = 'Romanov'
            new_id = c_id
            new_m_name = 'S'
            new_addr = 'Default City'
            phone_numbers = ['+79874561234', '79874565678']
            e_mails = ['and.romanov@gmail.com']
        return Contact(id=new_id, f_name=new_f_name, l_name=new_l_name, m_name=new_m_name, addr=new_addr,
                       h_phone=phone_numbers[0],
                       m_phone=phone_numbers[1], w_phone=phone_numbers[2], s_phone=phone_numbers[3],
                       e_mail1=e_mails[0], e_mail2=e_mails[1], e_mail3=e_mails[2])

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

