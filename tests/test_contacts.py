# -*- coding: utf-8 -*-
from fixture.common import clear_data, generate_contact
from fixture.contact_operations import ContactOps


def test_add_contact(app, test_data_contacts):
    contact = test_data_contacts
    co = ContactOps(app)
    app.navigation.home_page()
    old_contact_list = co.get_contact_list()
    test_contact = contact
    co.create_contact(test_contact)
    app.navigation.home_page()
    old_contact_list.append(test_contact)
    new_contact_list = co.get_contact_list()
    assert len(new_contact_list) == len(old_contact_list)
    assert sorted(new_contact_list) == sorted(old_contact_list)


def test_modify_contact(app):
    co = ContactOps(app)
    app.navigation.home_page()
    if not co.contacts_presented():
        co.create_contact(generate_contact())
    app.navigation.home_page()
    old_contact_list = co.get_contact_list()
    usr_id = co.helpers.choose_rnd_el()
    co.click_user_for_edit(usr_id)
    mod_contact = generate_contact(usr_id)
    co.modify_contact(mod_contact)
    app.navigation.home_page()
    new_contact_list = co.get_contact_list()
    assert len(new_contact_list) == len(old_contact_list)
    assert mod_contact in new_contact_list


def test_delete_contact_from_edit_form(app):
    co = ContactOps(app)
    app.navigation.home_page()
    if not co.contacts_presented():
        co.create_contact(generate_contact())
    app.navigation.home_page()
    old_contact_list = co.get_contact_list()
    del_id = co.helpers.choose_rnd_el()
    del_user = co.find_usr_by_id(del_id)
    co.click_user_for_edit(del_id)
    co.delete_contact()
    app.navigation.home_page()
    new_contact_list = co.get_contact_list()
    assert len(new_contact_list) == (len(old_contact_list) - 1)
    assert del_user not in new_contact_list


def test_delete_contact_from_the_list(app):
    co = ContactOps(app)
    app.navigation.home_page()
    if not co.contacts_presented():
        co.create_contact(generate_contact())
    app.navigation.home_page()
    old_contact_list = co.get_contact_list()
    del_user = co.find_usr_by_id(co.choose_rnd_contact())
    co.delete_contact()
    co.helpers.confirm_on_popup()
    co.wait_for_usr_del()
    new_contact_list = co.get_contact_list()
    assert len(new_contact_list) == (len(old_contact_list) - 1)
    assert del_user not in new_contact_list


def test_all_info_from_main_page_match_info_from_edit_page(app):
    co = ContactOps(app)
    app.navigation.home_page()
    test_id = co.helpers.choose_rnd_el()
    test_contact = co.get_full_contact_info_from_edit_page(test_id)
    main_page_info = co.get_full_contact_info_from_main_page(test_id)
    assert clear_data(test_contact.f_name) == main_page_info[0]
    assert clear_data(test_contact.l_name) == main_page_info[1]
    assert co.clear_addresses(test_contact.addr) == co.clear_addresses(main_page_info[2])
    assert co.get_contact_email_list(test_contact) == main_page_info[3]
    assert co.get_contact_phone_list(test_contact) == main_page_info[4]
