import random


class Helpers:

    def __init__(self, app):
        self.app = app

    def choose_rnd_el(self):
        wd = self.app.wd
        # Gather all elements in the list
        list_elements = wd.find_elements_by_name("selected[]")
        # Choose rnd group in the list
        del_el = random.choice(list_elements)
        # Clicking on chosen element
        del_el.click()

    def choose_rnd_user(self):
        wd = self.app.wd
        # Gather all elements in the list
        list_users = wd.find_elements_by_xpath("//a[.//img[contains(@title, 'Edit')]]")
        # Choose rnd user in the list
        ed_usr = random.choice(list_users)
        # debugging feature print(ed_usr.get_attribute('href'))
        # Clicking on chosen element
        ed_usr.click()
