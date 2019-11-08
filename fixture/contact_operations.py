

class ContactOps:

    def __init__(self, app):
        self.app = app

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

    def delete_contact(self):
        wd = self.app.wd
        # Submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
