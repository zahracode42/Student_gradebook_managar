class GradeBook:
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

    def record_grade(self, student_id, course_code, assessment_title, score):
        if student_id not in self.students:
            print("Student not found.")
            return
        if course_code not in self.courses:
            print("Course not found.")
            return
        course = self.courses[course_code]
        assessment = course.find_assessment(assessment_title)
        if assessment is None:
            print("Assessment not found.")
            return
        if not 0 <= score <= assessment.max_score:
            print("Invalid score.")
            return
        if student_id not in self.grades:
            self.grades[student_id] = {}

        if course_code not in self.grades[student_id]:
            self.grades[student_id][course_code] = {}

        self.grades[student_id][course_code][assessment_title] = score

    def calculate_average(self, student_id, course_code):
        if student_id not in self.grades:
            print("Student has no grades.")
            return
        if course_code not in self.grades[student_id]:
            print("Course has no grades.")
            return

        scores = []
        for assessment in self.grades[student_id][course_code]:
            scores.append(self.grades[student_id][course_code][assessment])
        average = sum(scores) / len(scores)
        return average

    def show_report(self, student_id):
        if student_id not in self.grades:
            print("Student has no grades.")
            return
        student = self.students[student_id]
        print(f"Student ID: {student.get_id()}")
        print(f"Student Name: {student.get_name()}")
        print(f"Email: {student.email}")
        for course_code in self.grades[student_id]:
            print(f"\nCourse: {course_code}")
            print("Grades:")
            for assessment_title in self.grades[student_id][course_code]:
                score = self.grades[student_id][course_code][assessment_title]
                print(f"{assessment_title}: {score}")

            average = self.calculate_average(student_id, course_code)
            print(f"Average: {average}")
            #TODO-1 update after creating get_result method
            #TODO-2 update after creating letter grades

    def search_student(self, keyword):
        for student in self.students.values():
            if student.get_id() == keyword:
                return student
            elif student.get_name() == keyword:
                return student
        print("Student not found.")
        return None

    def delete_student(self, student_id):
        if student_id not in self.students:
            print("Student not found.")
            return
        del self.students[student_id]
        if student_id in self.grades:
            del self.grades[student_id]

