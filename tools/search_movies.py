"""
tools/search_movies.py
=======================
Tool #1: searches the movie catalog (db.py) by genre, mood, keyword, or year.
"""

from db import MOVIE_CATALOG

SCHEMA = {
    "type": "function",
    "function": {
        "name": "search_movies",
        "description": "Search the movie catalog by genre, mood, keyword (title/director), and/or minimum year. Leave a field empty/omit it to ignore that filter.",
        "parameters": {
            "type": "object",
            "properties": {
                "genre": {"type": "string", "description": "e.g. sci-fi, comedy, drama"},
                "mood": {"type": "string", "description": "e.g. thoughtful, intense, heartwarming, dark"},
                "keyword": {"type": "string", "description": "matches title or director"},
                "min_year": {"type": "integer", "description": "only movies released this year or later"},
            },
        },
    },
}


def search_movies(genre: str = "", mood: str = "", keyword: str = "", min_year: int = 0, **_):
    """Search the catalog. All filters are optional and case-insensitive."""
    results = []
    for m in MOVIE_CATALOG:
        if genre and genre.lower() not in [g.lower() for g in m["genre"]]:
            continue
        if mood and mood.lower() not in [x.lower() for x in m["mood"]]:
            continue
        if keyword and keyword.lower() not in m["title"].lower() and keyword.lower() not in m["director"].lower():
            continue
        if m["year"] < min_year:
            continue
        results.append(m)
    return results if results else [{"info": "no matches found in catalog"}]

