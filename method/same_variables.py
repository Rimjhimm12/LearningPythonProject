a,b=1,2
class Calculator:
    a,b=10,20
    def add_nmm(self, a, b):

        #a,b=100,200
        print(a+b)#300
        print(self.a+self.b)#30
        print(globals()['a']+globals()['b'])#3

cal = Calculator()
cal.add_nmm(100,200)
print(cal.a)#10
print(cal.b)#20
print(a)#1
print(b)#2
