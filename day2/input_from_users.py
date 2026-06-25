# we user input() function
#When we use the input function in Python, it always takes user input in string format.
name = input("Enter your name: ")
age = input("Enter your age: ")
print(type(name)) #str
print(type(age)) #str
print("Name is :%s" '\n' "Age is :%s"%(name,age))
print(name +' '+ age)


num = input("Enter a number: ")
print(type(num))
num = int(num)
print("Performing type cast, str -> int")
print(type(num))
#
# # Approach 1 - type conversion
number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
print(number1 + number2)

# Approach 2 - type conversion
num1 = input("Enter a number : ")
num2 = input("Enter another number : ")
print(int(num1) + int(num2))



