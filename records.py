"""Everything to do with adding,
viewing, searching, updating and deleting students happens here. It
doesn't calculate averages or match names itself - it just calls the
functions from calculations.py and matching.py for that, and calls
storage.py whenever something needs to be saved.
"""

from calculations import calculate_average
from matching import find_actual_name
from storage import load_records, save_records


class StudentRepository:
    """Keeps all the student records in one dictionary and has a method
    for each menu option. Saves to the file every time something changes,
    so nothing is lost if the program is closed."""

    def __init__(self):
        self.records = load_records()

    def add_student(self, name, mark1, mark2):
        """Adds a new student. Returns (success, message)."""
        name = name.strip()
        if name == "":
            return False, "Error: Name cannot be blank."
        if find_actual_name(self.records, name) is not None:
            return False, "Error: Student already exists."

        self.records[name] = [mark1, mark2]
        save_records(self.records)
        return True, "Success: Student saved!"

    def all_students(self):
        """Returns a list of (name, marks, average) for every student."""
        report = []
        for name, marks in self.records.items():
            report.append((name, marks, calculate_average(marks)))
        return report

    def find_topper(self):
        """Returns (highest_average, [names]).

        More than one name is returned when students are tied for the
        highest average, so ties are never hidden.
        """
        if not self.records:
            return None, []

        highest_average = -1
        toppers = []

        for name, marks in self.records.items():
            average = calculate_average(marks)

            if average > highest_average:
                highest_average = average
                toppers = [name]
            elif average == highest_average:
                toppers.append(name)

        return highest_average, toppers

    def search_student(self, name):
        """Returns (actual_name, marks, average), or None if not found."""
        actual_name = find_actual_name(self.records, name)
        if actual_name is None:
            return None
        marks = self.records[actual_name]
        return actual_name, marks, calculate_average(marks)

    def update_marks(self, name, mark1, mark2):
        """Updates a student's marks. Returns the actual stored name, or
        None if the student was not found."""
        actual_name = find_actual_name(self.records, name)
        if actual_name is None:
            return None

        self.records[actual_name] = [mark1, mark2]
        save_records(self.records)
        return actual_name

    def delete_student(self, name):
        """Deletes a student. Returns the actual stored name that was
        deleted, or None if the student was not found."""
        actual_name = find_actual_name(self.records, name)
        if actual_name is None:
            return None

        del self.records[actual_name]
        save_records(self.records)
        return actual_name
