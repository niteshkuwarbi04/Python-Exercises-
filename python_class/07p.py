'''
7. Write a simple Python class named Student and display its type. Also, display the __dict__ attribute keys and the value
   of the __module__ attribute of the Student class.'''

class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

# Creating an instance of the Student class
student_instance = Student(1, "Vivek Singh", "BCA")

# This will display the type of the Student class
print("Type of Student class:", type(Student))

# Display the __dict__ attribute keys of the Student instance
print("__dict__ attribute keys:", student_instance.__dict__.keys())

# Display the value of the __module__ attribute of the Student class
print("__module__ attribute:", Student.__module__)

