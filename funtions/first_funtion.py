
'''We can create functions in multiple ways:
1. One function does not take an argument and does not return any value.
2. Second function does not take an argument but returns some value.
3. Function takes an argument but no return value.
4. Function takes an argument and also returns value.'''
## def : we use the keyword to create a function: definition and decleration
#Without Parameter and return Function
def my_function():
    print("Hello World")

#Calling function
my_function()

#Example 2: with one parameter and without return type function
def function_1(name):
    print("Hello,",name,"!")
function_1("Rimjhim")

#Example 3: two parameters and a return type function
def addition_function(num1, num2):
    return num1+num2
add = addition_function(1, 2)
print(add)

#Example 4: empty function returns: None.
def func():
    return
print(func())

#or
def funcc():
    a = 10
print(funcc())

#Exmaple 5:
def cal(a,b):
    print(a+b)
cal(6,7)