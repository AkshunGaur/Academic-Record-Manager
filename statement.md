# Project Statement

## Project Name

Academic Record Helper

## Problem Statement

Faculty usually keep track of student marks by hand and work out
averages and the topper manually. This takes time and it's easy to make
a small mistake, especially when checking who the topper is - if two
students have the same average, it's easy to just notice the first one
and miss that it's actually a tie.

## Scope

This is a terminal program for one faculty member to manage a small set
of student records - adding students and marks, viewing everyone's
average, finding the topper (including ties), searching by name,
updating marks, and deleting a record. Records are saved to a file so
they aren't lost when the program is closed.

It's not a GUI app, doesn't support multiple users, and doesn't connect
to the internet - it's just meant to run on one computer for one
faculty member at a time.

## Target Users

-Faculty who want a quick way to record and check a class's marks
  without setting up a full spreadsheet.
-Anyone learning Python who wants to see a small project split into
  separate files instead of one big script.

## High-Level Features

-Add a student's name and two marks
-View every student with their calculated average
-Find the topper, correctly handling ties
-Search for a student regardless of letter case
-Update a student's marks
-Delete a student
-Save records automatically and reload them next time
