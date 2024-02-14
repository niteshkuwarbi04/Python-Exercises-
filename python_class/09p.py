'''
9. Write a Python class named Student with two attributes student_name, marks. Modify the attribute values of the said 
   class and print the original and modified values of the said attributes.'''

class student:
    def __init__(self,std_name,marks):
        self.std_name = std_name
        self.marks = marks

std_instance = student('Vivek Singh', 70)

print("Original Values")
print("Student Name: ", std_instance.std_name)
print("Student Marks: ", std_instance.marks)

# Modifying attribute values
std_instance.std_name = "Vivek Singh Rawat"
std_instance.marks = 80

# Print modified values
print("\nModified values:")
print("Student Name:", std_instance.std_name)
print("Marks:", std_instance.marks)
