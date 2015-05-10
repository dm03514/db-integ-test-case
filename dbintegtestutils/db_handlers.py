import MySQLdb


SUPPORTED_DBS = ('mysql',)


class MySQLDbTestHandler(object):
    SWITCH_DB_SQL = 'USE {}'
    TRUNCATE_TABLE_SQL = 'TRUNCATE TABLE {}'
    SELECT_TABLES_SQL = """
        SELECT TABLE_NAME
        FROM information_schema.TABLES
        WHERE TABLE_SCHEMA = '{}'
    """

    def __init__(self, user, password, host, port):
        conn_kwargs =  {
            'user': user,
            'host': host,
        }
        if password is not None:
            conn_kwargs['passwd'] = password
        if port is not None:
            conn_kwargs['port'] = int(port)

        self.conn = MySQLdb.connect(**conn_kwargs)

    def destroy_db(self, destroy_db_script):
        """
        Executes the contents of destroy_db_script against the db.
        """
        self._execute_from_file(destroy_db_script)

    def initialize_db(self, create_db_script):
        """
        Executes the contents of create_db_script against the db.
        """
        self._execute_from_file(create_db_script)

    def load_fixture(self, fixture_path):
        """
        Loads the fixture_path into the db.
        """
        self._execute_from_file(fixture_path)

    def reset_dbs(self, dbs_to_reset):
        """
        Truncates all tables in the list of dbs_to_reset.
        """
        TABLE_NAME_INDEX = 0
        cursor = self.conn.cursor()
        for db_name in dbs_to_reset:
            cursor.execute(self.SWITCH_DB_SQL.format(db_name))

            cursor.execute('SET FOREIGN_KEY_CHECKS=0')

            cursor.execute(self.SELECT_TABLES_SQL.format(db_name))
            rows = cursor.fetchall()
            for row in rows:
                cursor.execute(self.TRUNCATE_TABLE_SQL.format(row[TABLE_NAME_INDEX]))

            cursor.execute('SET FOREIGN_KEY_CHECKS=1')

        cursor.close()

    def _execute_from_file(self, file_path):
        """
        Executes the contents of `file_path` against the db.
        """
        with open(file_path) as f:
            cursor = self.conn.cursor()
            cursor.execute(f.read())
            cursor.close()
            self.conn.commit()


def get_db_handler(db_conf):
    """
    Instantiates a DB wrapper object for generically interacting
    with any supported db backend.

    :param db_name:
    :return:
    """
    if db_conf.get('type') == 'mysql':
        return MySQLDbTestHandler(
            user=db_conf.get('user'),
            password=db_conf.get('password'),
            host=db_conf.get('host'),
            port=db_conf.get('port')
        )
