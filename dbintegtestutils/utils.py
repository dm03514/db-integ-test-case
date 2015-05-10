from ConfigParser import ConfigParser
import json
import os
import unittest
from dbintegtestutils.db_handlers import get_db_handler


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

    @classmethod
    def validate_config(cls, config):
        """
        :param config:
        :return:
        """
        SUPPORTED_DBS = ('mysql',)
        assert config.get('db', 'type') in SUPPORTED_DBS

        return config

    def setUp(self):
        self.db_handler.reset_dbs(self.dbs_to_reset)


