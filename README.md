# Academic Record Helper

This is a small terminal program I made for my VITyarthi project
assignment. It helps a faculty member add, view, search, update and
delete student marks, and it works out averages and the topper by
itself instead of doing it by hand.

## Overview

I made this because I've seen my friends and faculty spend time
calculating averages and finding the topper manually, and sometimes get
it wrong when two students end up with the same average. This program
just keeps the marks, does the average calculation for you, and tells
you the topper - and if there's a tie, it shows all the students who
are tied instead of picking one randomly.

It also saves the records to a file, so you don't lose everything when
you close the program (this was one of the things I had to fix after
my first submission - originally it only kept records in memory).

## Features

-Add a student with two subject marks
-View all students along with their average
-Find the topper (shows everyone if there's a tie)
-Search for a student by name - works even if you type the name in a
  different case, like "akshun" instead of "Akshun"
-Update a student's marks
-Delete a student
-Records are saved to `student_records.json` automatically and loaded
  back the next time you run it

## Technologies / Tools Used

-Python 3 (no extra packages needed, just the standard library)
-`json` for saving/loading the records
-`unittest` for the tests
-Graphviz to draw the diagrams in `docs/diagrams/`

## Project Structure

I split the program into a few files instead of putting everything in
one, since that got messy last time and made it harder to fix things
faculty pointed out:

```
academic_record_helper/
├── main.py            - starts the program, runs the menu
├── ui.py               - all the print statements and prompts
├── records.py          - StudentRepository class, does the actual work
├── calculations.py     - calculate_average()
├── matching.py         - find_actual_name() for case-insensitive search
├── storage.py          - saving/loading the JSON file
├── config.py           - just holds the file name setting
├── tests/
│   └── test_records.py - my tests
├── docs/
│   ├── DESIGN.md        - design write-up + diagrams
│   └── diagrams/
├── statement.md
├── requirements.txt
└── .gitignore
```

## How to Install & Run

You just need Python 3, nothing else to install.

1. Check Python is installed:
   ```
   python3 --version
   ```
2. Run it from the project folder:
   ```
   python3 main.py
   ```
3. Then just follow the menu and type a number from 1 to 7.

Your records get saved automatically in `student_records.json`, in the
same folder, and load back in next time you open the program.

## How to Run the Tests

I added tests after getting feedback that I should reuse the average
calculation properly and check the tie/case-insensitive fixes actually
work. The tests use a separate test data file so they won't mess with
your real records.

From the project folder, run:

```
python3 tests/test_records.py -v
```

All 10 should say `ok` at the end.

## Screenshots

I didn't add screenshots since it's a terminal program - there isn't
really a "screen" to screenshot, just text. A sample run is shown in
the project report instead.

## What I Learned

Breaking the program into separate files made it a lot easier to fix
things one at a time - like when I had to make the average calculation
reusable, I only had to change it in `calculations.py` instead of
finding every place I'd copy-pasted the same loop. It also made it
possible to actually write tests for each part on its own.

## Things I Can Improve Later

- Support more than two subjects
- Add a GUI instead of the terminal menu
- Add easier/harder grading modes
- Maybe password-protect the saved file
