class Car:

    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return f"The {self.brand} car is starting..."


car1 = Car("Suzuki")

print(car1.brand)
print(car1.start())
