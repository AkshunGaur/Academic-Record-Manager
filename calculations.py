"""This is where I calculate the average marks. I made it a separate
function because I was repeating the same loop in three different
places before (view, find topper, search) - now they all just call this.
"""


def calculate_average(marks):
    """Takes a list of marks (like [80, 90]) and gives back the average."""
    total = 0
    count = 0
    for m in marks:
        total = total + m
        count = count + 1
    return total / count
