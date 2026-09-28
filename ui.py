"""All the print statements and input prompts are here. I kept them
separate from records.py so I can change the wording of a message
without having to dig through the actual logic.
"""

TITLE = "Academic Record Helper"


def welcome():
    print("\n", "\n", "\n")
    print(TITLE.center(80, "*"))


def print_menu():
    print("STUDENT MENU")
    print("====================")
    print("1. Add a student")
    print("2. View all students and averages")
    print("3. Find the topper")
    print("4. Search for a student")
    print("5. Update student marks")
    print("6. Delete a student")
    print("7. Exit program")


def get_choice():
    return input("Enter your choice (1-7): ").strip()


def get_marks_input(first_prompt, second_prompt):
    """Reads two marks from the user. Returns (mark1, mark2) or None if
    either value entered was not a valid number."""
    try:
        mark1 = float(input(first_prompt))
        mark2 = float(input(second_prompt))
        return mark1, mark2
    except ValueError:
        return None


def show_report_row(name, marks, average):
    print("Name:", name, "| Marks:", marks, "| Average:", average)


def show_topper(highest_average, toppers):
    if len(toppers) == 1:
        print("Top Performer:", toppers[0], "with average:", highest_average)
    else:
        print(
            "Top Performers (tied):", ", ".join(toppers),
            "with average:", highest_average,
        )
