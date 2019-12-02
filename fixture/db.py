import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, pwd):
        self.host = host
        self.name = name
        self.user = user
        self.pwd = pwd
        self.connection = pymysql.connect(host=host, database=name, user=user, password=pwd, autocommit=True)

    def destroy(self):
        self.connection.close()

    def get_group_list_from_db(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name from group_list")
            for row in cursor:
                (g_id, g_name) = row
                group_list.append((Group(id=g_id, name=g_name)))
        finally:
            cursor.close()
        return group_list

    def get_contact_list_from_db(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook")
            for row in cursor:
                (c_id, cf_name, cl_name) = row
                contact_list.append((Contact(id=c_id, f_name=cf_name, l_name=cl_name)))
        finally:
            cursor.close()
        return contact_list
