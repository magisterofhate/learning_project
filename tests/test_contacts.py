# -*- coding: utf-8 -*-
from model.contact import Contact


# def test_add_contact(app):
#     app.navigation.home_page()
#     app.create_items.create_contact(Contact(f_name="First_Name", l_name="Last_Name", m_phone="+7888996755", day_dob="22", month_dob="September", year_dob="1987"))
#     app.navigation.home_page()


def test_modify_contact(app):
    app.navigation.home_page()
    app.helpers.choose_rnd_user()
    app.modify_items.modify_contact(Contact(f_name="AAAAA", l_name="BBBBB", m_phone="+7886666666"))
    app.navigation.home_page()
