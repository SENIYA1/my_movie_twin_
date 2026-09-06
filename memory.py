"""
memory.py
=========
This is what makes the agent "learn" the user's taste.

Each user gets a JSON file under taste_profiles/<user_id>.json. It tracks
liked/disliked genres, liked moods, and full watch history with ratings.
Because it's a file (not just a variable in RAM), the profile survives
between separate runs of the program — the agent remembers you tomorrow,
not just for this one conversation.
"""

import json
from pathlib import Path
from db import find_by_title

PROFILE_DIR = Path("./taste_profiles")
PROFILE_DIR.mkdir(exist_ok=True)


def _profile_path(user_id: str) -> Path:
    return PROFILE_DIR / f"{user_id}.json"


def _default_profile():
    return {
        "liked_genres": {},     # genre -> count
        "disliked_genres": {},
        "liked_moods": {},
        "watched": [],          # [{title, rating, note}]
    }


def get_taste_profile(user_id: str):
    """Return everything learned about this user so far, or a blank profile if new."""
    path = _profile_path(user_id)
    if not path.exists():
        return _default_profile()
    return json.loads(path.read_text())


def record_feedback(user_id: str, title: str, rating: int, note: str = ""):
    """
    Save the user's rating/reaction to a movie and update their taste profile.
    rating: 1 (disliked) to 5 (loved).
    """
    profile = get_taste_profile(user_id)
    movie = find_by_title(title)

    profile["watched"].append({"title": title, "rating": rating, "note": note})

    if movie:
        bucket = "liked_genres" if rating >= 4 else "disliked_genres" if rating <= 2 else None
        if bucket:
            for g in movie["genre"]:
                profile[bucket][g] = profile[bucket].get(g, 0) + 1
        if rating >= 4:
            for mo in movie["mood"]:
                profile["liked_moods"][mo] = profile["liked_moods"].get(mo, 0) + 1

    _profile_path(user_id).write_text(json.dumps(profile, indent=2))
    return {"status": "profile updated", "profile": profile}
