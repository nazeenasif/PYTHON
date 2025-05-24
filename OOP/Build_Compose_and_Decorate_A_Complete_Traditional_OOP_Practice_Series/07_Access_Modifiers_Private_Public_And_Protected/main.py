class Employee:

    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

    def get_ssn(self):
        print(f"Employee ssn: {self.__ssn}")

employee1 = Employee("John Doe", 50000, "1239")

print(f"Employee name: {employee1.name}")
print(f"Employee salary: {employee1._salary}")
employee1.get_ssn()  # Output: Employee ssn: 1239

