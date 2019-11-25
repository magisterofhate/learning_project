from model.group import Group
from fixture.helpers import Helpers as helpers


class GroupOps:

    def __init__(self, app):
        self.app = app
        self.helpers = helpers(self.app)

    group_cache = None

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
        self.group_cache = None

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
        self.group_cache = None

    def delete_group(self):
        wd = self.app.wd
        # Submit deletion
        wd.find_element_by_name("delete").click()
        self.group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.app.navigation.group_list()
            g_list = wd.find_elements_by_xpath("//span[@class='group']")
            self.group_cache = []
            for each in g_list:
                g_id = int(each.find_element_by_xpath(".//input[@name='selected[]']").get_attribute("value"))
                g_name = each.text
                self.group_cache.append(Group(id=g_id, name=g_name))
        return list(self.group_cache)

    def find_gr_by_id(self, g_id):
        wd = self.app.wd
        self.app.navigation.group_list()
        gr_name = wd.find_element_by_xpath("//span[.//input[contains(@value," + str(g_id) + ")]]").text
        return Group(id=g_id, name=gr_name)

    def groups_presented(self):
        return self.helpers.check_elements_presented()

    def choose_rnd_group(self):
        gr_id = self.helpers.choose_rnd_el()
        self.helpers.click_rnd_el(gr_id)
        return gr_id
