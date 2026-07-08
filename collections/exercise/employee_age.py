'''Store the ages of employees and remove all duplicate ages.'''
from enum import unique

emp_age = ["33","32","34","35","33","43", "32"]
i = 0
while i < len(emp_age):
    if emp_age.count(emp_age[i]) > 1:
        emp_age.remove(emp_age[i])  # removes the first matching occurrence
    else:
        i += 1
print(emp_age)


