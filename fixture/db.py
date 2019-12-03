import pymysql.cursors
from model.group import Group
from model.contact import Contact
import itertools


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

    def get_full_info_contact_list_from_db(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, "
                           "email3 from addressbook order by lastname")
            for row in cursor:
                (c_id, cf_name, cl_name, cl_addr, cl_home, cl_mobile, cl_work, cl_sphone,
                 cl_email, cl_email2, cl_email3) = row
                contact_list.append((Contact(id=c_id, f_name=cf_name, l_name=cl_name, addr=cl_addr, h_phone=cl_home,
                                             m_phone=cl_mobile, w_phone=cl_work, s_phone=cl_sphone,
                                             e_mail1=cl_email, e_mail2=cl_email2, e_mail3=cl_email3)))
        finally:
            cursor.close()
        return contact_list

    def get_contact_ids_of_group(self, gr_id):
        converter = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id from address_in_groups where group_id = %s" % gr_id)
            for row in cursor:
                (c_id) = row
                converter.append(c_id)
        finally:
            cursor.close()
        contacts_list = list(itertools.chain(*converter))
        return contacts_list

    def get_all_contact_ids(self):
        converter = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id from addressbook")
            for row in cursor:
                (c_id) = row
                converter.append(c_id)
        finally:
            cursor.close()
        id_list = list(itertools.chain(*converter))
        return id_list

    def get_all_group_ids(self):
        converter = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id from group_list")
            for row in cursor:
                (g_id) = row
                converter.append(g_id)
        finally:
            cursor.close()
        id_list = list(itertools.chain(*converter))
        return id_list

    def get_group_ids_with_users(self):
        converter = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id FROM `address_in_groups` as ag "
                           "join addressbook as a ON "
                           "a.id = ag.id")
            for row in cursor:
                (g_id) = row
                converter.append(g_id)
        finally:
            cursor.close()
        id_list = list(itertools.chain(*converter))
        return id_list
