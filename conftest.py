# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application


fixture = None


@pytest.fixture
def app():
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.navigation.int_login('admin', 'secret')
    else:
        if not fixture.helpers.is_session_valid():
            fixture = Application()
            fixture.navigation.int_login('admin', 'secret')
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def finalize():
        fixture.navigation.int_logout()
        fixture.destroy()
    request.addfinalizer(finalize)
    return fixture
