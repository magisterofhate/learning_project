# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application


fixture = None


@pytest.fixture
def app():
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.navigation.login()
    else:
        if not fixture.helpers.is_session_valid():
            fixture = Application()
            fixture.navigation.login()
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def finalize():
        fixture.navigation.logout()
        fixture.destroy()
    request.addfinalizer(finalize)
    return fixture
