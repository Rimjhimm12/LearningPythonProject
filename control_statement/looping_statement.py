
# Three ways we can use range() function
# range(10) --> it starts from 0 ..... and ending point is 9, always (n-1), n =10 here;
# range(1, 10) ---> 1 is starting point, 9 is ending point
# range(1,10,2) --> Starting point 1, ending point is 10, it increments by 2.
# for an example: 1, 3, 5, 7, 9

# there are two looping statement
#1. for loop ----> we use range() with for loop
#2. while loop
print("___________ Ascending order _______________")
i =1 #initialization
while i<10: #condition
    print(i)
    i=i+1 #increment
print("___________ Descending order _______________")
# Descending order
i = 10
while i>=0:
    print(i)
    i=i-1
print("_________Even Number_________________")

#Print even number between given range
num1 = int(input("Enter staring number: "))
num2 = int(input("Enter destination number: "))

i = num1
while i<=num2:
    if i%2==0:
        print(i)
    i= i+1

print("___________Odd Number_______________")
# Print odd number between given range
num1 = int(input("Enter staring number: "))
num2 = int(input("Enter destination number: "))

i = num1
while i <= num2:
    if i % 2 != 0:
        print(i)
    i = i + 1


