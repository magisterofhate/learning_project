import random


class ModifyItems:

    def __init__(self, app):
        self.app = app

    def modify_group(self, group):
        # Delete random group from the list
        wd = self.app.wd
        # Gather all elements in the list
        list_groups = self.app.wd.find_elements_by_name("selected[]")
        # Choose rnd group in the list
        del_gr = random.choice(list_groups)
        del_gr.click()
        # Open edit form
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("update").click()
