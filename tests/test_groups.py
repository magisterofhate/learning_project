# -*- coding: utf-8 -*-
import pytest
from sys import maxsize
from fixture.application import Application

q = Application()

test_data = [
    q.go.generate_group(maxsize, True)
    for i in range(5)
]

q.destroy()


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, group):
    app.navigation.group_list()
    old_group_list = app.go.get_group_list()
    # new_id = app.helpers.eval_max_id(old_group_list)
    # test_group = app.go.generate_group(new_id, True)
    test_group = group
    app.go.create_group(test_group)
    app.navigation.group_list()
    old_group_list.append(test_group)
    new_group_list = app.go.get_group_list()
    assert len(new_group_list) == len(old_group_list)
    assert sorted(new_group_list) == sorted(old_group_list)


def test_del_group(app):
    app.navigation.group_list()
    if app.helpers.check_elements_presented() is False:
        new_group = app.go.generate_group(True)
        app.go.create_group(new_group)
    app.navigation.group_list()
    old_group_list = app.go.get_group_list()
    del_id = app.helpers.choose_rnd_el()
    del_group = app.go.find_gr_by_id(del_id)
    app.helpers.click_rnd_el(del_id)
    app.go.delete_group()
    app.navigation.group_list()
    new_group_list = app.go.get_group_list()
    assert len(new_group_list) == (len(old_group_list) - 1)
    assert del_group not in new_group_list


def test_mod_group(app):
    app.navigation.group_list()
    if app.helpers.check_elements_presented() is False:
        new_group = app.go.generate_group(True)
        app.go.create_group(new_group)
    app.navigation.group_list()
    old_group_list = app.go.get_group_list()
    mod_id = app.helpers.choose_rnd_el()
    new_group = app.go.generate_group(mod_id, True)
    app.helpers.click_rnd_el(mod_id)
    app.go.modify_group(new_group)
    app.navigation.group_list()
    new_group_list = app.go.get_group_list()
    assert len(new_group_list) == len(old_group_list)
    assert new_group in new_group_list
