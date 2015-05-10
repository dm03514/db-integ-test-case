from dbintegtestutils.utils import DBIntegTestCase


class TestMySQLIntegTestCase(DBIntegTestCase):
    FIXTURE_FILE = 'test1.sql'

    def test_test(self):
        pass
