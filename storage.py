"""This file takes care of saving and loading the records from the JSON
file. I kept it separate from records.py so that if I ever want to
change how saving works (or use a real database one day), I only have
to change this one file.
"""

import json
import os

import config


def load_records():
    """Loads the saved records if the file exists. If there is no file
    yet (first time running the program) or the file is broken somehow,
    it just returns an empty dictionary instead of crashing."""
    if not os.path.exists(config.DATA_FILE):
        return {}

    try:
        with open(config.DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read saved records. Starting fresh.")
        return {}


def save_records(records):
    """Saves the records dictionary to the JSON file. Returns True if it
    worked, False if something went wrong (like no permission to write)."""
    try:
        with open(config.DATA_FILE, "w") as f:
            json.dump(records, f, indent=2)
        return True
    except OSError:
        print("Warning: Could not save records to file.")
        return False
