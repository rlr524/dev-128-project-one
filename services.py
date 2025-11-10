from database import Database
from models import Drama, Genre, Rating
from contextlib import closing
from typing import Any, List

db = Database()
conn = db.connect()


def make_drama(row: Any) -> Drama:
    return Drama(row["rowid"], row["title"], row["year"], row["episodes"], make_genre(row), row["average_rating"])


def make_genre(row: Any) -> Genre:
    return Genre(row["rowid"], row["name"])


def make_drama_list(output) -> List[Drama]:
    dramas: List[Drama] = []
    for r in output:
        dramas.append(make_drama(r))
    return  dramas


