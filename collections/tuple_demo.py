#Tuple
'''
* ✅ Ordered
* ✅ Indexed
* ✅ Allows duplicate values
* ❌ Immutable (cannot be modified)
* ✅ Can store different data types
* more secure than list'''

my_tuple = (1, 2, 3, 4, 5, 6, 2, 3, 4, 5)
print(type(my_tuple))
#This individual tuple's item
for item in my_tuple:
    print(item)

print('OR')
print(my_tuple[1]) #2
print(my_tuple[-3])#3

#Print  the range of tuples.
print(my_tuple[3:6])#4,5,6
print(my_tuple[-4:-1]) #2,3,4
print(my_tuple[:])
print(my_tuple[:-3])# 1, 2, 3, 4, 5, 6, 2
print(my_tuple[:3]) #1, 2, 3,
print(my_tuple[-4:6]) #()
print(my_tuple[-3: 5]) # 2, 3,
print(my_tuple[::1])# full tuple
print(my_tuple[::-1])# reverse tuple
print(my_tuple[::-2])# 5,3,6,4,2

#We cannot modify the tuple's value --> it is immutable
#we can convite tuple into list and vice versa
my_list = list(my_tuple)
my_list[0] = 8
print(my_list)
my_tuple = tuple(my_list)
print(my_tuple)

data_tuple=("Rimjhim", "30",130000,"Google")
print(type(data_tuple))
print(data_tuple)
#Check whether an item is present in the tuple or not.
print("Rimjhlim" in data_tuple) #True

if "Rimjhim" in data_tuple:
    print("Rimjkim" in data_tuple)

#Copping tuple
tuple1=(1, 2, 3, 4)
tuple2=tuple1
print(tuple2)
del tuple2
tuple2 =('a', 'b', 'c')
print(tuple1+tuple2)

tuple2 = tuple1
if tuple1 == tuple2:
    print("True")
else:
    print("False")






