def log_function_call(func):
    def wrapper():
        print("Fucntion is being called")
        func()
    return wrapper


@log_function_call
def greet():
    print("Hello, World!")


greet()    