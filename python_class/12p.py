'''
12. Write a Python class named Student with two instances student1, student2 and assign values to the instances' attributes. 
    Print all the attributes of the student1, student2 instances with their values in the given format.'''

class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

# Create instances of the Student class
student1 = Student(1, "Nitesh Kuwarbi", "Grade 10")
student2 = Student(2, "Nitesh Kuwarbi", "Grade 11")

# Print attributes and values for student1
print("Student 1 attributes and values:")
print(f"Student ID: {student1.student_id}")
print(f"Student Name: {student1.student_name}")
print(f"Student Class: {student1.student_class}")

# Print attributes and values for student2
print("\nStudent 2 attributes and values:")
print(f"Student ID: {student2.student_id}")
print(f"Student Name: {student2.student_name}")
print(f"Student Class: {student2.student_class}")
