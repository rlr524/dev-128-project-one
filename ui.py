from database import Database
import services as s
from typing import List, Optional
from models import Genre, Drama


# Instantiate an instance of the Database and create a connection
db = Database()
conn = db.connect()


def display_program_title() -> None:
    print(f"Welcome to the K-Drama Database")


def display_menu() -> None:
    print(f"{'*' * 5} MAIN MENU {'*' * 5}")
    print("1 - List all Dramas")
    print("2 - List all Dramas by Year")
    print("3 - List all Dramas by Genre")
    print("4 - Add a new Drama")
    print("5 - Delete a Drama")
    print("6 - Exit the program")


def display_genres() -> None:
    print(f"{'*' * 5} GENRES {'*' * 5}")
    genres: List[Genre] = s.get_all_genres()
    for genre in genres:
        print(f"{genre.id} - {genre.name}")


def display_dramas(dramas, title_term):
    print(f"{'*' * 5} DRAMAS {'*' * 5}")
    print(f"{'ID':4}{'Title':40}{'Year':6}{'Episodes':4}{'Genre':20}")
    print(f"{'*' * 76}")
    for drama in dramas:
        print(f"{drama.id:<4d}{drama.title:40}{drama.year:<6}{drama.episodes:<4d}{drama.genre.name: 20}")
    print()


def get_int(prompt) -> Optional[int]:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid whole number. Please try again\n")


def display_all_dramas() -> None:
    dramas = s.get_all_dramas()
    display_dramas(dramas, "All Dramas")


def display_dramas_by_genre() -> None:
    genre_id = get_int("Genre ID: ")
    genre = s.get_genre(genre_id)

    if genre is None:
        print("There is no genre with that ID.\n")
    else:
        print()
        dramas = s.get_dramas_by_genre(genre_id)
        display_dramas(dramas, genre.name.upper())


def display_dramas_by_year() -> None:
    year = input("Year: ")
    print()
    dramas = s.get_dramas_by_year(year)
    display_dramas(dramas, year)


def add_drama() -> None:
    title = input("Title: ")
    year = input("Year: ")
    episodes = get_int("Episodes: ")
    genre_id = get_int("Genre ID: ")

    genre = s.get_genre(genre_id)
    if genre is None:
        print("There is no genre with that ID. Drama not added.\n")
    else:
        drama = Drama(title=title, year=year, episodes=episodes, genre=genre)
        s.add_drama(drama)
        print(f"{title} was added to the database.\n")


def delete_drama() -> None:
    drama_id = get_int("Drama ID: ")
    drama_title = s.get_drama(drama_id).title
    s.delete_drama(drama_id)
    print(f"Drama '{drama_title}' was marked as deleted from the database.\n")
