# -*- coding: utf-8 -*-
from fixture.common import clear_data, generate_contact, clean_db_contacts, generate_group
from fixture.contact_operations import ContactOps
from fixture.group_operations import GroupOps


def test_add_contact(app, db, check_ui, test_data_contacts):
    contact = test_data_contacts
    co = ContactOps(app)
    app.navigation.home_page()
    old_contact_list = db.get_contact_list_from_db()
    test_contact = contact
    co.create_contact(test_contact)
    app.navigation.home_page()
    old_contact_list.append(test_contact)
    new_contact_list = db.get_contact_list_from_db()
    assert sorted(new_contact_list) == sorted(old_contact_list)
    if check_ui:
        contacts_ui = co.get_contact_list()
        assert sorted(map(clean_db_contacts, new_contact_list)) == sorted(contacts_ui)


def test_modify_contact(app, db, check_ui):
    co = ContactOps(app)
    app.navigation.home_page()
    if not co.contacts_presented():
        co.create_contact(generate_contact())
    app.navigation.home_page()
    usr_id = co.helpers.choose_rnd_el()
    co.click_user_for_edit(usr_id)
    mod_contact = generate_contact(usr_id)
    co.modify_contact(mod_contact)
    app.navigation.home_page()
    new_contact_list = db.get_contact_list_from_db()
    assert mod_contact in new_contact_list
    if check_ui:
        contacts_ui = co.get_contact_list()
        assert sorted(map(clean_db_contacts, new_contact_list)) == sorted(contacts_ui)


def test_delete_contact_from_edit_form(app, db, check_ui):
    co = ContactOps(app)
    app.navigation.home_page()
    if not co.contacts_presented():
        co.create_contact(generate_contact())
    app.navigation.home_page()
    old_contact_list = db.get_contact_list_from_db()
    del_id = co.helpers.choose_rnd_el()
    del_user = co.find_usr_by_id(del_id)
    co.click_user_for_edit(del_id)
    co.delete_contact()
    app.navigation.home_page()
    new_contact_list = db.get_contact_list_from_db()
    assert len(new_contact_list) == (len(old_contact_list) - 1)
    assert del_user not in new_contact_list
    if check_ui:
        contacts_ui = co.get_contact_list()
        assert sorted(map(clean_db_contacts, new_contact_list)) == sorted(contacts_ui)


def test_delete_contact_from_the_list(app, db, check_ui):
    co = ContactOps(app)
    app.navigation.home_page()
    if not co.contacts_presented():
        co.create_contact(generate_contact())
    app.navigation.home_page()
    old_contact_list = db.get_contact_list_from_db()
    del_user = co.find_usr_by_id(co.choose_rnd_contact())
    co.delete_contact()
    co.helpers.confirm_on_popup()
    co.wait_for_usr_del()
    new_contact_list = db.get_contact_list_from_db()
    assert len(new_contact_list) == (len(old_contact_list) - 1)
    assert del_user not in new_contact_list
    if check_ui:
        contacts_ui = co.get_contact_list()
        assert sorted(map(clean_db_contacts, new_contact_list)) == sorted(contacts_ui)


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


def test_full_contact_list_from_main_page(app, db):
    co = ContactOps(app)
    contacts_ui = co.get_full_info_contact_list()
    contacts_db = db.get_full_info_contact_list_from_db()
    reorganized_contacts = []
    for cont in contacts_db:
        reorganized_contacts.append(co.reorganize_contact_full_info(cont))
    assert contacts_ui == reorganized_contacts


def test_add_contact_to_group(app, db):
    co = ContactOps(app)
    go = GroupOps(app)
    app.navigation.home_page()
    if not co.contacts_presented():
        co.create_contact(generate_contact())
    app.navigation.group_list()
    group_id_to_add_to = go.helpers.choose_rnd_el()
    if not go.groups_presented():
        go.create_group(generate_group())
    app.navigation.home_page()
    user_id_to_add = co.helpers.choose_rnd_el()
    co.helpers.click_rnd_el(user_id_to_add)
    co.add_contact_to_group(group_id_to_add_to)
    contacts_in_group = db.get_contact_ids_of_group(group_id_to_add_to)
    assert user_id_to_add in contacts_in_group
