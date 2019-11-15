# -*- coding: utf-8 -*-


def test_add_contact(app):
    for i in range(1, 11):
        app.navigation.home_page()
        old_contact_list = app.co.get_contact_list()
        new_id = app.helpers.eval_max_id(old_contact_list)
        test_contact = app.co.generate_contact(new_id, True)
        app.co.create_contact(test_contact)
        app.navigation.home_page()
        old_contact_list.append(test_contact)
        new_contact_list = app.co.get_contact_list()
        assert len(new_contact_list) == len(old_contact_list)
        assert sorted(new_contact_list) == sorted(old_contact_list)


def test_modify_contact(app):
    app.navigation.home_page()
    if app.helpers.check_elements_presented() is False:
        new_contact = app.co.generate_contact(True)
        app.co.create_contact(new_contact)
    app.navigation.home_page()
    old_contact_list = app.co.get_contact_list()
    usr_id = app.helpers.choose_rnd_el()
    app.co.click_user_for_edit(usr_id)
    mod_contact = app.co.generate_contact(usr_id, True)
    app.co.modify_contact(mod_contact)
    app.navigation.home_page()
    new_contact_list = app.co.get_contact_list()
    assert len(new_contact_list) == len(old_contact_list)
    assert mod_contact in new_contact_list


def test_delete_contact_from_edit_form(app):
    app.navigation.home_page()
    if app.helpers.check_elements_presented() is False:
        new_contact = app.co.generate_contact(True)
        app.co.create_contact(new_contact)
    app.navigation.home_page()
    old_contact_list = app.co.get_contact_list()
    del_id = app.helpers.choose_rnd_el()
    del_user = app.co.find_usr_by_id(del_id)
    app.co.click_user_for_edit(del_id)
    app.co.delete_contact()
    app.navigation.home_page()
    new_contact_list = app.co.get_contact_list()
    assert len(new_contact_list) == (len(old_contact_list) - 1)
    assert del_user not in new_contact_list


def test_delete_contact_from_the_list(app):
    app.navigation.home_page()
    if app.helpers.check_elements_presented() is False:
        new_contact = app.co.generate_contact(True)
        app.co.create_contact(new_contact)
    app.navigation.home_page()
    old_contact_list = app.co.get_contact_list()
    del_id = app.helpers.choose_rnd_el()
    del_user = app.co.find_usr_by_id(del_id)
    app.helpers.click_rnd_el(del_id)
    app.co.delete_contact()
    app.helpers.confirm_on_popup()
    app.co.wait_for_usr_del()
    new_contact_list = app.co.get_contact_list()
    assert len(new_contact_list) == (len(old_contact_list) - 1)
    assert del_user not in new_contact_list
