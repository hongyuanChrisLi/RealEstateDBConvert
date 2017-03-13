from abstr_psql_cnx import AbstrPsqlCnx


class DdlDao(AbstrPsqlCnx):

    def create_tables(self):
        self.cursor.execute(open('postgres_dao/ddl/create_tables.sql', 'r').read())
        self.cnx.commit()
