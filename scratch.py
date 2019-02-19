from numbers import Number

class Test(Number):
    def __init__(self, num):
        self.num = num

    def __mul__(self, test2):
        print(test2)

    def __rmul__(self, test2):
        print(test2)

    def __truediv__(self, test2):
        Test.asdf()
        print(test2)

    @staticmethod
    def asdf():
        print("hello")

