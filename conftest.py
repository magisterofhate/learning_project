# -*- coding: utf-8 -*-

import pytest
import json
import os.path
from fixture.application import Application


fixture = None
config = None

@pytest.fixture
def app(request):
    global fixture
    global config
    dir_path = request.config.getoption("--file")
    file_path = os.path.join(dir_path, "cfg_file.json")

    if config is None:
        with open(file_path) as f:
            config = json.load(f)

    if fixture is None or not fixture.helpers.is_session_valid():
        fixture = Application(browser=config['browser'], base_url=config['baseUrl'])
        fixture.navigation.int_login(config['username'], config['password'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def finalize():
        fixture.navigation.int_logout()
        fixture.destroy()
    request.addfinalizer(finalize)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--file", action="store", default="C:/Anatoly_Milinevsky/learning_project/")
