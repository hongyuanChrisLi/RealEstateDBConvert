from abstr_psql_cnx import AbstrPsqlCnx
from utility.constants import COUNTY_TABLE, CITY_TABLE, ZIPCODE_TABLE
from utility.constants import PROP_ADDR_PRICE_RPT_TABLE, MLS_PRICE_RPT_TABLE


class DmlDao(AbstrPsqlCnx):

    """ Postgres DML Dao """

    """ COUNTY_TABLE """
    def insert_county(self, data):
        self.__print_insert__(COUNTY_TABLE, len(data))
        self._insert_table_(COUNTY_TABLE, 2, data)

    """ CITY_TABLE """
    def insert_city(self, data):
        self.__print_insert__(CITY_TABLE, len(data))
        self._insert_table_(CITY_TABLE, 3, data)

    """ ZIPCODE_TABLE """
    def insert_zipcode(self, data):
        self.__print_insert__(ZIPCODE_TABLE, len(data))
        self._insert_table_(ZIPCODE_TABLE, 3, data)

    """ ADDR_PRICE_MONTH_RPT_TABLE """

    def insert_addr_month_rpt(self, data):
        self.__print_insert__(PROP_ADDR_PRICE_RPT_TABLE, len(data))
        self._insert_table_(PROP_ADDR_PRICE_RPT_TABLE, 9, data)

    def trunc_addr_month_rpt(self):
        self._trunc_table_(PROP_ADDR_PRICE_RPT_TABLE)

    """ MLS_PRICE_RPT_TABLE """

    def select_latest_date(self):
        return self._select_single_value_(self.__gen_select_max_date_stmt__())

    def insert_mls_rpt(self, data):
        rec_num = len(data)
        if rec_num == 0:
            print("No insert to " + MLS_PRICE_RPT_TABLE)
        else:
            self.__print_insert__(MLS_PRICE_RPT_TABLE, rec_num)
            self._insert_table_(MLS_PRICE_RPT_TABLE, 9, data)

    def trunc_mls_rpt(self):
        self._trunc_table_(MLS_PRICE_RPT_TABLE)

    """ static """

    @staticmethod
    def __gen_select_max_date_stmt__():
        return "SELECT MAX(RPT_DATE) FROM " + MLS_PRICE_RPT_TABLE

    @staticmethod
    def __print_insert__(table, num):
        print("Insert " + str(num) + " records to " + table)
