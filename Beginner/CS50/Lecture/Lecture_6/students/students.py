## Initial version.

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name[0]} is in {house[1]}")

## Sorted version.

students = []

with open ("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student ["name"] = name
        student["house"] = house
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")

## Updated version of sorted version. with a key used in order to sort.

students = []

with open ("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")


## other version with pass key called a lambda.

students = []

with open ("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students = {"name": name, "house": house}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]): # lambda key
    print(f"{student['name']} is in {student['house']}")

## Version with second list with studen addresses instead of name of House. with csv libraries to bypass "3 commas" probelm on the list.

import csv

students = []

with open ("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({name: row[0], "home": row[1]})

for student in sorted(students, key=lambda student: student["name"]): 
    print(f"{student['name']} is in {student['home']}")

## Version in using a DictReader. this is more robust version name and home as header so to speak.

import csv

students = []

with open ("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({name: row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]): 
    print(f"{student['name']} is in {student['home']}")