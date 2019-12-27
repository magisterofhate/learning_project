# -*- coding: utf-8 -*-
import allure
from fixture.common import clear_data, generate_contact, clean_db_contacts, generate_group, \
    pick_rnd_contact_id_from_db, pick_rnd_group_id_from_db, pick_rnd_group_with_users
from fixture.contact_operations import ContactOps
from fixture.group_operations import GroupOps


def test_add_contact(app, db, check_ui, test_data_contacts):
    contact = test_data_contacts
    co = ContactOps(app)
    app.navigation.home_page()
    with allure.step('Get old contact list'):
        old_contact_list = db.get_contact_list_from_db()
    test_contact = contact
    with allure.step('Create contact %s' % test_contact):
        co.create_contact(test_contact)
    app.navigation.home_page()
    old_contact_list.append(test_contact)
    with allure.step('Get new contact list'):
        new_contact_list = db.get_contact_list_from_db()
    with allure.step('Verify that new contact is on the list'):
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
    if len(db.get_all_contact_ids()) == 0:
        co.create_contact(generate_contact())
    if len(db.get_all_group_ids()) == 0:
        app.navigation.group_list()
        go.create_group(generate_group())
        app.navigation.home_page()
    app.navigation.home_page()
    group_id_to_add_to = pick_rnd_group_id_from_db(db)
    user_id_to_add = pick_rnd_contact_id_from_db(db)
    co.helpers.click_rnd_el(user_id_to_add)
    co.add_contact_to_group(group_id_to_add_to)
    contacts_in_group = db.get_contact_ids_of_group(group_id_to_add_to)
    assert user_id_to_add in contacts_in_group


def test_remove_contact_from_group(app, db):
    co = ContactOps(app)
    go = GroupOps(app)
    if len(db.get_group_ids_with_users()) == 0:
        if len(db.get_all_contact_ids()) != 0 and len(db.get_all_group_ids()) == 0:
            app.navigation.group_list()
            go.create_group(generate_group())
            co.add_rnd_contact_to_rnd_group(db)
        elif len(db.get_all_contact_ids()) == 0 and len(db.get_all_group_ids()) != 0:
            co.create_contact(generate_contact())
            app.navigation.home_page()
            co.add_rnd_contact_to_rnd_group(db)
        else:
            co.add_rnd_contact_to_rnd_group(db)
    app.navigation.home_page()
    group_id = pick_rnd_group_with_users(db)
    app.navigation.go_to_group(group_id)
    user_to_delete = co.helpers.choose_rnd_el()
    co.helpers.click_rnd_el(user_to_delete)
    co.remove_contact_from_group()
    users_in_group_list = db.get_contact_ids_of_group(group_id)
    assert user_to_delete not in users_in_group_list




