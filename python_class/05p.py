'''
5. Define a Python function student(). Using function attributes display the names of all arguments.'''

# def student(student_id, student_name, student_batch):
#     return f'Student ID: {student_id}\nStudent Name: {student_name}\nClass: {student_batch}'
# print(student('1001', 'Nitesh Kuwarbi', 'MCA'))

def Student(student_id, student_name, student_branch):
    return f'Student ID : {student_id} \n Student Name : {student_name} \n Student Branch : {student_branch}'

print(Student(1001, 'Vivek Singh', 'BCA'))
print(Student(1002, 'Jitendra Mehra', 'BCA'))
print(Student(1003, 'Ayush Singh', 'MCA'))