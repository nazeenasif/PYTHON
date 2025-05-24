class Department:
    def __init__(self, name):
        self.name = name

class Employee:    
    def __init__(self, employees):
        self.employees = employees

employee1 = Employee("Mujtaba") 
employee2 = Employee("Ahmed")

department = Department([employee1, employee2])

print(f"Department: {department}")

del department

print(f"employee: {employee1}")
print(f"employee2: {employee2}")