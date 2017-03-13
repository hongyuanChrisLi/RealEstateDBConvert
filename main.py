from postgres_dao.ddl_dao import DdlDao
from mysql_dao.select_dao import SelectDao as MysqlSelectDao
from postgres_dao.dml_dao import DmlDao as PsqlDmlDao
from mysql_dao.abstr_mysql_cnx import AbstrMySqlCnx

import time


def get_hms(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

mysql_select_dao = MysqlSelectDao()
psql_dml_dao = PsqlDmlDao()

data = mysql_select_dao.select_addr_month_rpt()
psql_dml_dao.trunc_addr_month_rpt()

start = time.time()
psql_dml_dao.copy_data_to_addr_month_rpt_a(data)
print (get_hms(time.time() - start))

mysql_select_dao.close()
psql_dml_dao.close()


# ddl_cnx = DdlDao()
# ddl_cnx.create_tables()