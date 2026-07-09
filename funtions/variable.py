"""The variable stores values.
The variables create outside the function are called global variables.
The variables created inside the function are called local variables."""

#Example 1:
global_var = 20
def func():
    local_var = 30
    print(global_var+local_var)

print(global_var)
#print(local_var) we can't access a local variable outside the function.
func()

#Example 2:
xy = 30
def cool():
    xy = 40
    print(xy)

cool() #40

#Example 3:
xyz = 30 #global variable
def cool():
    global xyz
    n = xyz
    xyz = 40 #local Variable
    print(n+ xyz)
cool()

def fun_2():
    global a
    a = 400
    print(a)
fun_2()
print(a)