#1. No argument, no return value.
def my_function():
    print('I am practicing function once again.')
#Printing, calling the function
my_function()

#2. No argument with return value
def my_function_2():
    return "No argument with return value."
#Calling my second function
print(my_function_2())

#3. With argument, no return value
def my_function_3(i,j):
    print(i,j)
    j = i+j
    print(j)
#Calling my third function
my_function_3(3,5)

#4. With argument and with return value
def my_function_4(i,j):
    print(i,j)
    return i*j
print(my_function_4(7,8))
