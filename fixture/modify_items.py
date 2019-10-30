

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
