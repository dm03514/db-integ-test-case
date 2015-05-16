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

class TestMySQLIntegTestCase3(DBIntegTestCase):
    FIXTURE_FILE = 'test1.sql'

    def test_test(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)

    def test_test1(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)

    def test_test2(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)

    def test_test3(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)

    def test_test4(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)
    def test_test5(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)
    def test_test6(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)
    def test_test7(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)
    def test_test8(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)

class TestMySQLIntegTestCase2(DBIntegTestCase):
    FIXTURE_FILE = 'test1.sql'

    def test_test(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)

    def test_test1(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)

    def test_test2(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)

    def test_test3(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)

    def test_test4(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)
    def test_test5(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)
    def test_test6(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)
    def test_test7(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)
    def test_test8(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)

class TestMySQLIntegTestCase1(DBIntegTestCase):
    FIXTURE_FILE = 'test1.sql'

    def test_test(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)

    def test_test1(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)

    def test_test2(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)

    def test_test3(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)

    def test_test4(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)
    def test_test5(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)
    def test_test6(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)
    def test_test7(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)
    def test_test8(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)

class TestMySQLIntegTestCase(DBIntegTestCase):
    FIXTURE_FILE = 'test1.sql'

    def test_test(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)

    def test_test1(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)

    def test_test2(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)

    def test_test3(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)

    def test_test4(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)
    def test_test5(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)
    def test_test6(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)

    def test_test7(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)

    def test_test8(self):
        cursor = self.db_handler.conn.cursor()
        cursor.execute('SELECT * from integtests.example')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)

