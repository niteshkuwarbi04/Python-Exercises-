'''
5. Define a Python function student(). Using function attributes display the names of all arguments.'''

def student(student_id, student_name, student_batch):
    return f'Student ID: {student_id}\nStudent Name: {student_name}\nClass: {student_batch}'
print(student('1001', 'Nitesh Kuwarbi', 'MCA'))
