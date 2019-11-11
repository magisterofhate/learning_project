from model.group import Group


class GroupOps:

    def __init__(self, app):
        self.app = app

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

    def delete_group(self):
        wd = self.app.wd
        # Submit deletion
        wd.find_element_by_name("delete").click()

    def get_group_list(self):
        wd = self.app.wd
        # wd.navigation.group_list()
        g_list = wd.find_elements_by_xpath("//span[@class='group']")
        groups = []
        for each in g_list:
            g_id = int(each.find_element_by_xpath(".//input[@name='selected[]']").get_attribute("value"))
            g_name = each.text
            groups.append(Group(id=g_id, name=g_name))
        return groups
