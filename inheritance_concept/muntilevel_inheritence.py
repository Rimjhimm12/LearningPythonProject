class A():
    def m1(self):
        print("This is a method of class A")

class B(A):
    def m2(self):
        print("This is a method of class B")

class C(B):
    def m3(self):
        print("This is a method of class C")

obj1 = C()
obj1.m3()
obj1.m2()
obj1.m1()

obj2 = B()
obj2.m1()
obj2.m2()

obj3 = A()
obj3.m1()