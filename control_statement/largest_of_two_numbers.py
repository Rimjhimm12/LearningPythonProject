##Find the largest number between two numbers.
number1 = float(input("Enter the first number:"))
number2 = float(input("Enter the second number:"))

if number1>number2:
    print(number1," is the largest number")
elif number1==number2:
    print("Both the numbers are same ",number1)
else:
    print(number2," is the largest number")