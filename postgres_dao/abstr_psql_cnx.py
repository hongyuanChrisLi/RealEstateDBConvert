import os
import psycopg2
import sys
from utility.uri_parser import parse_url
from utility import constants
from psycopg2 import OperationalError


class AbstrPsqlCnx(object):

    def __init__(self):
        url = os.environ['RET_DB_URL']
        (db_host, db_port, db_name, db_user, db_pass) = parse_url(url)
        try:
            self.cnx = psycopg2.connect(dbname=db_name,
                                        user=db_user,
                                        password=db_pass,
                                        host=db_host,
                                        port=db_port)
        except OperationalError as e:
            print 'Failed to connect to Postgres DB\n{0}'.format(e)
            sys.exit(constants.FAILED_TO_CONNECT)

        print ("Connected to Postgres: " + db_name + "\n")
        self.cursor = self.cnx.cursor()

    def _trunc_table_(self, table):
        self.cursor.execute("TRUNCATE TABLE " + table)

    def _insert_table_(self, table, field_num, data):
        val_format = '('+','.join(['%s']*field_num)+')'
        args_str = ','.join(self.cursor.mogrify(val_format, x) for x in data)
        self.cursor.execute("INSERT INTO " + table + " VALUES " + args_str)
        self.cnx.commit()

    def _select_single_value_(self, stmt):
        self.cursor.execute(stmt)
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.cnx.close()
