"""When we create a function inside a class, it is called a method."""
#Creating a class
class MyFirstClass:
    def function_1(self):
        pass
    def function_2(self):
        print("My second method")
    def function_3(self, arg1, arg2):
        print(arg1, arg2)

#Creating an object
obj = MyFirstClass()
obj.function_1()
obj.function_2()
obj.function_3(1, 2)