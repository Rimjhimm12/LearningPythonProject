class A():
    def m1(self):
        print("This is a method of class A")

class B():
    def m2(self):
        print("This is a method of class B")

class C(A, B):
    def m3(self):
        print("This is a method of class C")

obj1 = C()
obj1.m1()
obj1.m2()