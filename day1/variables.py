############# Example 1 #########
from multiprocessing.util import ForkAwareThreadLock

a = 1
b =2
print(a) #1
print(b) #2
print(a,b) #1, 2
print(b, a) #2, 1

########### Example 2 ###############

a , b , c = 1, 2, 3
print(a, b, c)
print(c, a, b)
print(c, b, a)

####### Example 3 ###########

d = 100
e = 100
f = 100
#or when all the variables have the same value we can use the following syntax
d = e = f = 100

print(d, e, f)

####### Example 4 -- Swapping #######
x = 12
y = 13
print (x, y) # 12 13
y , x = x , y
print(x, y) #13 12

####### Example 5 #############
# g = 664 # at the beginning there is a space- Python follows indentation
# print(g)
g = "GOAT"
print(g)
