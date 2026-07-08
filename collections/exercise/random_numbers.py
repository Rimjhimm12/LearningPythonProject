'''You receive random integers and need to know whether a number already exists before inserting it.'''
rem_num = [8,3,11,6,20,30,45,32,45,63,75,66,32,32]
num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
print(type(num_set))
for i in rem_num:
    if i in num_set:
        print(i," is already in the set")
    else:
        num_set.add(i)
print(num_set)

