import json
import os

EXIT_KEYWORDS = {"exit", "quit", "bye", "goodbye", "stop"}

def is_exit_command(text: str) -> bool:
    return any(word in text.lower() for word in EXIT_KEYWORDS)

def save_candidate_data(info: dict, questions: dict, path="candidates.json"):
    data = {"info": info, "questions": questions}
    if os.path.exists(path):
        with open(path, "r") as f:
            try:
                all_data = json.load(f)
            except json.JSONDecodeError:
                all_data = []
    else:
        all_data = []

    all_data.append(data)
    with open(path, "w") as f:
        json.dump(all_data, f, indent=2)
