class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        self._price = new_price

    @price.deleter
    def price(self):
        print("Deleting...")

p1 = Product("3000")
p2 = Product("5000")            

print(f"Before change the price of p1 : {p1.price}")
print(f"After change the price of p2 : {p2.price}")

p1 = Product("4000")
p2 = Product("6000")

print(f"Before change the price of p1 : {p1.price}")
print(f"After change the price of p2 : {p2.price}")

del p1.price
print(p1.price)