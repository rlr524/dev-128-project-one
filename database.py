"""
Dev 128 Fall 2025 Section 27802
Rob Ranf
Programming Project 1: SQLite Database App
Public repo: https://github.com/rlr524/dev-128-project-one

database.py - A convenience module used to abstract database connection details from the business logic and ui.
"""

import sqlite3


class Database:
    def connect(self) -> sqlite3.Connection:
        """
        A reusable connect method. The creation of a Database class allows for the database to be easily updated
        to a different database engine without needing to touch the model, services layer, or user interface. This
        is generally equivalent to using the Repository pattern in Java and other languages to abstract away the
        database access layer.
        :return: A SQLite3 Connection object
        """
        conn: sqlite3.Connection = sqlite3.connect("drama_database.sqlite")
        conn.row_factory = sqlite3.Row

        return conn


    def close(self):
        """
        A reusable close method that can be called to close the database connection in instances in which the
        closing context from the contextlib library isn't used.
        :return: None
        """
        conn: sqlite3.Connection = self.connect()
        if conn:
            conn.close()
