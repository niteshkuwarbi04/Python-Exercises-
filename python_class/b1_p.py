'''
1. Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and methods like 
   calculate_emp_salary, emp_assign_department, and print_employee_details.'''

class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (self.emp_salary / 50)
            total_salary = self.emp_salary + overtime_amount
        else:
            total_salary = self.emp_salary

        return total_salary

    def emp_assign_department(self, new_department):
        self.emp_department = new_department

    def print_employee_details(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Employee Salary:", self.emp_salary)
        print("Employee Department:", self.emp_department)

# Sample Employee Data
employee1 = Employee("Vivek Singh Rawat", "E7876", 50000, "ACCOUNTING")
employee2 = Employee("Jitendra Mehra", "E7499", 45000, "Development")
employee3 = Employee("Ayush Singh", "E7900", 50000, "SALES")
employee4 = Employee("Akanksha Joshi", "E7698", 55000, "OPERATIONS")

# Sample usage of methods
employee1.print_employee_details()

# Change department using the assign_department method
employee2.emp_assign_department("HR")

# Print details after department change
employee2.print_employee_details()

# Calculate salary with overtime for employee3
total_salary_employee3 = employee3.calculate_emp_salary(55)
print(f"Total Salary for {employee3.emp_name}: ${total_salary_employee3}")
