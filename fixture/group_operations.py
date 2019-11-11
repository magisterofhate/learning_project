from model.group import Group


class GroupOps:

    def __init__(self, app):
        self.app = app

    group_cache = None

    def generate_group(self, g_id=None, c_type=True):
        if c_type:
            new_name = self.app.helpers.rnd_string(15)
            new_id = g_id
        else:
            new_name = 'New Custom Group'
            new_id = g_id
        return Group(id=new_id, name=new_name)

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
