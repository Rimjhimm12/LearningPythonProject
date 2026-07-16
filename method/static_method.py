class Employee:
    @staticmethod
    def company_name():
        print("ABC Company")

    def employee_details(self, name, salary):
        print('Employee Details')
        print("Name:", name)
        print("Salary:", salary)

emp = Employee()
Employee.company_name()
emp.employee_details("Rimjhim", 20000)