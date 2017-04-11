from mysql_dao.select_dao import SelectDao as MysqlSelectDao
from postgres_dao.dml_dao import DmlDao as PsqlDmlDao
from datetime import date

mysql_select_dao = MysqlSelectDao()
psql_dml_dao = PsqlDmlDao()

last_upd_date = mysql_select_dao.select_latest_upd_date_addr_price_rpt()

if date.today() == last_upd_date:
    data = mysql_select_dao.select_full_addr_month_rpt()
    psql_dml_dao.trunc_addr_month_rpt()
    psql_dml_dao.insert_addr_month_rpt(data)

data = mysql_select_dao.select_full_mls_daily_rpt()
psql_dml_dao.trunc_mls_rpt()
psql_dml_dao.insert_mls_rpt(data)

mysql_select_dao.close()
psql_dml_dao.close()
