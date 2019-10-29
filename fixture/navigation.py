

class Navigation:

    def __init__(self, app):
        self.app = app

    def home_page(self):
        self.app.wd.get("http://10.201.48.35/addressbookv4.1.4/")

    def group_list(self):
        self.app.wd.find_element_by_link_text("groups").click()
