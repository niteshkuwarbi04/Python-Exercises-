'''
3. Write a Python program to create an instance of a specified class and display the namespace of the said instance.'''

class Employee:
    def __init__(self,name, dept):
        self.name = name
        self.dept = dept

# Creating an instance
instance_ex = Employee(name = "Vivek Singh", dept = "Sales")    

print("Namespace of the instance: ", instance_ex.__dict__)
