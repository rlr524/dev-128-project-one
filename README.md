# Programming Assignment 1 for DEV 128 Due 11/9/2025

> This README file was generated with the assistance of Microsoft Copilot

## Project overview
This is a small Python project that manages dramas and genres using an SQLite database. Key modules:
- `models.py` — domain models (data classes) for Drama and Genre.
- `services.py` — data access and business logic (CRUD + validation).
- `README.md` — this document.

## Database schema (summary)
- Table: `genres`
  - `genre_id` (PK)
  - `name` (TEXT)
- Table: `dramas`
  - `drama_id` (PK)
  - `title` (TEXT) — required
  - `year` (INTEGER) — required
  - `episodes` (INTEGER) — required
  - `genre_id` (FK -> `genres.genre_id`) — required
  - `deleted` (BOOLEAN) — default false

## `models.py` (classes)
Two domain classes represent rows in the database:

- `Genre`
  - Attributes:
    - `genre_id: int`
    - `name: str`

- `Drama`
  - Attributes:
    - `drama_id: int`
    - `title: str` (required)
    - `year: int` (required)
    - `episodes: int` (required)
    - `genre: Union[int, Genre]` (can be an integer id or a `Genre` instance)
    - `deleted: bool` (default `False`)

### UML diagram showing the relationship (Drama -> Genre):

![uml diagram](UML%20class.png)

## `services.py` (summary of responsibilities)
- get_drama(drama_id: int) -> Optional[Drama]
  - SQL: joins `dramas` and `genres` to return a single Drama with its genre.
  - Important: calls `c.fetchone()` (not `c.fetchone`) and maps the row into a `Drama` object via `make_drama`.

- get_genre(genre_id: int) -> Optional[Genre]
  - SQL: selects from `genres` by `genre_id`.
  - Uses `c.fetchone()` and `make_genre` to construct a `Genre`.

- add_drama(drama: Drama) -> None
  - Validates required fields: `title`, `year`, `episodes`, and `genre`.
  - Resolves `genre_id` whether `drama.genre` is an `int` or an object (`.id` or `.genre_id`).
  - Inserts into `dramas` with parameters for `(title, year, episodes, genre_id, deleted)`.
  - Handles `commit` and `rollback` on errors; raises exceptions upward.

Example validation rules implemented:
- If `drama.genre` is `None` or cannot resolve to an int, raise `ValueError("drama genre id is required")`.
- If `title`, `year`, or `episodes` are missing, raise corresponding `ValueError`.
