# db-integ-test-case

## Provides a framework for python ran integration tests (tests against a database)

This framework provides a class that formalizes setup/teardown/reloading
a test database.

The test class provided is named `DBIntegTestCase`.  All integ tests should subclass
this class.

### Terminology:

- fixture - a file of sql statements, should contain the data necessary to run a specific test
    configurable on a class level to be ran before every test, or on a per test level.
- destroy_db_script - a file of sql statemens that is ran on test class initialization to teardown the database
- create_db_script - file of sql statements that is ran on test class initialization to prepare the database for testing
- database - a database to run tests against.  Right now only mysql is 
- reset_dbs - for mysql all tables in these dbs will be truncated before each test

The flow of the test framework is:

1. Test class Initialization (is ran for each test class)

    - all DESTROY_DB_SCRIPTS are executed
    - all CREATE_DB_SCRIPTS are executed

2. Individual Test case initialization (ran before each individual test)

    - all LOAD_CLASS_FIXTURES are executed
    - all individual test fixtures are executed

---

To run tests a settings file must be defined.  Settings contains credentials
for accessing the database, path information for fixtures, and optional scripts
to be ran before every test.  For an example see `mysql/settings_test.py`.

- `FIXTURES_DIR` - fixtures will be looked for in this path, this should keep fixture declarations
to just the filename.
- `RESET_DBS` - all dbs in this list will have their tables truncated before each test (for mysql)
- `CREATE_DB_SCRIPTS` - a list of sql files to be executed before each test
- `DESTROY_DB_SCRIPS` - a list of sql files to be exectued before each test.  This is the same as `CREATE_DB_SCRIPTS` except
these are executed first.  These separate directives were provided just for ease of use.
- `DATABASE` - contains all database connection information

---
Example of tests can be foundDB_TEST_SETTINGS=tests.mysql.settings_test python -m unittest discover in `test_mysql_test_case.py`.  The mysql tests use the
framework to run the tests :)

Running tests require `DB_TEST_SETTINGS` envvar to be set.

To run the projects unittests:

1. start local mysql server (make sure there is a root/root user with all permissions)
2. `pip install -r requirements.txt`
3. `DB_TEST_SETTINGS=tests.mysql.settings_test python -m unittest discover`
