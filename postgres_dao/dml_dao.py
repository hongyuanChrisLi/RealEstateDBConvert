from abstr_psql_cnx import AbstrPsqlCnx
from utility.constants import ADDR_PRICE_MONTH_RPT_TABLE, MLS_PRICE_RPT_TABLE


class DmlDao(AbstrPsqlCnx):

    def copy_addr_month_rpt(self, data):
        self._copy_table_(ADDR_PRICE_MONTH_RPT_TABLE, 8, data)

    def trunc_addr_month_rpt(self):
        self._trunc_table_(ADDR_PRICE_MONTH_RPT_TABLE)

    def copy_mls_rpt(self, data):
        self._copy_table_(MLS_PRICE_RPT_TABLE, 9, data)

    def trunc_mls_rpt(self):
        self._trunc_table_(MLS_PRICE_RPT_TABLE)
