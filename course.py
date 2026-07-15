class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name
        self.students = []
        self.assessments = []


    def add_student(self, student_id):
        if student_id not in self.students:
            self.students.append(student_id)
        else:
            print("Student is already enrolled.")

    def add_assessment(self, assessment):
        self.assessments.append(assessment)
        # This part will be completed after creating class "Assessment"

    #TODO: Create find_assessment() after creating the Assessment Class


    def display_info(self):
        print(f"Course Code: {self.course_code}")
        print(f"Course Name: {self.course_name}")
        print(f"Enrolled Students: {len(self.students)}")
        # This part will be completed after creating class "Assessment"