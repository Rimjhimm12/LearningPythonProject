#using for loop print 1.....10
for i in range(10):
    print(i)

print("---------------------")

for i in range(1, 10):
    print(i)

print(" Print 1 to 20")
for i in range(1,21):
    print(i)

print(" Print 1 to 10 in decreasing order")
for i in range(10,0,-1):
    print(i)

print("print only even numbers between 1 to 10")
for i in range(2,10,2):
    print(i)

print("OR")

for i in range(1,10,1):
    if i%2==0:
        print(i)
print("print only odd numbers between 1 to 10")
for i in range(1,10,2):
    print(i)

print("OR")
for i in range(1, 10,1):
    if i%2!=0:
        print(i)

