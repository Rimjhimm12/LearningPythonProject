string1 = "I love Python"
reverse_string = ''
for i in string1:
    reverse_string= i+reverse_string
print(reverse_string)

print('OR------- using slicing')

rev_str = string1[::-1]
for i in rev_str:
    print(i)


print("Print duplicate characters")
name_str = 'Rimjhim'
duplicate= []
for char in name_str:
    if name_str.count(char) > 1 and char not in duplicate:
        duplicate.append(char)
print(duplicate)

print("OR")
seen= []
duplicates = []
for char in name_str:
    if char in seen and char not in duplicates:
        duplicates.append(char)
    else:
        seen.append(char)
print(duplicates)




