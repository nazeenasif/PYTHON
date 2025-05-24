class Engine:    

    def start(self):
        print("Engine starts...")


class Car: 

    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()

car1 = Car()

car1.drive()
