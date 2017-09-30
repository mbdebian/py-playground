# MRO sample

class MyBaseClass(object):
    def __init__(self, value):
        self.value = value

class TimesFive(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value *= 5


