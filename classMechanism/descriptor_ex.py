class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        obj.__dict__[self.name] = value

class MyClass:
    number = Integer('number')

    def __init__(self, number):
        self.number = number

# Using the descriptor
obj = MyClass(100)
print(obj.number)  # 100
obj.number = 200   # Works fine
# obj.number = 'Hello'  # Raises TypeError: Expected an int