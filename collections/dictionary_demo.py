#dictionary
'''
* ✅ Stores data as key-value pairs
* ✅ Mutable
* ✅ Ordered (Python 3.7+)
* ❌ Duplicate keys are not allowed
* ✅ Duplicate values are allowed
'''
product_dict = {"Shirt":4, "Pant":5,"TankTop":2}
print(type(product_dict))
print(product_dict)

for key, value in product_dict.items():
    print(key, value)

print(product_dict["Shirt"])
print(product_dict.get("Pant"))
print(product_dict.pop("TankTop"))

product_dict.update({"Shirt":4, "Pant":9,"TankTop":2})
print(product_dict)
product_dict["Shirt"] = 10
print(product_dict)

for i in product_dict:
    print(i,":", product_dict[i])

print("Shirt" in product_dict)

if "TankTop" in product_dict:
    print(product_dict["TankTop"])
else:
    print("TankT is not exit")

product_dict.pop("TankTop")
print(product_dict)
del product_dict["Shirt"]
print(product_dict)
product_dict.update({"Shirt":4, "Pant":9,"TankTop":2})
product_dict.clear()
print(product_dict)
product_dict.update({"Shirt":4, "Pant":9,"TankTop":2})
print(product_dict)
#del product_dict
#product_dict.update({"Shirt":4, "Pant":9,"TankTop":2})
#print(product_dict)

