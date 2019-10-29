# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.navigation.home_page()
    app.create_items.create_contact(Contact(f_name="First_Name", l_name="Last_Name", m_phone="+7888996755", day_dob="22", month_dob="September", year_dob="1987"))
    app.navigation.home_page()
