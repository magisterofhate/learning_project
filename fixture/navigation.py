

class Navigation:

    def __init__(self, app):
        self.app = app

    def login(self):
        self.app.wd.find_element_by_name("user").send_keys('admin')
        self.app.wd.find_element_by_name("pass").send_keys('secret')
        self.app.wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        self.app.wd.find_element_by_link_text("Logout").click()
        self.app.helpers.wait_for_element("//input[@value='Login']")

    def home_page(self):
        self.app.wd.get("http://10.201.48.35/addressbook/")

    def group_list(self):
        self.app.wd.find_element_by_link_text("groups").click()
