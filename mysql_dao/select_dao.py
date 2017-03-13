from abstr_mysql_cnx import AbstrMySqlCnx
from utility.constants import ADDR_PRICE_MONTH_RPT_TABLE, MLS_PRICE_RPT_TABLE


class SelectDao(AbstrMySqlCnx):

    def select_full_addr_month_rpt(self):
        return self._select_full_table_(ADDR_PRICE_MONTH_RPT_TABLE)

    def select_full_mls_rpt(self):
        return self._select_full_table_(MLS_PRICE_RPT_TABLE)
