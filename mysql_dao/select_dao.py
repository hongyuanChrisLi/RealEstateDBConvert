from abstr_mysql_cnx import AbstrMySqlCnx
from utility.constants import COUNTY_TABLE
from utility.constants import PROP_ADDR_PRICE_RPT_TABLE, MLS_PRICE_RPT_TABLE


class SelectDao(AbstrMySqlCnx):

    """ Mysql Select Dao """

    def select_all_counties(self):
        print ("Full select on " + COUNTY_TABLE)
        return self._select_full_table_(COUNTY_TABLE)

    def select_full_addr_month_rpt(self):
        print ("Full select on " + PROP_ADDR_PRICE_RPT_TABLE)
        return self._select_full_table_(PROP_ADDR_PRICE_RPT_TABLE)

    def select_full_mls_rpt(self):
        print ("Full select on " + MLS_PRICE_RPT_TABLE)
        return self._select_full_table_(MLS_PRICE_RPT_TABLE)

    def select_mls_rpt_after_date(self, date):
        print ("Select " + MLS_PRICE_RPT_TABLE +
               " after date " + date[0].strftime('%Y-%m-%d'))
        stmt = self.__gen_select_lt_date_stmt__()
        return self._select_(stmt, date)

    """ static """
    @staticmethod
    def __gen_select_lt_date_stmt__():
        return 'SELECT * FROM ' + MLS_PRICE_RPT_TABLE + ' WHERE RPT_DATE > %s'
