# MRO sample

from pprint import pprint

class MyBaseClass(object):
    def __init__(self, value):
        self.value = value

class TimesFive(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value *= 5

class PlusTwo(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 2

class GoodWay(TimesFive, PlusTwo):
    def __init__(self, value):
        super().__init__(value)

# Use case
foo = GoodWay(5)
print("It results in 5*(5+2) = 35 ---> {}".format(foo.value))

# Pretty print MRO
print("---> MRO:")
pprint(GoodWay.mro())
