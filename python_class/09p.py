'''
9. Write a Python class named Student with two attributes student_name, marks. Modify the attribute values of the said 
   class and print the original and modified values of the said attributes'''

class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

# Creatimg an instance of the Student class
student_instance = Student("Nitesh Kuwarbi", 75)

print("Original values:")
print("Student Name:", student_instance.student_name)
print("Marks:", student_instance.marks)

# Modifying attribute values
student_instance.student_name = "Nitesh Kuwarbi"
student_instance.marks = 85

# Print modified values
print("\nModified values:")
print("Student Name:", student_instance.student_name)
print("Marks:", student_instance.marks)
