# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application


fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url)
        fixture.navigation.int_login('admin', 'secret')
    else:
        if not fixture.helpers.is_session_valid():
            fixture = Application(browser=browser, base_url=base_url)
            fixture.navigation.int_login('admin', 'secret')
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def finalize():
        fixture.navigation.int_logout()
        fixture.destroy()
    request.addfinalizer(finalize)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="ff")
    parser.addoption("--baseUrl", action="store", default="http://10.201.48.35/addressbook/")
