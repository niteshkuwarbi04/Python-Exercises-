'''
11. Write a Python class named Student with two attributes: student_id, student_name. 
    Add a new attribute: student_class. 
    Create a function to display all attributes and their values in the Student class.'''

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = None  # Adding a new attribute with an initial value of None

    def display_attributes(self):
        print("Student ID:", self.student_id)
        print("Student Name:", self.student_name)
        print("Student Class:", self.student_class)

# Create an instance of the Student class
student_instance = Student(1, "Nitesh Kuwarbi")

# Display all attributes and their values using the display_attributes function
print("Original attributes and values:")
student_instance.display_attributes()

# Add a new value for the student_class attribute
student_instance.student_class = "Grade 10"

# Display all attributes and their values after adding student_class
print("\nAttributes and values after adding student_class:")
student_instance.display_attributes()
