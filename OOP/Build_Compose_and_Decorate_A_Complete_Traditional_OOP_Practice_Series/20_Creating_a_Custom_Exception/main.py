class InvalidAgeError(Exception):
    """Raised when the age is invalid."""
    def __init__(self, message="You are younger than 18! "):
        self.message = message
        super().__init__(self.message)

def check_age(age):
    if age < 18:
        raise InvalidAgeError
    print("Access granted")

try:
    user_input = int(input("Enter your age: "))
    check_age(user_input)
except InvalidAgeError as e:
    print(e.message)
except ValueError:
    print("Your age is incorrect")    
