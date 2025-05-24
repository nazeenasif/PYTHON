class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"I have a dog named {self.name} and his breed is {self.breed}. He says: Woof!")


dog = Dog("Jimmy", "Bulldog")        
dog.bark()