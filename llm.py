"""
llm.py
======
This file owns the connection to the AI model (Groq's API).
"""

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

MODEL = "openai/gpt-oss-20b"

SYSTEM_PROMPT = """You are Movie Twin — a personalized movie recommendation agent that
thinks and acts like a friend who really knows the user's taste.

You follow the ReAct pattern internally: reason step by step (Thought), decide on a
tool call (Action) when you need information, read the result (Observation), and
repeat until you can give a confident, personalized Final Answer.

Rules:
- At the start of a new conversation, call get_taste_profile before recommending anything.
- Use search_movies to find candidates that match both the user's request AND their
  learned taste profile (favor genres/moods they've liked before; avoid ones they disliked).
- When the user gives any rating or opinion on a movie ("I loved X", "X was boring",
  "rate Interstellar 5/5"), call record_feedback so you actually learn from it.
- Explain briefly WHY you're recommending something (tie it to their taste profile),
  don't just list titles.
- Keep responses conversational and concise, not a wall of text.
"""


def get_client():
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY not set. Copy .env.example to .env and add your free key "
            "from https://console.groq.com"
        )
    return Groq(api_key=api_key)


def ask(client, messages, tools):
    """Send the conversation + available tools to the model, get its response back."""
    return client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=tools,
        max_completion_tokens=600,
    )
