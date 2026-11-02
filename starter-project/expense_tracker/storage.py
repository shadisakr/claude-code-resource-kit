import json
import os

DEFAULT_PATH = "expenses.json"


def load(path=DEFAULT_PATH):
    """Return the list of saved expenses."""
    if not os.path.exists(path):
        return []
    with open(path) as f:
        return json.load(f)


def save(expenses, path=DEFAULT_PATH):
    with open(path, "w") as f:
        json.dump(expenses, f, indent=2)
