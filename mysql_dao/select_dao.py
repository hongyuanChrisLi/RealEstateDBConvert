from abstr_mysql_cnx import AbstrMySqlCnx
from utility.constants import ADDR_PRICE_MONTH_RPT_TABLE


class SelectDao(AbstrMySqlCnx):

    def select_addr_month_rpt(self):
        select_stmt = SelectDao.__gen_select_stmt__()
        self.cursor.execute(select_stmt)
        return self.cursor.fetchall()

    @staticmethod
    def __gen_select_stmt__():
        return "SELECT * FROM " + ADDR_PRICE_MONTH_RPT_TABLE + " LIMIT 2"
