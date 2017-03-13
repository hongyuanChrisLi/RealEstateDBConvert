import os
import mysql.connector
from utility.uri_parser import parse_url


class AbstrMySqlCnx(object):

    def __init__(self):
        url = os.environ['RET_MYSQL_URL']
        (db_host, db_port, database, db_user, db_pass) = parse_url(url)
        config = {
            'user': db_user,
            'password': db_pass,
            'host': db_host,
            'port': db_port,
            'database': database,
            'autocommit': True
            }
        self.cnx = mysql.connector.connect(**config)
        self.cursor = self.cnx.cursor()
