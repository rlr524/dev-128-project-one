# import the sqlite3 database module
import sqlite3

# create a connection to the database file
conn = sqlite3.connect("drama_database.sqlite")

# create a cursor that we will use to move through the database
cursor = conn.cursor()

# create the tables if they don't already exist
# note that primary keys are automatically created in sqlit3 and referenced as rowid
cursor.execute('''CREATE TABLE IF NOT EXISTS dramas (title TEXT, year TEXT, episodes INTEGER, genre_id INTEGER, average_rating REAL)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS genres (name TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS ratings (rating INTEGER, drama_id INTEGER)''')

# create some records of data for genres
cursor.execute('''INSERT INTO genres(name) VALUES ('Romantic Comedy')''')
cursor.execute('''INSERT INTO genres(name) VALUES ('Thriller')''')
cursor.execute('''INSERT INTO genres(name) VALUES ('Workplace Drama')''')

# create some records of data for dramas
cursor.execute('''INSERT INTO dramas(title, year, episodes, genre_id, average_rating)
               VALUES ('Goblin', '2016', 16, 1, 0.0 )''')
cursor.execute('''INSERT INTO dramas(title, year, episodes, genre_id, average_rating)
               VALUES ('The Glory', '2022', 16, 2, 0.0 )''')
cursor.execute('''INSERT INTO dramas(title, year, episodes, genre_id, average_rating)
               VALUES ('Extraordinary Attorney Woo', '2022', 16, 3, 0.0 )''')
cursor.execute('''INSERT INTO dramas(title, year, episodes, genre_id, average_rating)
               VALUES('Squid Game', '2021', 22, 2, 0.0 )''')

# create some ratings on the dramas
cursor.execute('''INSERT INTO ratings(rating, drama_id) VALUES (9, 1)''')
cursor.execute('''INSERT INTO ratings(rating, drama_id) VALUES (8, 1)''')
cursor.execute('''INSERT INTO ratings(rating, drama_id) VALUES (10, 2)''')
cursor.execute('''INSERT INTO ratings(rating, drama_id) VALUES (9, 2)''')
cursor.execute('''INSERT INTO ratings(rating, drama_id) VALUES (10, 3)''')
cursor.execute('''INSERT INTO ratings(rating, drama_id) VALUES (7, 3)''')
cursor.execute('''INSERT INTO ratings(rating, drama_id) VALUES (8, 4)''')
cursor.execute('''INSERT INTO ratings(rating, drama_id) VALUES (9, 4)''')

# commit the changes to the database
conn.commit()

# close the database
conn.close()
