

class CreateItems:

    def __init__(self, app):
        self.app = app

    def create_group(self, group):
        wd = self.app.wd
        # new group
        wd.find_element_by_name("new").click()
        # filling new group parameters
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit new group
        wd.find_element_by_name("submit").click()

    def create_contact(self, contact):
        wd = self.app.wd
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
