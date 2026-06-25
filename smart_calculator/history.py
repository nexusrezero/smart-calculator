# HISTORY STORAGE MODULE
# Handles saving/loading data

import os

HISTORY_FILE = "history.txt"

def load_history():
   # loads previous calculation history
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    return []

def save_history(item):
    # saves new entry to file
    with open(HISTORY_FILE, "a") as f:
        f.write(item + "\n")

def clear_history():
   # clears all history data
    open(HISTORY_FILE, "w").close()
