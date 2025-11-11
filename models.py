"""
Dev 128 Fall 2025 Section 27802
Rob Ranf
Programming Project 1: SQLite Database App
Public repo: https://github.com/rlr524/dev-128-project-one

models.py - The model classes for the program's two objects, Drama and Genre.
"""

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
