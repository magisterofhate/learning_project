

class DeleteItems:

    def __init__(self, app):
        self.app = app

    def delete_group(self):
        wd = self.app.wd
        # Submit deletion
        wd.find_element_by_name("delete").click()

