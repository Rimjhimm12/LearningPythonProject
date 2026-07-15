#Types of arguments
'''1.Positional arguments
2. Keywords argument '''
#Example 1
def func(i, j):
    print(i,j)
func(1,2)

def func2(i=10, j=20):
    print(i,j)
func2()

#Example 2: default values assigned to positional arguments
def func3(i, j=122):
    print(i,j)
func3(3, 2)
func3(23)

#Example 3: Keyword Argument
def func4(name, roll):
    print("Name",name,", Roll",roll)
func4(name ="Rimjhim", roll=30)
func4(roll=30,name ="Rimjhim")

#Example 4: expositional and Keywords Argument
def func5(a, b,c):
    print(a,b,c)
func5(5,6,7) # expositional parameters
func5(a=5,b=6,c=7) #Keyword Parameters
func5(b=6,a=5,c=7) #Keyword parameters: But jumble, The positions
func5(5,6,c=7)
#func5(a=5,6,7)
''' Positional arguments must come first, keyword arguments come after — and once you switch to keyword,
  you can't switch back to positional.'''
#Example 5:
def func6(a, b, c):
    if a > b:
        return a,b
    else:
        return b,c

print(func6(1, 2, 3))
print(type(func6(1, 2, 3)))

