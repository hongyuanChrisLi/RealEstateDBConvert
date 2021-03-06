import os
import mysql.connector
import sys

from mysql.connector.errors import ProgrammingError

from utility.uri_parser import parse_url
from utility import constants


class AbstrMySqlCnx(object):

    def __init__(self):
        url = os.environ['RET_MYSQL_URL']
        (db_host, db_port, db_name, db_user, db_pass) = parse_url(url)
        self.schema = db_name
        config = {
            'user': db_user,
            'password': db_pass,
            'host': db_host,
            'port': db_port,
            'database': db_name,
            'autocommit': True
            }
        try:
            self.cnx = mysql.connector.connect(**config)
        except ProgrammingError as e:
            print 'Failed to connect to Mysql DB\n{0}'.format(e)
            sys.exit(constants.FAILED_TO_CONNECT)

        print ("Connected to mysql: " + db_name + "\n")
        self.cursor = self.cnx.cursor()

    def _select_full_table_(self, table):
        stmt = "SELECT * FROM " + table
        self.cursor.execute(stmt)
        return self.cursor.fetchall()

    def _select_(self, stmt, data):
        self.cursor.execute(stmt, data)
        return self.cursor.fetchall()

    def _select_single_value_(self, sel_stmt):
        self.cursor.execute(sel_stmt)
        return self.cursor.fetchone()[0]

    def close(self):
        self.cursor.close()
        self.cnx.close()
