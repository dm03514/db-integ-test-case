import os
from dbintegtestutils.settings_base import *

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
FIXTURES_DIR = os.path.join(FILE_PATH, 'fixtures')
RESET_DBS = ['integtests']

CREATE_DB_SCRIPTS = [
    os.path.join(FILE_PATH, 'test_create.sql')
]

DESTROY_DB_SCRIPTS = [
    os.path.join(FILE_PATH, 'test_destroy.sql')
]

DATABASE = {
    'type': 'mysql',
    'user': 'root',
    'host': 'localhost',
    'password': 'root',
    'port': 3306
}
