# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.navigation.home_page()
    app.navigation.login()
    app.create_items.create_contact(Contact(f_name="First_Name", l_name="Last_Name", m_phone="+7888996755", day_dob="22", month_dob="September", year_dob="1987"))
    app.navigation.home_page()
    app.navigation.logout()


def test_modify_contact(app):
    app.navigation.home_page()
    app.navigation.login()
    app.helpers.choose_rnd_user()
    last_name = app.helpers.rnd_string(7)
    app.modify_items.modify_contact(Contact(f_name="AAAAA", l_name=last_name, m_phone="+7886666666"))
    app.navigation.home_page()
    app.helpers.wait_for_element("//table")
    elements = app.wd.find_elements_by_xpath("//tr/td")
    elements_text = []
    for each in elements:
        elements_text.append(each.text)
    assert last_name in elements_text
    app.navigation.logout()


# def test_delete_contact_from_edit_form(app):
#     app.navigation.home_page()
#     app.navigation.login()
#     app.helpers.choose_rnd_user()
#     app.delete_items.delete_contact()
#     app.navigation.home_page()
#     app.navigation.logout()
#
#
# def test_delete_contact_from_the_list(app):
#     app.navigation.home_page()
#     app.navigation.login()
#     app.helpers.choose_rnd_el()
#     app.delete_items.delete_contact()
#     app.helpers.confirm_on_popup()
#     app.navigation.logout()

