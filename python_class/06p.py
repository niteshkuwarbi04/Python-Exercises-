'''
6. Write a Python function student_data () that will print the ID of a student (student_id). If the user passes an 
   argument student_name or student_class the function will print the student name and class.'''

def student_data(student_id, student_name=None, student_class=None):
    print("Student ID:", student_id)
    
    if student_name is not None:
        print("Student Name:", student_name)
    
    if student_class is not None:
        print("Student Class:", student_class)

# Example usage:
student_data(123)
student_data(456, student_name="Vivek Singh")
student_data(789, student_class="Mathematics")
student_data(101, student_name="Akanksha Joshi", student_class="Computer Science")

