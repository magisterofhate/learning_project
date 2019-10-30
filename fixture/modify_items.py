

class ModifyItems:

    def __init__(self, app):
        self.app = app

    def modify_group(self, group):
        wd = self.app.wd
        # Open edit form
        wd.find_element_by_name("edit").click()
        # Filling form (Clear two fields and appending footer)
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit form
        wd.find_element_by_name("update").click()

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
        wd.find_element_by_name("update").click()
