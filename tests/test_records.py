"""Some basic tests for the project.
Run with:  python3 tests/test_records.py -v
(run from the project's top-level folder, not from inside tests/)
"""

import os
import sys
import unittest

# Make the project root importable when tests are run directly.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import config
from calculations import calculate_average
from matching import find_actual_name
from records import StudentRepository


class TestCalculateAverage(unittest.TestCase):
    def test_average_of_two_marks(self):
        self.assertEqual(calculate_average([80, 90]), 85)

    def test_average_of_equal_marks(self):
        self.assertEqual(calculate_average([70, 70]), 70)


class TestFindActualName(unittest.TestCase):
    def setUp(self):
        self.records = {"Akshun": [80, 90], "Bella": [90, 80]}

    def test_matches_regardless_of_case(self):
        self.assertEqual(find_actual_name(self.records, "akshun"), "Akshun")
        self.assertEqual(find_actual_name(self.records, "AKSHUN"), "Akshun")

    def test_returns_none_when_not_found(self):
        self.assertIsNone(find_actual_name(self.records, "Charlie"))


class TestStudentRepository(unittest.TestCase):
    def setUp(self):
        # Use a throwaway data file so tests never touch real records.
        self.original_data_file = config.DATA_FILE
        config.DATA_FILE = "test_student_records.json"
        if os.path.exists(config.DATA_FILE):
            os.remove(config.DATA_FILE)
        self.repo = StudentRepository()

    def tearDown(self):
        if os.path.exists(config.DATA_FILE):
            os.remove(config.DATA_FILE)
        config.DATA_FILE = self.original_data_file

    def test_add_and_search_student(self):
        success, message = self.repo.add_student("Akshun", 80, 90)
        self.assertTrue(success)
        result = self.repo.search_student("akshun")
        self.assertIsNotNone(result)
        name, marks, average = result
        self.assertEqual(name, "Akshun")
        self.assertEqual(average, 85)

    def test_cannot_add_duplicate_student(self):
        self.repo.add_student("Akshun", 80, 90)
        success, message = self.repo.add_student("akshun", 50, 50)
        self.assertFalse(success)

    def test_topper_with_a_tie(self):
        self.repo.add_student("Akshun", 80, 90)
        self.repo.add_student("Bella", 90, 80)
        highest_average, toppers = self.repo.find_topper()
        self.assertEqual(highest_average, 85)
        self.assertEqual(sorted(toppers), ["Akshun", "Bella"])

    def test_update_marks_is_case_insensitive(self):
        self.repo.add_student("Bella", 90, 80)
        actual_name = self.repo.update_marks("bella", 85, 85)
        self.assertEqual(actual_name, "Bella")
        self.assertEqual(self.repo.records["Bella"], [85, 85])

    def test_delete_student_is_case_insensitive(self):
        self.repo.add_student("Akshun", 80, 90)
        deleted_name = self.repo.delete_student("AKSHUN")
        self.assertEqual(deleted_name, "Akshun")
        self.assertEqual(self.repo.records, {})

    def test_records_persist_after_reload(self):
        self.repo.add_student("Akshun", 80, 90)
        reloaded_repo = StudentRepository()
        self.assertIn("Akshun", reloaded_repo.records)


if __name__ == "__main__":
    unittest.main()
