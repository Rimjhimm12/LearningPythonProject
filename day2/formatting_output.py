name, age, salary = "Rimjhim", 30, 130000
print("Find details:")
print(name, age, salary)

print("Name is: ", name, "Age is:",age ,"Salary is:",salary)
print("Name is: ", name,'\n' "Age is:",age,'\n'"Salary is:",salary)

# s stands for str, d stands for digit,g stands for double
print("Name is :%s Age is:%d Salary is:%g"%(name,age,salary))
print("Name is :%s" '\n' "Age is:%d" '\n' "Salary is:%g"%(name,age,salary))

#Approach {}
#order is important
print("name is:{} Age is:{} Salary is:{}".format(name,age,salary))
