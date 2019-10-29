# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.navigation.home_page()
    app.navigation.group_list()
    app.create_items.create_group(Group("name777", "header78", "footer_test"))
    app.navigation.group_list()


def test_del_group(app):
    app.navigation.home_page()
    app.navigation.group_list()
    app.delete_items.delete_group()
    app.navigation.group_list()
