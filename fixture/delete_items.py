import random


class DeleteItems:

    def __init__(self, app):
        self.app = app

    def delete_group(self):
        # Delete random group from the list
        wd = self.app.wd
        # Gather all elements in the list
        list_groups = self.app.wd.find_elements_by_name("selected[]")
        # Choose rnd group in the list
        del_gr = random.choice(list_groups)
        del_gr.click()
        # Submit deletion
        wd.find_element_by_name("delete").click()

