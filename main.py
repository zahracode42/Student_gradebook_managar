from os import name

from assessment import Assessment
from project import Project
from student import Student
from course import Course
from quiz import Quiz
from exam import Exam
from gradebook import GradeBook

gradebook = GradeBook()

student = Student("s001", "Ahmad", "ahmad@gmail.com")
gradebook.add_student(student)

course = Course("cs101", "Python")
gradebook.add_course(course)

gradebook.enroll_student("s001", "cs101")
running_main_menu = True
while running_main_menu:
    print("==== *Student Gradebook Manager* ====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Add Course")
    print("4. Enroll Student in Course")
    print("5. Add Assessment")
    print("6. Record Grade")
    print("7. View Student Report")
    print("8. Search Student")
    print("9. Delete Student")
    print("0. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")

        valid_email = False
        while not valid_email:
            email = input("Enter student email: ")
            student = Student(student_id, name, email)
            if student.email is None:
                print("Invalid email!")
            else:
                valid_email = True
        gradebook.add_student(student)


    elif choice == "2":
        gradebook.view_students()

    elif choice == "3":
        course_code = input("Enter course code: ")
        title = input("Enter course title: ")

        course = Course(course_code, title)
        gradebook.add_course(course)

    elif choice == "4":
        student_id = input("Enter student ID: ")
        course_id = input("Enter course code: ")
        gradebook.enroll_student(student_id, course_id)

    elif choice == "5":
        course_code = input("Enter course code: ")
        print("1. Quiz \n2. Exam \n3. Project")
        assessment_type = input("Choose assessment type: ")
        title = input("Enter assessment title: ")
        max_score = int(input("Enter max score: "))
        if assessment_type == "1":
            assessment = Quiz(title, max_score)
        elif assessment_type == "2":
            assessment = Exam(title, max_score)
        elif assessment_type == "3":
            assessment = Project(title, max_score)
        else :
            print("Invalid assessment type. Only choose one of the options.")
        if assessment_type in ["1", "2", "3"]:
            gradebook.add_assessment(course_code, assessment)
            print("Assessment added successfully!")
    elif choice == "6":
        student_id = input("Enter student ID: ")
        course_code = input("Enter course code: ")
        assessment_title = input("Enter assessment title: ")
        score = int(input("Enter score: "))
        gradebook.record_grade(student_id, course_code, assessment_title, score)
        print("Grade recorded successfully")
        print(gradebook.grades)

    elif choice == "7":
        pass

    elif choice == "8":
        pass

    elif choice == "9":
        pass

    elif choice == "0":
        print("Goodbye!")
        running_main_menu = False

    else:
        print("Invalid choice. You can *only* choose one of the options.")

    if running_main_menu:
        input("Press Enter to continue...")
        print("\n" * 2)
