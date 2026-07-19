
class Student:
    def __init__(self, student_id, name, email):
        self.__student_id = student_id
        self.__name = name
        self.email = email
        self.courses = []

    def get_id(self):
        return self.__student_id
    def get_name(self):
        return self.__name


    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        if "@" in email:
            self.__email = email
            print("Email updated:)")
        else:
            self.__email = None

    def enroll_course(self, course_code):
        self.courses.append(course_code)


    def display_info(self):
        print(f"Student ID: {self.__student_id}")
        print(f"Name: {self.__name}")
        print(f"Email: {self.__email}")
        print(f"Enrolled courses: {len(self.courses)}")
        #this part will complete after creating class "Course"


