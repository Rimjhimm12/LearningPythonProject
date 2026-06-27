'''List:A list is a collection that:
* Maintains insertion order.
* Is mutable (can be modified after creation).
* Allows duplicate elements.
* Stores elements using indexes (starting from 0).
* Can store different data types'''

my_list = [1, 2, 3, 5, 4, 2, 1,3, 2]
fruit_list =["apple", "banana", "cherry", "mango", "apple", "watermelon", "banana"]
employee_data =["Rimjhim","30",130000.00,"Google.com"]
print(my_list)
print(fruit_list)
print(employee_data)

#Accessing items from the list
#Read the list items using loop
print("Print all fruits from the list")

for fruit in fruit_list:
    print(fruit)
print("__________")
print(fruit_list[5])
print("__________")
print(fruit_list[-6])#banana
print("Range of indexes")
print(fruit_list[2:5]) # cherry, "mango", "apple"
print("with negative range")
print(fruit_list[-7:-1]) # "apple", "banana", "cherry", "mango", "apple", "watermelon"

print("Print duplicate  fruits")
new_fruits_list =[]
duplicate_fruits_list =[]
for fruit in fruit_list:
    if fruit in new_fruits_list and fruit not in duplicate_fruits_list:
        duplicate_fruits_list.append(fruit)
    else:
        new_fruits_list.append(fruit)
print(duplicate_fruits_list)
print("OR")
duplicate_fruits_list =[]
for fruit in fruit_list:
    if fruit_list.count(fruit)>1 and fruit not in duplicate_fruits_list:
        duplicate_fruits_list.append(fruit)
print(duplicate_fruits_list)

print("change item value")
employee_data[2]=140000
print(employee_data)

list_of_vegetables = ["Potato", "Tomato","Cabbage","Carrot"]
print("length of the list",len(list_of_vegetables))
for i in range(len(list_of_vegetables)):
    if list_of_vegetables[i] in list_of_vegetables:
        print(list_of_vegetables[i],"Vegetable is present")
    else:
        print("Vegetable is not present")

print("Add item in a list")
list_of_vegetables.append("Potato") # append value end of the list
print(list_of_vegetables)
list_of_vegetables.insert(2,"Onion") # add value depends on index provided
print(list_of_vegetables)
list_of_vegetables.remove("Potato")
print(list_of_vegetables)
list_of_vegetables.pop(2) #remove value depends on provided index
print(list_of_vegetables)
del list_of_vegetables[0] #remove item from the list
print(list_of_vegetables)
list_of_vegetables.clear() #remove all the items 
print(list_of_vegetables)









