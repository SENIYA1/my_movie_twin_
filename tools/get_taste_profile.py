"""
tools/get_taste_profile.py
============================
Tool #2: reads what's been learned about the user so far (memory.py).
"""

from memory import get_taste_profile as _get_taste_profile

SCHEMA = {
    "type": "function",
    "function": {
        "name": "get_taste_profile",
        "description": "Get everything learned so far about this user's taste: liked/disliked genres, liked moods, and watch history with ratings. Always call this before recommending, if you haven't already this session.",
        "parameters": {
            "type": "object",
            "properties": {"user_id": {"type": "string"}},
            "required": ["user_id"],
        },
    },
}


def get_taste_profile(user_id: str, **_):
    return _get_taste_profile(user_id)

