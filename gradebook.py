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
