# we can create string in three different way
# within '', "" and str("Welcome")
#


s = 'hello world'
print(type(s))
print(s)

name = '' # empty string
print("name is ...:",name)

print(id(name)) #4373300848
print(id(s))

name = name + "t"
print(id(name))
print(name)

# + vs * in string
name = 'rimjhim'
print(name+" mallick") #rimjhim Mallick ----> concatenation is happening here
print(name*2)#rimjhimrimjhim ---> for reputation we can use '*'


# Slicing [] operate
# stating index start from 0
#ending index will be(n-1)

name = "Rimjhim"
print(name[1:4])#imj
print(name[:8]) # full name
print(name[:4])#Rimj
print(name[2:])#mjhim
print(name[2])#m
print(name[1:-1])#imjhi
#  R  i  m  j  h  i  m
#  0  1  2  3  4  5  6   ← positive indices
# -7 -6 -5 -4 -3 -2 -1  ← negative indices

#ord() and chr()
print(ord('A')) # returns the ASCII value 65 (of a character)
print(chr(66)) # returns ASCII code #B

#max(), min(), len()
#max() and min() on strings work based on ASCII/Unicode value of each character — essentially alphabetical
#order, but with some nuances.
print(max("RiMjhiM")) #R
print(min("Hello"))  #i
print(len("Rimjhim")) #7
# in , not in operator
s ="welcome"
print("come" in s) # True
print("kjim" in s) #False
print("kjim" not in s) #True

# string comparison with relation operator
#When you use relational operators (<, >, ==, !=, <=, >=) on strings, Python compares them character by
#character using their ASCII/Unicode values, from left to right
print("---------")
print("tim" == "tim") #true
print("tim" == "tie") #false
print("free" != "freedom") #true
print("arrow" > "aron") #true
print("teeth" < "tee")#false
print("yellow" <= "fellow")#false
print("abc" >"") #true
print("---------")
#testing strings --> True or False
# ┌──────────────────┬─────────────────────────────────────────────┬─────────────────────────────────────┐
#   │      Method      │              Question it asks               │   Result for "Welcome to python"    │
#   ├──────────────────┼─────────────────────────────────────────────┼─────────────────────────────────────┤
#   │ s.isalnum()      │ Are ALL characters letters or digits? (no   │ False — has spaces                  │
#   │                  │ spaces, no symbols)                         │                                     │
#   ├──────────────────┼─────────────────────────────────────────────┼─────────────────────────────────────┤
#   │ s.isalpha()      │ Are ALL characters letters only? (no        │ False — has spaces                  │
#   │                  │ digits, no spaces)                          │                                     │
#   ├──────────────────┼─────────────────────────────────────────────┼─────────────────────────────────────┤
#   │ s.isdigit()      │ Are ALL characters digits (0–9)?            │ False — has letters                 │
#   ├──────────────────┼─────────────────────────────────────────────┼─────────────────────────────────────┤
#   │ s.isidentifier() │ Is it a valid Python variable name?         │ False — has spaces (valid:          │
#   │                  │                                             │ welcome_to_python)                  │
#   ├──────────────────┼─────────────────────────────────────────────┼─────────────────────────────────────┤
#   │ s.isprintable()  │ Are ALL characters printable? (no hidden    │ True — all normal visible           │
#   │                  │ chars like \n, \t)                          │ characters                          │
#   ├──────────────────┼─────────────────────────────────────────────┼─────────────────────────────────────┤
#   │ s.isspace()      │ Is the ENTIRE string just whitespace?       │ False — has letters                 │
#   ├──────────────────┼─────────────────────────────────────────────┼─────────────────────────────────────┤
#   │ s.islower()      │ Are ALL letters lowercase?                  │ False — W is uppercase              │
#   ├──────────────────┼─────────────────────────────────────────────┼─────────────────────────────────────┤
#   │ s.isupper()      │ Are ALL letters uppercase?                  │ False — most are lowercase          │
#   └──────────────────┴─────────────────────────────────────────────┴─────────────────────────────────────┘

s = "Welcome to python"
print(s.isalnum())
print(s.isalpha())
print(s.isdigit())
print(s.isidentifier())
print(s.isprintable())
print(s.isspace())
print(s.islower())
print(s.isupper())

#Searching for substring
print("--------")
print(s.endswith("thon")) #True
print(s.startswith("Wel"))#True
print(s.find("e to ")) #6
print(s.find(" "))#7
print(s.count("o")) #3





