from dbintegtestutils.utils import DBIntegTestCase, load_fixture


class TestMultipleFixtureFiles(DBIntegTestCase):
    """
    Tests that multiple fixture files can be loaded.
    """
    FIXTURE_FILES = [
        'test1.sql',
        'test2.sql'
    ]

    def test_load_single_fixture(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 20)


class TestLoadFixturesAppendData(DBIntegTestCase):
    """
    Tests that @load_fixture decorator will
    append the data to FIXTURE_FILES
    """
    FIXTURE_FILES = [
        'test1.sql',
    ]

    @load_fixture('test2.sql')
    def test_load_fixture_decorator_append_to_fixture_files(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 20)
