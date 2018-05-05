import os
import pytest


@pytest.fixture
def custom_fixture(tmpdir):
    with open(os.path.join(tmpdir, "test.txt"), "w+") as c:
        print("before yield")
        yield c
        print("after yield")


def pytest_addoption(parser):
    parser.addoption('--os-name', default='linux', help='os_name')
