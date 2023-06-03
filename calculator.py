class MyCalculator:
    def __init__(self,a,b):    #constructor initilaization
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b


obj = MyCalculator(10,20) #creating an object for class
print(obj.addition())
print(obj.multiply())

