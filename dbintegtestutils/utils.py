from ConfigParser import ConfigParser
import functools
import json
import os
import unittest
from dbintegtestutils.db_handlers import get_db_handler, SUPPORTED_DBS


class DBIntegTestCase(unittest.TestCase):
    db_handler = None
    dbs_to_reset = None

    @classmethod
    def setUpClass(cls):
        """
        Initialized db integ test by:
        - parsevalidating config
        - executing create db command

        :return:
        """
        config = ConfigParser()
        config.read(os.environ.get('DB_TEST_CONF_PATH'))
        config = cls.validate_config(config)

        cls.db_handler = get_db_handler(dict(config.items('db')))

        cls.db_handler.destroy_db(
            config.get('managementscripts', 'destroy_db_script'))

        cls.db_handler.initialize_db(
            config.get('managementscripts', 'create_db_script'))

        cls.dbs_to_reset = json.loads(config.get('dbintegtests', 'reset_dbs'))

        cls.config = config

    @classmethod
    def validate_config(cls, config):
        """
        :param config:
        :return:
        """
        assert config.get('db', 'type') in  SUPPORTED_DBS

        return config

    @property
    def fixtures_dir(self):
        return self.config.get('dbintegtests', 'fixtures_dir')

    def load_fixture(self, test_module_string):
        """
        Loads the appropriate test fixture for the current test.
        Loading consists of opening a file with sql statements
        and executing those commands against the current db.

        Fixtures can be specified on the class level, which would
        apply against every class or per test by decorating it.

        All fixtures should specifiy filenames that will be loaded
        in reference to `fixture_dirs` in the config file.

        :param: test_module_string represents the current test as
            returned by TestCase.id() method
        :return:
        """
        # default to the class attribute
        fixture_file = getattr(self, 'FIXTURE_FILE', None)

        test_method = self._get_test_method(test_module_string)
        if hasattr(test_method, '_integ_fixture_file'):
            fixture_file = test_method._integ_fixture_file

        assert fixture_file

        fixture = os.path.join(self.fixtures_dir, fixture_file)
        self.db_handler.load_fixture(fixture)

    def setUp(self):
        self.db_handler.reset_dbs(self.dbs_to_reset)
        self.load_fixture(self.id())

    def _get_test_method(self, test_module_string):
        """
        Dynamically imports test method to inspect whether it is decorated
        or not.
        """
        module_str, klass_str, method_str = test_module_string.split('.')
        module =  __import__(module_str, fromlist=[klass_str])
        klass = getattr(module, klass_str)
        method = getattr(klass, method_str)
        return method


class load_fixture(object):
    """
    Attaches fixture file name to wrapped function

    :param func:
    :return:
    """
    def __init__(self, fixture_name):
        self.fixture_name = fixture_name

    def __call__(self, func):
        func._integ_fixture_file = self.fixture_name
        return func
