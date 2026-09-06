"""
tools/__init__.py
==================
Collects all 3 tools into one place so main.py only needs one import.
Add a 4th tool later by: creating tools/your_tool.py with SCHEMA + function,
then adding both lines below.
"""

from .search_movies import SCHEMA as SEARCH_MOVIES_SCHEMA, search_movies
from .get_taste_profile import SCHEMA as GET_TASTE_PROFILE_SCHEMA, get_taste_profile
from .record_feedback import SCHEMA as RECORD_FEEDBACK_SCHEMA, record_feedback

TOOLS = [SEARCH_MOVIES_SCHEMA, GET_TASTE_PROFILE_SCHEMA, RECORD_FEEDBACK_SCHEMA]

TOOL_FUNCTIONS = {
    "search_movies": search_movies,
    "get_taste_profile": get_taste_profile,
    "record_feedback": record_feedback,
}

