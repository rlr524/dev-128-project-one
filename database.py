import sqlite3


class Database:
    def connect(self) -> sqlite3.Connection:
        conn: sqlite3.Connection = sqlite3.connect("drama_database.sqlite")
        conn.row_factory = sqlite3.Row

        return conn


    def close(self):
        conn: sqlite3.Connection = self.connect()
        if conn:
            conn.close()
