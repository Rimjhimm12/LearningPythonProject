#Check whether the given number is positive or negative.
try:
    number = float(input("Enter a number: "))
except ValueError:
    print("Please enter a number ")
else:
    if number > 0:
        print("This is a positive number")
    elif number == 0:
        print("This is zero")
    else:
        print("This is a negative number")
