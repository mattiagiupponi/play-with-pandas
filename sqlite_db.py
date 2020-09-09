import sqlite3
from sqlite3 import Error


class DbHook:
    def __init__(self):
        self.conn = None

    def get_connection(self):
        """ create a database connection to a database that resides
            in the memory
        """
        try:
            self.conn = sqlite3.connect(":memory:")
            self.__setup_table()
            self.__populate_table()
            return self.conn
        except Error as e:
            raise e

    def close_connection(self):
        """ close database connection to a database that resides in the memory
       """
        if self.conn:
            self.conn.close()

    def __setup_table(self):
        country_table = """CREATE TABLE IF NOT EXISTS country (
                            id integer PRIMARY KEY,
                            name varchar(2) NOT NULL,
                            population INT,
                            continent varchar(100) NOT NULL
                        ); """
        return self.__execute_query(self.conn, country_table)

    def __populate_table(self):
        insert_query = """
        INSERT INTO country VALUES
                (1, 'ao', null, 'africa'),
                (2, 'za', 1000, 'africa'),
                (3, 'uk', 1000, 'europe'),
                (4, 'de', 100, 'europe'),
                (5, 'it', 100, 'europe')
        """
        return self.__execute_query(self.conn, insert_query)

    @staticmethod
    def __execute_query(conn, query):
        try:
            c = conn.cursor()
            c.execute(query)
        except Error as e:
            raise e
