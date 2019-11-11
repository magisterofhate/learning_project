# -*- coding: utf-8 -*-


# def test_add_contact(app):
#     app.navigation.home_page()
#     old_contact_list = app.co.get_contact_list()
#     new_id = app.helpers.eval_max_id(old_contact_list)
#     test_contact = app.co.generate_contact(new_id, True)
#     app.co.create_contact(test_contact)
#     app.navigation.home_page()
#     old_contact_list.append(test_contact)
#     new_contact_list = app.co.get_contact_list()
#     assert len(new_contact_list) == len(old_contact_list)
#     assert sorted(new_contact_list) == sorted(old_contact_list)
# #

def test_modify_contact(app):
    app.navigation.home_page()
    if app.helpers.check_elements_presented() is False:
        new_contact = app.co.generate_contact(True)
        app.co.create_contact(new_contact)
    app.navigation.home_page()
    old_contact_list = app.co.get_contact_list()
    usr_id = app.co.choose_rnd_user_for_edit()
    app.co.click_rnd_user_for_edit(usr_id)
    mod_contact = app.co.generate_contact(usr_id, True)
    app.co.modify_contact(mod_contact)
    app.navigation.home_page()
    new_contact_list = app.co.get_contact_list()
    assert len(new_contact_list) == len(old_contact_list)
    assert mod_contact in new_contact_list
#
#
# def test_delete_contact_from_edit_form(app):
#     app.navigation.home_page()
#     if app.helpers.check_elements_presented() is False:
#         app.co.create_contact(
#             Contact(f_name="First_Name", l_name="Last_Name", m_phone="+7888996755", day_dob="22", month_dob="September",
#                     year_dob="1987"))
#     app.navigation.home_page()
#     app.co.choose_rnd_user_for_edit()
#     app.co.delete_contact()
#     app.navigation.home_page()
#
#
# def test_delete_contact_from_the_list(app):
#     app.navigation.home_page()
#     if app.helpers.check_elements_presented() is False:
#         app.co.create_contact(
#             Contact(f_name="First_Name", l_name="Last_Name", m_phone="+7888996755", day_dob="22", month_dob="September",
#                     year_dob="1987"))
#     app.navigation.home_page()
#     app.helpers.click_rnd_el(app.helpers.choose_rnd_el())
#     app.co.delete_contact()
#     app.helpers.confirm_on_popup()
