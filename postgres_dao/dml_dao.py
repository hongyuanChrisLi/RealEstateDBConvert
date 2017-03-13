from abstr_psql_cnx import AbstrPsqlCnx
from utility.constants import ADDR_PRICE_MONTH_RPT_TABLE


class DmlDao(AbstrPsqlCnx):

    def copy_data_to_addr_month_rpt_a(self, data):
        insert_stmt = DmlDao.__gen_insert_stmt__()
        self.cursor.executemany(insert_stmt, data)
        self.cnx.commit()

    def copy_data_to_addr_month_rpt_b(self, data):
        args_str = ','.join(self.cursor.mogrify("(%s,%s,%s,%s,%s,%s,%s,%s)", x) for x in data)
        self.cursor.execute("INSERT INTO " + ADDR_PRICE_MONTH_RPT_TABLE + " VALUES " + args_str)
        self.cnx.commit()

    def trunc_addr_month_rpt(self):
        self.cursor.execute("TRUNCATE TABLE " + ADDR_PRICE_MONTH_RPT_TABLE)

    @staticmethod
    def __gen_insert_stmt__():
        return 'INSERT INTO ' + ADDR_PRICE_MONTH_RPT_TABLE + \
               ' (AREA_ID, PROP_TYPE_ID, RPT_DATE, CITY, ZIPCODE,' \
               ' AVG_PRICE, AVG_PRICE_STRUCT_SQFT, AVG_PRICE_TOT_SQFT)' \
               ' VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
