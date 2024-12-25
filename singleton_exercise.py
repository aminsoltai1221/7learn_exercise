class SingletonBase:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print(cls)
            cls._instances[cls] = super(SingletonBase, cls).__new__(cls, *args, **kwargs)
        return cls._instances[cls]

# کلاس‌های فرزند
class ChildA(SingletonBase):
    def __init__(self):
        self.name = "ChildA"

class ChildB(SingletonBase):
    def __init__(self):
        self.name = "ChildB"

# تست
a1 = ChildA()
a2 = ChildA()
b1 = ChildB()
b2 = ChildB()

print(a1 is a2)  # خروجی: True (سینگل‌تون در ChildA)
print(b1 is b2)  # خروجی: True (سینگل‌تون در ChildB)
print(a1 is b1)  # خروجی: False (هر کلاس شیء مختص به خود دارد)
