class MyClass:
    def __init__(self, emp_id, emp_name,emp_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary

    def display_emp_details(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Employee Salary:", self.emp_salary)

mc = MyClass("10c001", "John", 50000)
mc.display_emp_details()
