class A():
    name = "Rim"

class B(A):
    def m1(self):
        print(super().name)
        name = "John"
        print(name)
obj1 = B()
obj1.m1()
