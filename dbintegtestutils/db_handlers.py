import MySQLdb


class MySQLDbTestHandler(object):
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
