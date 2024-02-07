'''
6. Write a Python function student_data () that will print the ID of a student (student_id). If the user passes an 
   argument student_name or student_class the function will print the student name and class.'''

def student_data(student_id, student_name=None, student_class=None):
    print(f"Student ID: {student_id}")
    
    if student_name is not None:
        print(f"Student Name: {student_name}")
        
    if student_class is not None:
        print(f"Student Class: {student_class}")

# Example usage: 
# If you only want to print ID:
student_data(12345)

# If you want to print ID, Name, and Class:
student_data(67890, student_name="John Doe", student_class="Grade 10")
