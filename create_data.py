"""
Dev 128 Fall 2025 Section 27802
Rob Ranf
Programming Project 1: SQLite Database App
Public repo: https://github.com/rlr524/dev-128-project-one

create_data.py - A utility file used to create database tables and starter data.
"""

# import the sqlite3 database module
import sqlite3

# create a connection to the database file
conn = sqlite3.connect("drama_database.sqlite")

# create a cursor that we will use to move through the database
cursor = conn.cursor()

# create the tables if they don't already exist
# note that primary keys are automatically created in sqlit3 and referenced as rowid
cursor.execute('''CREATE TABLE IF NOT EXISTS dramas (drama_id INTEGER PRIMARY KEY, title TEXT, year TEXT, episodes INTEGER, genre_id INTEGER, deleted BOOLEAN)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS genres (genre_id INTEGER PRIMARY KEY, name TEXT)''')

# create some records of data for genres
cursor.execute('''INSERT INTO genres(name) VALUES ('Romantic Comedy')''')
cursor.execute('''INSERT INTO genres(name) VALUES ('Thriller')''')
cursor.execute('''INSERT INTO genres(name) VALUES ('Workplace Drama')''')

# create some records of data for dramas
cursor.execute('''INSERT INTO dramas(title, year, episodes, genre_id, deleted)
               VALUES ('Guardian: The Lonely and Great God', '2016', 16, 1, FALSE)''')
cursor.execute('''INSERT INTO dramas(title, year, episodes, genre_id, deleted)
               VALUES ('The Glory', '2022', 16, 2, FALSE)''')
cursor.execute('''INSERT INTO dramas(title, year, episodes, genre_id, deleted)
               VALUES ('Extraordinary Attorney Woo', '2022', 16, 3, FALSE)''')
cursor.execute('''INSERT INTO dramas(title, year, episodes, genre_id, deleted)
               VALUES('Squid Game', '2021', 22, 2, FALSE)''')

# commit the changes to the database
conn.commit()

# close the database
conn.close()
