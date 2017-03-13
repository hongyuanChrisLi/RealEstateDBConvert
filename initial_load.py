from mysql_dao.select_dao import SelectDao as MysqlSelectDao
from postgres_dao.dml_dao import DmlDao as PsqlDmlDao

mysql_select_dao = MysqlSelectDao()
psql_dml_dao = PsqlDmlDao()

data = mysql_select_dao.select_full_addr_month_rpt()
psql_dml_dao.trunc_addr_month_rpt()
psql_dml_dao.insert_addr_month_rpt(data)

data = mysql_select_dao.select_full_mls_rpt()
psql_dml_dao.trunc_mls_rpt()
psql_dml_dao.insert_mls_rpt(data)

mysql_select_dao.close()
psql_dml_dao.close()
