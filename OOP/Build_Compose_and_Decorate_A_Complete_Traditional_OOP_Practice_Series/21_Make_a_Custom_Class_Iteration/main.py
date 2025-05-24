class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        return self    
    
    def __next__(self):
        if self.current >= 0:
            num = self.current
            self.current -= 1
            return num
        
        else:
            raise StopIteration
        

object = Countdown(15)        
for num in object:
    print(num)