import logging
from database import Database
from models import Drama, Genre
from contextlib import closing
from typing import Any, List, Optional

# Instantiate an instance of the Database and create a connection
db = Database()
conn = db.connect()

def make_genre(row: Any) -> Genre:
    """
    Creates a new Genre instance given input from a SQL query
    :param row: A parameter of type Any that is passed to the initializer of a Genre instance
    :return: An instance of the Genre class
    """
    return Genre(row["genre_id"], row["name"])


def make_drama(row: Any) -> Drama:
    """
    Creates a new Drama instance given input from a SQL query
    :param row: A parameter of type Any that is passed to the initializer of a Drama instance
    :return: An instance of the Drama class
    """
    return Drama(row["drama_id"], row["title"], row["year"], row["episodes"], make_genre(row), row["deleted"])


def make_drama_list(drama_results: Any) -> List[Drama]:
    """
    Creates a List of Drama instances given input from a SQL query
    :param drama_results: A parameter of type Any that represents a List of drama rows from a DB query
    :return: A List of instances of the Drama class
    """
    dramas: List[Drama] = []
    for r in drama_results:
        dramas.append(make_drama(r))
    return  dramas


def get_drama(drama_id: int) -> Optional[Drama]:
    """
    Get a single drama given a drama's id
    :param drama_id: An int representing the id of a drama
    :return: An Optional of a Drama object or None of the drama_id doesn't exist
    """
    q = '''SELECT d.drama_id, d.title, d.year, d.episodes, g.name AS genre_name, d.deleted 
           FROM dramas d join genres g ON g.genre_id = d.genre_id
           WHERE d.drama_id = ?'''
    with closing(conn.cursor()) as c:
        c.execute(q, (drama_id,))
        drama_row: Any = c.fetchone
        if drama_row:
            return make_drama(drama_row)
        else:
            return None


def get_all_dramas() -> List[Drama]:
    """
    Get all dramas in the database
    :return: A List of Drama objects representing all Dramas where the deleted flag is not True
    Note: This can be debated as to if the logic for the deleted flag should be applied here or in the UI. For the
    sake of keeping the assignment fairly simple, I applied it here.
    """
    q = '''SELECT d.drama_id, d.title, d.year, d.episodes, d.genre_id, g.name AS genre_name, d.deleted 
           FROM dramas d JOIN genres g ON g.genre_id = d.genre_id
           WHERE d.deleted <> true'''
    with closing(conn.cursor()) as c:
        c.execute(q)
        results = c.fetchall()

    dramas: List[Drama] = []
    for r in results:
        dramas.append(make_drama(r))
    return  dramas


def get_all_genres() -> List[Genre]:
    """
    Get all genres in the database
    :return: A list of Genre objects
    """
    q = '''SELECT genre_id, name FROM genres '''
    with closing(conn.cursor()) as c:
        c.execute(q)
        results = c.fetchall()

    genres: List[Genre] = []
    for r in results:
        genres.append(make_genre(r))
    return genres


def get_genre(genre_id: int) -> Optional[Genre]:
    """
    Get a genre given a specific genre id
    :param genre_id: An int value representing the genre_id of a Genre object
    :return: An optional of a Genre object, or None if the genre_id does not exist
    """
    q = '''SELECT genre_id, name FROM genres WHERE genre_id = ?'''
    with closing(conn.cursor()) as c:
        c.execute(q, (genre_id,))
        genre_row: Any = c.fetchone
        if genre_row:
            return make_genre(genre_row)
        else:
            return None


def get_dramas_by_genre(genre_id: int) -> List[Drama]:
    """
    Gets all dramas given a specific genre
    :param genre_id: An int value representing the genre_id of a Genre object
    :return: A List of Drama objects
    """
    q = '''SELECT d.drama_id, d.title, d.year, d.episodes, g.name AS genre_name, d.deleted
           FROM dramas d JOIN genres g ON g.genre_id = d.genre_id
           WHERE d.genre_id = ?'''
    with closing(conn.cursor()) as c:
        c.execute(q, (genre_id,))
        results: List[Any] = c.fetchall()

    return make_drama_list(results)


def get_dramas_by_year(year: str) -> List[Drama]:
    """
    Gets all dramas given a specific year
    :param year: A string value representing a four digit year
    :return: A List of Drama objects
    """
    q = '''SELECT d.drama_id, d.title, d.year, d.episodes, g.name AS genre_name, d.deleted
           FROM dramas d JOIN genres g ON g.genre_id = d.genre_id
           WHERE d.year = ?'''
    with closing(conn.cursor()) as c:
        c.execute(q, (year,))
        results: List[Any] = c.fetchall()

    return make_drama_list(results)


def add_drama(drama: Drama) -> None:
    """
    Add a single drama to the database. Includes validation of required fields that do not have a default value as
    well as error handling for database transaction commit errors. This error handling is necessary on any function
    that performs a transaction commit on the database in order to comply with ACID assurance.
    :param drama: A Drama object to insert
    :return: None
    :raises: A SQLite Database error if insertion fails. If this were a production application, I would include
    methods for this error handling in the Database class as it is specific to SQLite3.
    """
    if not getattr(drama, "genre", None) or getattr(drama.genre, "genre_id", None) is None:
        raise ValueError("drama genre id is required")
    if not getattr(drama, "title", None):
        raise ValueError("drama title is required")
    if not getattr(drama, "year", None):
        raise ValueError("drama year is required")
    if not getattr(drama, "episodes", None):
        raise ValueError("drama episodes is required")

    s = '''INSERT INTO dramas (title, year, episodes, genre_id, deleted) VALUES (?, ?, ?, ?, false)'''
    try:
        with closing(conn.cursor()) as c:
            c.execute(s, (drama.title, drama.year, drama.episodes, drama.genre.id, drama.deleted))
        conn.commit()
    except conn.DatabaseError as e:
        try:
            conn.rollback()
        except conn.OperationalError:
            logging.exception("Failed to roll back transaction after insert failure")
        logging.exception(f"Failed to insert drama {e}")
        raise


def delete_drama(drama_id: int) -> None:
    """
    Perform a soft delete by flagging a single drama as deleted. Includes error handling for database transaction
    commit errors. This error handling is necessary on any function that performs a transaction commit on the
    database in order to comply with ACID assurance.
    :param drama_id: The drama_id of the intended drama
    :return: None
    :raises: A Database error if insertion fails
    """
    s = '''UPDATE dramas SET deleted = true WHERE drama_id = ?'''
    try:
        with closing(conn.cursor()) as c:
            c.execute(s, (drama_id,))
        conn.commit()
    except conn.DatabaseError as e:
        try:
            conn.rollback()
        except conn.OperationalError:
            logging.exception("Failed to roll back transaction after delete failure")
        logging.exception(f"Failed to delete drama {e}")
        raise
