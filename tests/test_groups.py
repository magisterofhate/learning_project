# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.navigation.group_list()
    app.go.create_group(Group("name777", "header78", "footer_test"))
    app.navigation.group_list()


def test_del_group(app):
    app.navigation.group_list()
    if app.helpers.check_elements_presented() is False:
        app.go.create_group(Group("name777", "header78", "footer_test"))
    app.navigation.group_list()
    app.helpers.choose_rnd_el()
    app.go.delete_group()
    app.navigation.group_list()


def test_mod_group(app):
    app.navigation.group_list()
    if app.helpers.check_elements_presented() is False:
        app.go.create_group(Group("name777", "header78", "footer_test"))
    app.navigation.group_list()
    app.helpers.choose_rnd_el()
    app.go.modify_group(Group("name123456789999", "header78____AAAAAA", "footer_test____GGGGGG"))
    app.navigation.group_list()
