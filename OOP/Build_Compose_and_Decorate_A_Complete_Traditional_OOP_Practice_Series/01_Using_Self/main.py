class Student:
    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")


student1 = Student("Nazeen", 85) 
student1.display()  # Output: Name: Nazeen Marks: 85
