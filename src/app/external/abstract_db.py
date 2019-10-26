import psycopg2
import psycopg2.extras


class AbstractDbWorker:
    def __init__(self, config):
        self.config = config
        self.conn = self.create_connection()
        self.cur = self.create_cursor()

    def create_connection(self):
        """Создает соединение с бд."""
        return psycopg2.connect(**self.config)

    def create_cursor(self):
        """Создает курсор для взаимодействия с бд."""
        return self.conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)

    def select(self, db_name, columns):
        """SELECT FROM"""
        self.cur.execute(f"SELECT {columns} FROM {db_name};")
        return self.cur.fetchone()

    def select_where(self, condition):
        """SELECT FROM WHERE"""

    def insert(self, data):
        """INSERT INTO"""

    def close(self):
        """Закрывает соединение с бд."""
        self.cur.close()
        self.conn.close()
