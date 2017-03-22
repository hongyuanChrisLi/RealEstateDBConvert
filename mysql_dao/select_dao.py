from abstr_mysql_cnx import AbstrMySqlCnx
from utility.constants import COUNTY_TABLE, CITY_TABLE, ZIPCODE_TABLE
from utility.constants import PROP_ADDR_PRICE_RPT_TABLE, MLS_DAILY_RPT_TABLE


class SelectDao(AbstrMySqlCnx):

    """ Mysql Select Dao """

    def select_all_counties(self):
        print ("Full select on " + COUNTY_TABLE)
        return self._select_full_table_(COUNTY_TABLE)

    def select_all_cities(self):
        print ("Full select on " + CITY_TABLE)
        return self._select_full_table_(CITY_TABLE)

    def select_all_zipcodes(self):
        print ("Full select on " + ZIPCODE_TABLE)
        return self._select_full_table_(ZIPCODE_TABLE)

    def select_full_addr_month_rpt(self):
        print ("Full select on " + PROP_ADDR_PRICE_RPT_TABLE)
        return self._select_full_table_(PROP_ADDR_PRICE_RPT_TABLE)

    def select_full_mls_daily_rpt(self):
        print ("Full select on " + MLS_DAILY_RPT_TABLE)
        return self._select_full_table_(MLS_DAILY_RPT_TABLE)