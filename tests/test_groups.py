# -*- coding: utf-8 -*-
from fixture.common import generate_group
from fixture.group_operations import GroupOps


def test_add_group(app, test_data_groups):
    group = test_data_groups
    go = GroupOps(app)
    app.navigation.group_list()
    old_group_list = go.get_group_list()
    test_group = group
    go.create_group(test_group)
    app.navigation.group_list()
    old_group_list.append(test_group)
    new_group_list = go.get_group_list()
    assert len(new_group_list) == len(old_group_list)
    assert sorted(new_group_list) == sorted(old_group_list)


def test_del_group(app):
    go = GroupOps(app)
    app.navigation.group_list()
    if not go.groups_presented():
        go.create_group(generate_group())
    app.navigation.group_list()
    old_group_list = go.get_group_list()
    del_group = go.find_gr_by_id(go.choose_rnd_group())
    go.delete_group()
    app.navigation.group_list()
    new_group_list = go.get_group_list()
    assert len(new_group_list) == (len(old_group_list) - 1)
    assert del_group not in new_group_list


def test_mod_group(app):
    go = GroupOps(app)
    app.navigation.group_list()
    if not go.groups_presented():
        go.create_group(generate_group())
    app.navigation.group_list()
    old_group_list = go.get_group_list()
    new_group = generate_group(go.choose_rnd_group())
    go.modify_group(new_group)
    app.navigation.group_list()
    new_group_list = go.get_group_list()
    assert len(new_group_list) == len(old_group_list)
    assert new_group in new_group_list
