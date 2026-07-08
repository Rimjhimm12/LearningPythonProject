#set
'''
* ❌ Unordered
* ✅ Mutable
* ❌ No duplicate elements
* ❌ Not indexed
* ✅ Can store different data types (as long as the elements are hashable)'''

fruits_set = {"apple", "banana", "cherry"}
print(type(fruits_set)) #set


#Accessing items from set
print(fruits_set)#Entire set will be printed
print("OR")
for i in fruits_set:
    print(i)

#Whether an item is available in set or not
print("banana" in fruits_set) #true
# Add a new item in set --- for single item user add() function
fruits_set.add("Watermelon")
print(fruits_set)
# Add multiple new items in set --- for single item update() function
fruits_set.update(["Watermelon","mango","pineapple"])
print(fruits_set)
#length of a set
print(len(fruits_set))
#Remove item from the set
fruits_set.remove("Watermelon")
#fruits_set.remove("xyz") #key error
print(fruits_set)

fruits_set.discard("banana")
fruits_set.discard("xyz") # it does not throw any error
print(fruits_set)

#Clear all items
#fruits_set.clear()
#print(fruits_set)
#del fruits_set
#print(fruits_set)


set1 ={1,2,3,4}
set2 = {'a','b','c','d'}
set3 = set1.union(set2)
#set3 = set1 | set2
print(set3)
set4={6,5,8}
set3.update(set4)
print(set3)