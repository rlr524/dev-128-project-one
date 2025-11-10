from dataclasses import dataclass


@dataclass
class Drama:
    id: int = 0
    title: str = ""
    year: str = ""
    episodes: int = 0
    genre: Genre = None
    deleted: bool = False


@dataclass
class Genre:
    id: int = 0
    name: str = ""
