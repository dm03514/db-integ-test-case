from dbintegtestutils.settings_base import *

FIXTURES_DIR = '/home/daniel/code/github/db-integ-test-case/tests/mysql/fixtures/'
RESET_DBS = ['integtests']

CREATE_DB_SCRIPTS = [
    '/home/daniel/code/github/db-integ-test-case/tests/mysql/test_create.sql'
]

DESTROY_DB_SCRIPTS = [
    '/home/daniel/code/github/db-integ-test-case/tests/mysql/test_destroy.sql'
]

DATABASE = {
    'type': 'mysql',
    'user': 'root',
    'host': 'localhost',
    'password': 'root',
    'port': 3306
}
