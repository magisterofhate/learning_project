# -*- coding: utf-8 -*-

import pytest
import json
import os.path as op
from fixture.application import Application
import jsonpickle


fixture = None
config = None

@pytest.fixture
def app(request):
    global fixture
    global config
    dir_path = request.config.getoption("--file")
    file_path = op.join(dir_path, "cfg_file.json")

    if config is None:
        with open(file_path) as f:
            config = json.load(f)

    if fixture is None or not fixture.is_session_valid():
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


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("test_data_"):
            test_data = load_from_json(fixture[10:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])


def load_from_json(file):
    with open(op.join(op.dirname(op.abspath(__file__)), "test_data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())
