"""
db.py
=====
This is the movie "database" for the project.

It's a plain in-memory list of dicts right now (12 sample movies) so the
project runs with zero setup. Swap MOVIE_CATALOG for a real query
(SQLite, Postgres, a TMDB API call, etc.) later without touching any
other file — every tool imports from here, never hardcodes movie data.
"""

MOVIE_CATALOG = [
    {"title": "Interstellar", "genre": ["sci-fi", "drama"], "mood": ["thoughtful", "epic"], "year": 2014, "director": "Christopher Nolan", "rating": 8.7},
    {"title": "The Grand Budapest Hotel", "genre": ["comedy", "drama"], "mood": ["quirky", "light"], "year": 2014, "director": "Wes Anderson", "rating": 8.1},
    {"title": "Parasite", "genre": ["thriller", "drama"], "mood": ["dark", "tense"], "year": 2019, "director": "Bong Joon-ho", "rating": 8.5},
    {"title": "La La Land", "genre": ["romance", "musical"], "mood": ["dreamy", "bittersweet"], "year": 2016, "director": "Damien Chazelle", "rating": 8.0},
    {"title": "Mad Max: Fury Road", "genre": ["action", "sci-fi"], "mood": ["intense", "adrenaline"], "year": 2015, "director": "George Miller", "rating": 8.1},
    {"title": "Coco", "genre": ["animation", "family"], "mood": ["heartwarming"], "year": 2017, "director": "Lee Unkrich", "rating": 8.4},
    {"title": "Whiplash", "genre": ["drama", "music"], "mood": ["intense", "tense"], "year": 2014, "director": "Damien Chazelle", "rating": 8.5},
    {"title": "Knives Out", "genre": ["mystery", "comedy"], "mood": ["fun", "clever"], "year": 2019, "director": "Rian Johnson", "rating": 7.9},
    {"title": "Arrival", "genre": ["sci-fi", "drama"], "mood": ["thoughtful", "quiet"], "year": 2016, "director": "Denis Villeneuve", "rating": 7.9},
    {"title": "Everything Everywhere All at Once", "genre": ["sci-fi", "comedy"], "mood": ["chaotic", "heartwarming"], "year": 2022, "director": "Daniels", "rating": 7.8},
    {"title": "The Dark Knight", "genre": ["action", "thriller"], "mood": ["intense", "dark"], "year": 2008, "director": "Christopher Nolan", "rating": 9.0},
    {"title": "Amelie", "genre": ["romance", "comedy"], "mood": ["quirky", "light"], "year": 2001, "director": "Jean-Pierre Jeunet", "rating": 8.3},
]


def find_by_title(title: str):
    """Look up a single movie by exact (case-insensitive) title. Used by memory.py."""
    return next((m for m in MOVIE_CATALOG if m["title"].lower() == title.lower()), None)
