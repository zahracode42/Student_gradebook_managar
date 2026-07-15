class Course:
    def __init__(self,course_code,course_name):
        self.course_code = course_code
        self.course_name = course_name
        self.students = []
        self.assessments = []


    def add_student(self,student_id):
        if student_id not in self.students:
            self.students.append(student_id)
        else:
            print("Student is already enrolled.")