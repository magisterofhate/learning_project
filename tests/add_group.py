# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.navigation.home_page()
    app.navigation.group_list()
    app.create_items.create_group(Group("name1", "header78", "footer_test"))
    app.navigation.group_list()

