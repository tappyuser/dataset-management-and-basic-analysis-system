#!/usr/bin/env python3

import re
from re import Match
from typing import TypeAlias

file_data = 'student-data.csv'

class Student:
    firstname: str
    lastname: str
    courses: list[str]
    scores: list[int]

    def __init__(self, firstname: str, lastname: str, courses: list[str], scores: list[int]):
        self.firstname = firstname
        self.lastname = lastname
        self.courses = courses
        self.scores = scores

    def average(self) -> float:
        total: int = 0
        for score in self.scores:
            total = total + score
        return total / len(self.scores)


    def minimum(self) -> int:
        minval: int = self.scores[0]
        for score in self.scores:
            if score < minval:
                minval = score
        return minval

    def maximum(self) -> int:
        maxval: int = self.scores[0]
        for score in self.scores:
            if score > maxval:
                maxval = score
        return maxval

Students: TypeAlias = list[Student]
students: Students = list()
courses: list[str] = ['ele311', 'ele321', 'ele331', 'ele361', 'ele381']
# The csv format should be
# Firstname, Lastname, Score
try:
    with open(file_data, 'r') as f:
        for index, line in enumerate(f.readlines()):
            if line != '\n' and index == 0: continue
            pattern: str = r'(\w+),(\w+),([a-zA-Z0-9\,]+)+(\n)'
            match: Match = re.match(pattern, line)
            if match is not None:
                scores: str = match.group(3)
                if not re.match(r'^(\d+)(,\d+)+', scores): raise ValueError # Ensures that the score is of type int
                firstname: str = match.group(1)
                lastname: str = match.group(2)
                courses: str = courses
                scores: list[int] = list(map(lambda x: int(x), scores.split(',')))
                student: Student = Student(firstname, lastname, courses, scores)
                students.append(student)
except FileNotFoundError:
    print(f"The file {file_data} does not exist")
except ValueError:
    print("Score should be of type int")
    
for student in students:
    print(student.scores)
    print(student.average())
    print(student.minimum())
    print(student.maximum())




           
