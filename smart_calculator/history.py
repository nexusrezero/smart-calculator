import os

HISTORY_FILE = "history.txt"

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    return []

def save_history(item):
    with open(HISTORY_FILE, "a") as f:
        f.write(item + "\n")

def clear_history():
    open(HISTORY_FILE, "w").close()