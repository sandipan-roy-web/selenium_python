from calculator import MyCalculator


# inheritance from Parent node

class ChildNode(MyCalculator):
    num = 100

    def __init__(self):
        MyCalculator.__init__(self, 2, 10)

    def get_data(self):
        return self.num + self.addition()


obj = ChildNode()
print(obj.get_data())
