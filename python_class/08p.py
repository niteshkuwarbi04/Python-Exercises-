'''
8. Write a Python program to create two empty classes, Student and Marks. Now create some instances and check whether 
   they are instances of the said classes or not. Also, check whether the said classes are subclasses of the built-in object 
   class or not.'''

class Student:
    pass

class Marks:
    pass

# Creating instances
student_instance = Student()
marks_instance = Marks()

# Checking if instances are instances of the specified classes
is_student_instance = isinstance(student_instance, Student)
is_marks_instance = isinstance(marks_instance, Marks)

# Checking if the specified classes are subclasses of the built-in object class
is_student_subclass = issubclass(Student, object)
is_marks_subclass = issubclass(Marks, object)

print(f"Is student_instance an instance of Student class? {is_student_instance}")
print(f"Is marks_instance an instance of Marks class? {is_marks_instance}")
print(f"Is Student class a subclass of the built-in object class? {is_student_subclass}")
print(f"Is Marks class a subclass of the built-in object class? {is_marks_subclass}")
