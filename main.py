from postgres_dao.ddl_dao import DdlDao
from mysql_dao.select_dao import SelectDao as MysqlSelectDao
from postgres_dao.dml_dao import DmlDao as PsqlDmlDao
from mysql_dao.abstr_mysql_cnx import AbstrMySqlCnx


mysql_select_dao = MysqlSelectDao()
psql_dml_dao = PsqlDmlDao()

data = mysql_select_dao.select_addr_month_rpt()
psql_dml_dao.trunc_addr_month_rpt()
psql_dml_dao.copy_data_to_addr_month_rpt_a(data)

mysql_select_dao.close()
psql_dml_dao.close()

# ddl_cnx = DdlDao()
# ddl_cnx.create_tables()