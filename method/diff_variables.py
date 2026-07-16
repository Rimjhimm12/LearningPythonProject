a, b = 10, 20 #----> Global Variable
class Math:
    # ------> Class variable.
    c, d =30,40
    def addition(self, x, y):
        #----> Local Variable
        i, j = 30, 40
        print(self.c+self.d)
        print(x + y)
        print(i+j)
        print(a+b)

math = Math()
math.addition(10,20)

