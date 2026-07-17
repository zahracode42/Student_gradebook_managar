class Gradebook:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.grades = {}
        self.passing_grade = 55

    def add_student(self, student):
        if student.get_id() not in self.students:
            self.students[student.get_id()] = student
        else:
            print("Student already exists")

    def add_course(self, course):
        if course.course_code not in self.courses:
            self.courses[course.course_code] = course
        else:
            print("Course already exists")

    def enroll_student(self, student_id , course_code):
        if student_id in self.students and course_code in self.courses:
            student = self.students[student_id]
            course = self.courses[course_code]

            student.enroll_course(course_code)
            course.add_student(student)
        else:
            print("Student or course not exist")

    def add_assessment(self, course_code, assessment):
        if course_code in self.courses:
            course = self.courses[course_code]
            course.add_assessment(assessment)
        else:
            print("Course not exist")