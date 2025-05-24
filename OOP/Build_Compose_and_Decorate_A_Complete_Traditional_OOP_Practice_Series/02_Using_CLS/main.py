class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


a = Counter()
b = Counter()
c = Counter()


print(Counter.get_count())