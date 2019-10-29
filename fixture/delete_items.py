import random


class DeleteItems:

    def __init__(self, app):
        self.app = app

    def delete_group(self):
        # Delete random group from the list
        wd = self.app.wd
        list_groups = self.app.wd.find_elements_by_name("selected[]")
        del_gr = random.choice(list_groups)
        print(del_gr.get_attribute('Title'))
        del_gr.click()
        wd.find_element_by_name("delete").click()

