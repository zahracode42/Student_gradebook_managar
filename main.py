from os import name

from assessment import Assessment
from student import Student
from course import Course
from quiz import Quiz
from exam import Exam
from gradebook import GradeBook

gradebook = GradeBook()
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
        student_id = int(input("Enter student ID: "))
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
        pass

    elif choice == "4":
        pass

    elif choice == "5":
        pass

    elif choice == "6":
        pass

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
        print("\n" * 2)
