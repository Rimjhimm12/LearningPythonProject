# there are two jumping statements in Python
# brake and continue
# Using break statement
print("----------- Using break Statement-----------")
for i in range(1, 10):
    print(i)
    if i == 5:
        break
print("Good Bye")

# Using continue statement
print("----------- Using continue Statement-----------")
for i in range(1, 10): #1,2,3,4,6,7,8,9
    if i ==5:
        continue
    print(i)
print("I am here")


for i in range(1, 10): #1,2,3,4,6,7,8,9
    if i ==5 or i==3 or i==7:
        continue
    print(i)
print("I am here")