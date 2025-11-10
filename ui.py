from database import Database


db = Database()
conn = db.connect()


def display_program_title() -> None:
    print(f"Welcome to the K-Drama Database")


def display_menu() -> None:
    print(f"{'*' * 5} MAIN MENU {'*' * 5}")
