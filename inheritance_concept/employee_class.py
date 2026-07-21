class EmployeeA:
    def m1(self):
        print("This is a method of Employee class A")

class EmployeeB(EmployeeA):
    def m2(self):
        print("This is a method of Employee class B")
    def m1(self):
        print("This is a method of Employee class AB")
if __name__ == '__main__':
    obj1 = EmployeeB()
    obj1.m2()
    obj1.m1()
    obj2 = EmployeeA()
    obj2.m1()
