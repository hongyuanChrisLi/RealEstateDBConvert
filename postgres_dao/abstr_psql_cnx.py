import os
import psycopg2
from utility.uri_parser import parse_url


class AbstrPsqlCnx(object):
    def __init__(self):
        url = os.environ['RET_DB_URL']
        (db_host, db_port, db_name, db_user, db_pass) = parse_url(url)
        print(parse_url(url))
        self.cnx = psycopg2.connect(dbname=db_name,
                                    user=db_user,
                                    password=db_pass,
                                    host=db_host,
                                    port=db_port)
        self.cursor = self.cnx.cursor()

