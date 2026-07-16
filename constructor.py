class MyClass:
    def __init__(self):
        print("I am a constructor")

    def addition(self,a,b):
        return a+b

mc = MyClass()
print(mc.addition(10,20))