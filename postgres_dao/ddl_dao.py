from abstr_psql_cnx import AbstrPsqlCnx


class DdlDao(AbstrPsqlCnx):

    def run(self):
        return