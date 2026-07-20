class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    def __str__(self): #cannot return number type data
        return self.first + " " + self.last

e1 = Employee("John", "Scotte", 30000)
print(e1)