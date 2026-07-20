class myEmployee():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def emp_details(self):
        print("Employee Name:", self.name)
        print("Employee Age:", self.age)


myclass = myEmployee("John", 30)
myclass.emp_details()
