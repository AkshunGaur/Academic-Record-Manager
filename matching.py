"""This fixes the problem where searching for "akshun" wouldn't find "Akshun"
because Python treats them as different strings.
"""


def find_actual_name(records, name_to_find):
    """Goes through the records and checks each name in lowercase, so it
    doesn't matter what case the user typed. Still returns the name the
    way it was originally saved (so it prints as "Akshun", not "akshun").
    Returns None if nobody matches."""
    for stored_name in records:
        if stored_name.lower() == name_to_find.lower():
            return stored_name
    return None
