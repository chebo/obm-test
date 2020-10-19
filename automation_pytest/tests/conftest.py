import pytest


@pytest.fixture(scope='function')
def case_data():
    print("\nHi!!!")
    yield
    print("\nBye!!!")