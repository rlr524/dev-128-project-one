"""
Dev 128 Fall 2025 Section 27802
Rob Ranf
Programming Project 1: SQLite Database App
Public repo: https://github.com/rlr524/dev-128-project-one

main.py - The program entry point.
"""

from database import Database
import ui

# Instantiate an instance of the Database and create a connection
db = Database()
conn = db.connect()


def main():
    ui.display_program_title()
    print()
    ui.display_menu()
    print()
    ui.display_genres()
    print()
    while True:
        command = input("Command (enter a row number from the Menu): ")
        if command == "1":
            ui.display_all_dramas()
        elif command == "2":
            ui.display_dramas_by_year()
        elif command == "3":
            ui.display_dramas_by_genre()
        elif command == "4":
            ui.add_drama()
        elif command == "5":
            ui.delete_drama()
        elif command == "6":
            break
        else:
            print("Not a valid command. Please enter a whole number corresponding to a menu item.\n")
    db.close()
    print("Thank you for visiting!")


if __name__ == "__main__":
    main()
