subjects = {
    'math': {'George': 85, 'Salome': 78, 'David': 92},
    'physics': {'George': 90, 'David': 75, 'Salome': 88},
    'chemistry': {'David': 82, 'George': 80, 'Salome': 91}
}

students = {}

for subject_name, grades in subjects.items():
    for student_name, grade in grades.items():
        if student_name not in students:
            students[student_name] = {}
        students[student_name][subject_name] = grade


print(students)

