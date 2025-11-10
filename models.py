from dataclasses import dataclass


@dataclass
class Drama:
    id: int
    title: str
    year: str
    episodes: int
    genre: Genre
    average_rating: float

    def __init__(self, title: str, year: str, episodes: int, rating: int, genre: Genre, average_rating: float):
        self.title  = title
        self.year = year
        self.episodes = episodes
        self.genre = genre
        self.average_rating = average_rating


@dataclass
class Genre:
    id: int = 0
    name: str = ""


@dataclass
class Rating:
    id: int = 0
    rating: int = 0
    drama_id: int = 0
