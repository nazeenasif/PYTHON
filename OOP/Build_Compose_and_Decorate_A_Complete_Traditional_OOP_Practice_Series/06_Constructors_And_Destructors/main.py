class  Logger:

    def __init__(self):
        print("Object Created!")

    def __del__(self):    
        print("Object Destroyed!")

obj1 = Logger()        

print(obj1)