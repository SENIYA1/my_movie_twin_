"""
tools/record_feedback.py
==========================
Tool #3: saves a rating/reaction and updates the taste profile (memory.py).
This is the tool that makes the agent "learn."
"""

from memory import record_feedback as _record_feedback

SCHEMA = {
    "type": "function",
    "function": {
        "name": "record_feedback",
        "description": "Save the user's rating/reaction to a movie so the agent learns their taste for future recommendations. Call this whenever the user rates, praises, or criticizes a movie.",
        "parameters": {
            "type": "object",
            "properties": {
                "user_id": {"type": "string"},
                "title": {"type": "string"},
                "rating": {"type": "integer", "description": "1 (disliked) to 5 (loved)"},
                "note": {"type": "string", "description": "optional short reason"},
            },
            "required": ["user_id", "title", "rating"],
        },
    },
}


def record_feedback(user_id: str, title: str, rating: int, note: str = "", **_):
    return _record_feedback(user_id, title, rating, note)

