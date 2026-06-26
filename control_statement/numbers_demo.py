num = 10
print(type(num)) #int

num = 10.6
print(type(num)) #float

print("Find maximum of 3 numbers ")
i,j,k = 65, 90,21
if i>=j and i>=k:
    print(i," is gratest number")
elif j>=i and j>=k:
    print(j," is gratest number")
else:
    print(k," is gratest number")

print("OR")
print(max(i,j,k))
print("AND")
print(min(i,j,k))
