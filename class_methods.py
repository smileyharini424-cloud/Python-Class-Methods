class Student:

    college = "ABC College"

    def __init__(self, name, course):
        self.name = name
        self.course = course

    def display_student(self):
        print("Student Name:", self.name)
        print("Course:", self.course)

    @classmethod
    def display_college(cls):
        print("College:", cls.college)

    @staticmethod
    def welcome_message():
        print("Message: Welcome to Python OOP")

student = Student("Harini", "CSE")

student.display_student()
Student.display_college()
Student.welcome_message()
