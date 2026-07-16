class Calculation:
    a, b = 2, 10

    def add_numbers(self):
        print(self.a+self.b)

    @staticmethod
    def static_addition():
        print(Calculation.a+Calculation.b)

cal = Calculation()
cal.add_numbers()
Calculation.static_addition()
