## Lists

## initial simple version

#students = ["Hermoine", "Harry", "Ron"]
#
#print(students[0])
#print(students[1])
#print(students[2])

## other with for loop version

#students = ["Hermoine", "Harry", "Ron"]
#
#for students in students:
#    print(students)

## version with function len (lenght)

#students = ["Hermoine", "Harry", "Ron"]
#
#for i in range(len(students)):
#    print(i + 1, students[i])

## version using dict (dictionary)

#students = ["Hermoine", "Harry", "Ron", "Draco"]
#house = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
#
#students = {
#    "Hermione": "Gryffindor",
#    "Harry": "Gryffindor",
#    "Ron": "Gryffindor",
#    "Draco": "Slytherin",
#}
#
#for student in students:
#    print(student, students[student], sep=", ")

## updated version with keyword "none"

students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ") 