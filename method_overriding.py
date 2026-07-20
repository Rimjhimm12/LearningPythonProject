class A():
    def m1(self):
        print("This is a method of class A")

class B(A):
    def m1(self):
        print("This is a method of class B")
        super().m1()

obj1 = B()
obj1.m1()