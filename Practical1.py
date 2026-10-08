import math
import numpy as np
import zipfile 
import os.path
import csv
import pandas as po

students = []
courses = []
marks = {}
f = open("students.csv", "w", newline="")
t = open("courses.csv", "w", newline="")
m = open("marks.csv", "w", newline="")
def input_in4():
    #get the information of courses and students
    n = int(input("The number of the student in a class: "))
    c = int(input("The number of the courses: "))
    
    for i in range(n):
        id = int(input("student ID: "))
        name = (input("The name: "))
        DoB = (input("dd/mm/yy: " ))
        student = {'id': id,
                   'name': name,
                   'DoB': DoB}
        students.append(student)
    for i in range(c):
        id_c = int(input("ID Course:" ))
        name_c = (input("The course:"))
        credit = int(input("The credit of the course:"))
        course = {'id': id_c,
                  "name": name_c,
                  'credit': credit}
        courses.append(course)

def list_students():

    writer = csv.writer(f)

    writer.writerow(["id", "name", "DoB"])
    print("---Information of Students---")

    for student in students:

        writer.writerow([
            student['id'],
            student['name'],
            student['DoB']
        ])
        
        print(
            'ID student',
            student['id'],
            student['name'],
            student['DoB']
        )
        
def list_courses():

    writer = csv.writer(t)

    writer.writerow(["id", "name", "credit"])
    print("---Information of COurses---")

    for course in courses:

        writer.writerow([
            course['id'],
            course['name'],
            course['credit']
        ])

        print(
            'ID Course',
            course['id'],
            ':',
            course['name']
        )
        
def mark_id():
    #get mark and select mark for the student

    for course in courses:

        course_id = course['id']

        print("\nEnter marks for course:", course['name'])

        marks[course_id] = {}

        for student in students:

            mark = float(
                input(
                    "Enter mark for ID_Student: "
                    + str(student['id'])
                    + ": "
                )
            )

            marks[course_id][student['id']] = math.floor(mark * 10) / 10

        
def show_marks():

    course_id = int(input("Enter ID Course: "))

    if course_id in marks:

        for student in students:

            student_id = student['id']

            if student_id in marks[course_id]:

                print(
                    'The mark of the student',
                    student['name'],
                    ":",
                    marks[course_id][student_id]
                )

    else:
        print("No marks")

    # Export marks to CSV
    writer = csv.writer(m)

    writer.writerow([
        "CourseID",
        "StudentID",
        "Mark"
    ])

    for course_id in marks:

        for student_id in marks[course_id]:

            writer.writerow([
                course_id,
                student_id,
                marks[course_id][student_id]
            ])
            
def calculate_gpa(student_id):
    mark_list = []
    credit_list = []

    for course in courses:
        course_id = course['id']
        credit = course['credit']

        if course_id in marks and student_id in marks[course_id]:
            mark = marks[course_id][student_id]

            mark_list.append(mark)
            credit_list.append(credit)

    if len(credit_list) > 0:

        marks_array = np.array(mark_list)
        credits_array = np.array(credit_list)

        total_weighted_marks = np.sum(marks_array * credits_array)
        total_credits = np.sum(credits_array)

        gpa = total_weighted_marks / total_credits

        return round(gpa, 2)

    else:
        return None

def calculate_all_gpas():
    gpa_array = []

    for student in students:
        student_id = student['id']
        gpa = calculate_gpa(student_id)

        if gpa is not None:
            gpa_array.append((student_id, student['name'], gpa))
            print(f"GPA of {student['name']}: {gpa}")

    return gpa_array

def sort_students_by_gpa():

    for student in students:
        student['gpa'] = calculate_gpa(student['id'])

    students.sort(
        key=lambda student: student['gpa'],
        reverse=True
    )

    print("Students sorted by GPA (highest to lowest):")

    for student in students:
        print(
            student['id'],
            student['name'],
            ":",
            student['gpa']
        )



#run modules
input_in4()
list_students()
list_courses()
mark_id()
show_marks()
calculate_all_gpas()
sort_students_by_gpa()
f.close()
t.close()
m.close()

students_df = po.read_csv("students.csv")
courses_df = po.read_csv("courses.csv")
marks_df = po.read_csv("marks.csv")

print(students_df)
print(courses_df)
print(marks_df)

print("\n--- Students DataFrame ---")
print(students_df)

print("\n--- Courses DataFrame ---")
print(courses_df)

print("\n--- Marks DataFrame ---")
print(marks_df)


with zipfile.ZipFile('students.dat', 'w') as zipf:
    zipf.write('students.csv')
    zipf.write('courses.csv')
    zipf.write('marks.csv')

if os.path.exists('students.dat'):
    print("The file students.dat has been created successfully.")
else:
    print("Failed to create the file students.dat.")

    

