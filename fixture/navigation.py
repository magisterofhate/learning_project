

class Navigation:

    def __init__(self, app):
        self.app = app

    def login(self, user='admin', pwd='secret'):
        self.home_page()
        self.app.wd.find_element_by_name("user").send_keys(user)
        self.app.wd.find_element_by_name("pass").send_keys(pwd)
        self.app.wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        self.app.wd.find_element_by_link_text("Logout").click()
        self.app.helpers.wait_for_element("//input[@value='Login']")

    def int_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        return len(self.app.wd.find_elements_by_xpath("//input[@value='Logout']")) > 0

    def int_login(self, user, pwd):
         if self.is_logged_in():
             if self.is_logged_in_as(user):
                return
             else:
                 self.logout()
         self.login(user, pwd)

    def is_logged_in_as(self, user):
        return self.app.wd.find_elements_by_xpath("//form[@name='logout']/b") == "(" +user+ ")"

    def home_page(self):
        self.app.wd.get("http://10.201.48.35/addressbook/")

    def group_list(self):
        self.app.wd.find_element_by_link_text("groups").click()
