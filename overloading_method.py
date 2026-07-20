class A:
    def m1(self):
        print("m1")
class B(A):
    def m1(self):
        print("m2")
class C(B):
    def m1(self):
        print("m3")
m = [A(), B(), C()]
o = C()
o.m1()
for obj in m:
    obj.m1()


