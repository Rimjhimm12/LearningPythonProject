##### int ####
num1 = input("Enter a number : ")
num2 = input("Enter a number : ")
print(type(num1)) #When we take input from the user, it is always taken as a string type imput
print(type(num2)) #str
print(num1 + num2) #num1num2

#Let's convert it here.
mum1 = int(num1)
mum2 = int(num2)
print(type(mum1)) #int
print(type(mum2)) #int
print(mum1 + mum2) #General Addition

####### Float data type
num1 = float(num1)
num2 = float(num2)
print(type(num1)) #float
print(type(num2)) #float
print(num1 + num2) #We will get some decimal value.

######Complex data type#######
num1 = complex(num1 + 4j)
num2 = complex(num2 + 5j)
print(type(num1)) #complex
print(type(num2)) #complex
print(num1 + num2) #Numbers additional value +9j 