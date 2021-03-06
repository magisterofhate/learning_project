# -*- coding: utf-8 -*-

import pytest
import json
import os.path as op
from fixture.application import Application
import jsonpickle
from fixture.db import DbFixture


# fixture = None
config = None


def load_config(file_path):
    global config
    if config is None:
        with open(file_path) as f:
            config = json.load(f)
    return config


@pytest.fixture
def app(app_for_session):
    # global fixture
    # global config
    # dir_path = request.config.getoption("--file")
    # file_path = op.join(dir_path, "cfg_file.json")
    #
    # web_config = load_config(file_path)['web']

    # if config is None:
    #     with open(file_path) as f:
    #         config = json.load(f)

    if app_for_session is None or not app_for_session.is_session_valid():
        app_for_session.initialize()
    return app_for_session


@pytest.fixture(scope="session")
def app_for_session(request):
    dir_path = request.config.getoption("--file")
    file_path = op.join(dir_path, "cfg_file.json")
    web_config = load_config(file_path)['web']
    app = Application(browser=web_config['browser'], base_url=web_config['baseUrl'], username=web_config['username'],
                      password=web_config['password'])
    app.initialize()
    # app.navigation.int_login(web_config['username'], web_config['password'])

    def finalize():
        app.navigation.int_logout()
        app.destroy()
    request.addfinalizer(finalize)
    return app


@pytest.fixture(scope="session")
def db(request):
    dir_path = request.config.getoption("--file")
    file_path = op.join(dir_path, "cfg_file.json")
    db_config = load_config(file_path)['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], pwd=db_config['pwd'])

    def finalize():
        dbfixture.destroy()
    request.addfinalizer(finalize)
    return dbfixture


# @pytest.fixture(scope="session", autouse=True)
# def stop(request):
#     global fixture
#     fixture = Application(browser=web_config['browser'], base_url=web_config['baseUrl'])
#
#     def finalize():
#         fixture.navigation.int_logout()
#         fixture.destroy()
#     request.addfinalizer(finalize)
#     return fixture


@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


def pytest_addoption(parser):
    parser.addoption("--file", action="store", default="C:/Anatoly_Milinevsky/learning_project/")
    parser.addoption("--check_ui", action="store_true")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("test_data_"):
            test_data = load_from_json(fixture[10:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])


def load_from_json(file):
    with open(op.join(op.dirname(op.abspath(__file__)), "test_data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())
