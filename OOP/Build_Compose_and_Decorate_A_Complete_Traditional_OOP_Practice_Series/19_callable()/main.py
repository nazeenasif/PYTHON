class Multiplier:

    def __init__(self, factor):
        self.factor = factor

    def call(self, value):
        return value * self.factor
    
value1 = Multiplier(5)
print(callable(value1))

