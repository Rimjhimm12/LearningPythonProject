'''You need to frequently remove the first element from a collection containing one million elements.'''
import collections

element_list = ["A","B","C","D","E","F","G","H","I"]
i = 0
while i < len(element_list):
    element_list.remove(element_list[i])
    print(element_list)