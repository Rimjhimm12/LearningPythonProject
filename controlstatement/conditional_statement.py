# if if..else elif

#First example: whether a person is eligible to vote or not
age = 15
if age >= 18:
    print("Eligibility approved") #indentation is important
else:
    print("Eligibility rejected")


#Second Example 2
true = age >= 18
print (type(true)) #bool
false = age < 18
if true:
    print("This is true condition")
else :
    print("This is false condition")

#Third Example
statement = 0
if statement:
    print("This is True condition")
else:
    print("This is False condition")



#Write a program whether a number is even or odd
num = int(input("Enter a number: "))
if num%2==0:
    print("This number is even")
else:
    print("This number is odd")

#If-else statement in a single line
# <if_true> if <condition> else <if_false>
#It is not a ternary operation or operator we are using here.
# However, we consider it is a ternary expression
# it's basically the conditional expression we are using in a single line.
number = 13
print("Even number") if number%2==0 else print("Odd number")

#If you want to print multiple print statements
# in an if-else condition on a single line,
# then we have to use curly braces and inside the curly braces
# we have to keep all the print statements.

{print("Hello"), print("World")} if 10>=2 else {print("wrong"),print("window")}

#for multiple conditions - elif
week_number = int(input("Enter a week number: "))
if week_number ==1:
    print("Sunday")
elif week_number ==2:
    print("Monday")
elif week_number ==3:
    print("Tuesday")
elif week_number ==4:
    print("Wednesday")
elif week_number ==5:
    print("Thursday")
elif week_number ==6:
    print("Friday")
elif week_number ==7:
    print("Saturday")
else:
    print("Choose a number between 1 and 7.")

#Check whether the given number is positive or negative.
#Find the largest number between two numbers.
#Find the largest number among three numbers.
#Print the correct browser depending on the input value. 
