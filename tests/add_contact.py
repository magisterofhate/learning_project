# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.open_home_page()
    app.create_new_contact(Contact(f_name="First_Name", l_name="Last_Name", m_phone="+7888996755", day_dob="15", month_dob="May", year_dob="1987"))
    app.open_home_page()
