"""
main.py
=======
Terminal entrypoint. Run this file: python main.py
"""

import json
from llm import get_client, ask, SYSTEM_PROMPT
from tools import TOOLS, TOOL_FUNCTIONS


def run_agent_turn(client, user_id, messages, user_message, verbose=True):
    """One full ReAct cycle: Thought -> Action -> Observation -> ... -> Final Answer."""
    messages.append({"role": "user", "content": user_message})

    while True:
        response = ask(client, messages, TOOLS)
        msg = response.choices[0].message
        messages.append(msg.model_dump(exclude_none=True))

        if verbose and msg.content and msg.content.strip():
            print(f"\n Movie Twin: {msg.content.strip()}")

        if not msg.tool_calls:
            break

        for tc in msg.tool_calls:
            tool_name = tc.function.name.split("<|channel|>")[0]
            fn = TOOL_FUNCTIONS[tool_name]
            args = json.loads(tc.function.arguments)
            args["user_id"] = user_id

            if verbose:
                print(f"    [Action] {tool_name}({args})")

            result = fn(**args)

            if verbose:
                print(f"    [Observation] {json.dumps(result)[:300]}")

            messages.append({
                "role": "tool",
                "tool_call_id": tc.id,
                "content": json.dumps(result),
            })

    return messages


def main():
    client = get_client()
    user_id = input("Enter your name/user id: ").strip() or "guest"
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    print(f"\nHey {user_id}! I'm Movie Twin  tell me what you're in the mood for,")
    print("or rate a movie you've seen and I'll remember it. Type 'quit' to exit.\n")

    while True:
        user_message = input("You: ").strip()
        if user_message.lower() in ("quit", "exit"):
            break
        snapshot_length = len(messages)
        try:
            messages = run_agent_turn(client, user_id, messages, user_message)
        except Exception as e:
            print(f"\n Movie Twin hit a hiccup and could not finish that reply ({e}).")
            print("   Let's try again - say that once more, or ask something else.\n")
            messages = messages[:snapshot_length]


if __name__ == "__main__":
    main()
