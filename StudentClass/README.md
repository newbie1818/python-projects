# Student Class

A simple Python class for managing a student's grades.

## Features

- Store a student's name and list of grades
- Add new grades
- Calculate average grade
- Find the highest grade

## Usage

```python
student = Student("James", [88, 90, 57, 80])

student.add_grade(95)          # adds 95 to grades list
student.get_average()          # returns 82.0
student.get_highest()          # returns 95
```

## Methods

| Method | Description | Returns |
|---|---|---|
| `add_grade(grade)` | Adds a grade to the list | Nothing |
| `get_average()` | Calculates the average of all grades | Float |
| `get_highest()` | Returns the highest grade | Int |

## Requirements

Python 3.x — no external libraries needed.