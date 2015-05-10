from dbintegtestutils.utils import DBIntegTestCase, load_fixture


class TestMySQLIntegTestCase(DBIntegTestCase):

    @load_fixture('test1.sql')
    def test_test(self):
        pass
