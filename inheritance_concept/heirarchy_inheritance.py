class A():
    def m1(self):
        print("This is a method of class A")

class B(A):
    def m2(self):
        print("This is a method of class B")

class C(A):
    def m3(self):
        print("This is a method of class C")

class D(B, C):
    def m4(self):
        print("This is a method of class D")

obj1 = C()
obj1.m1()