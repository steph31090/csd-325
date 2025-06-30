# Stephanie Ramos
# June 29, 2025
# Module 8.2 Assignment: JSON Practice

# This code reads student data from a JSON file, adds a new student, prints both lists, and updates the file.

import json

with open('student.json', 'r') as file:
    students = json.load(file)

def print_students(student_list):
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']}, Email = {student['Email']}")

print("Original Student List: \n")
print_students(students)

new_student = {
    "F_Name": "Stephanie",
    "L_Name": "Ramos",
    "Student_ID": 25415,
    "Email": "slramos310@gmail.com"
}
students.append(new_student)

print("\nUpdated Student List: \n")
print_students(students)

with open('student.json', 'w') as file:
    json.dump(students, file, indent=4)

print("\nNew student added successfully!")