#Exception is an even which causes programing termination
#try, except, els, finally

print("this is starting point of my program ....")
print(1)
print(2)
try:
    print(x)
except:
    print("=====Exception occurred========")
print(4)
print("This is end point of my program ....")


#Example 2
print("this is starting point of my program ....")
print('Program is running ....')
try:
    print(0/0)
except ZeroDivisionError:
    print("=====Exception occurred: ZeroDivisionError========")
except TypeError:
    print("=====Exception occurred: TypeError========")
print("This is end point of my program ....")

#Example 3
try:
    num1, num2 = 10, 0
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("=====Exception occurred: ZeroDivisionError========")
except TypeError:
    print("=====Exception occurred: TypeError========")
except NameError:
    print("=====Exception occurred: NameError========")
except SyntaxError:
    print("=====Exception occurred: SyntaxError========")
else:
    print("=====No exception occurred========")
finally:
    print("=====This is finally block========")

#Example 4: raising our own exception
def enterage(num):
    if num<0:
        raise ValueError("===Only Integers are allowed====")
    if num%2==0:
        print("Even number")
    else:
        print("Odd number")

try:
    enterage(5)
except ValueError:
    print("=====Exception occurred: ValueError========")