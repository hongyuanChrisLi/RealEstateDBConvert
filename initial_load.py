from mysql_dao.select_dao import SelectDao as MysqlSelectDao
from postgres_dao.ddl_dao import DdlDao
from postgres_dao.dml_dao import DmlDao as PsqlDmlDao

psql_ddl_dao = DdlDao()
mysql_select_dao = MysqlSelectDao()
psql_dml_dao = PsqlDmlDao()

psql_ddl_dao.create_tables()

county_data = mysql_select_dao.select_all_counties()
psql_dml_dao.insert_county(county_data)

city_data = mysql_select_dao.select_all_cities()
psql_dml_dao.insert_city(city_data)

zipcode_data = mysql_select_dao.select_all_zipcodes()
psql_dml_dao.insert_zipcode(zipcode_data)

data = mysql_select_dao.select_full_addr_month_rpt()
psql_dml_dao.trunc_addr_month_rpt()
psql_dml_dao.insert_addr_month_rpt(data)

data = mysql_select_dao.select_full_mls_daily_rpt()
psql_dml_dao.trunc_mls_rpt()
psql_dml_dao.insert_mls_rpt(data)

mysql_select_dao.close()
psql_dml_dao.close()
