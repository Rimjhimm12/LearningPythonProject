''' Here's some repeated code. Convert it into a single reusable function, then call it three times with different values.
    print("Testcase 1 passed")
    print("Testcase 2 passed")
    print("Testcase 3 passed") '''

def test_result(testcase):
    print("Testcase",testcase,'passed')
#calling function
test_result(1)
test_result(2)
test_result(3)


#Step 2 Task
'''Write a function called add_numbers that takes two parameters, a and b, and just prints their sum (no return yet — that's Step 3's topic on   
  purpose). '''

def add_numbers(a, b):
    print("Adding two numbers is: ",(a+b))
#Calling add_numbers() function
add_numbers(2,3)
add_numbers(10,20)
add_numbers(-5,5)
#This is the limitation.
result = add_numbers(10,20)
print(result)

#Define add_numbers() function with return keyword.
def add_numbers(a, b):
    return (a+b)
#Calling add_numbers() function
print("Adding two numbers is ",add_numbers(2,3))
print("Adding two numbers is ",add_numbers(10,20))
print("Adding two numbers is ",add_numbers(-5,5))

'''Write a function run_tests(*testcases, **options) that:                                                                              
  - prints each testcase name in testcases                                                                                                              
  - prints any options passed in options (e.g. browser="chrome", headless=True)                                                                         

  Call it like: run_tests("login_test", "logout_test", browser="chrome", headless=True) '''


def run_tests(*testcases, **options):
    for testcase in testcases:
        print(testcase)
        print(options)


run_tests("login_test", "logout_test", browser="chrome", headless=True)
run_tests("login_test","account_detail_test", "logout_test", browser="chrome", headless=True, env="QA")

count = 0
def func():
    for i in range(1,10):
        global count
        k=9
        print(count)
        print(i)

func()
print(count)