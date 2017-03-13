import os
import mysql.connector
import sys

from mysql.connector.errors import ProgrammingError

from utility.uri_parser import parse_url
from utility import constants


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
        try:
            self.cnx = mysql.connector.connect(**config)
        except ProgrammingError as e:
            print('Failed to connect to Mysql DB')
            print(e)
            sys.exit(constants.FAILED_TO_CONNECT)

        self.cursor = self.cnx.cursor()
