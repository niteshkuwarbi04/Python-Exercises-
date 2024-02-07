'''
3. Write a Python program to create an instance of a specified class and display the namespace of the said instance.'''

class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

# Create an instance of ExampleClass
example_instance = Employee(name="John", department='Sales')

# Display the namespace of the instance
print("Namespace of the instance:")
print(example_instance.__dict__)
