import pytest


class TestSuite():
    @pytest.mark.fixtures
    def test_using_fixture(self, case_data):
        print(" >>> Testing something")
        assert True