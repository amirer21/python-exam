def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Arguments passed to the function:", args)
        print("Keyword arguments passed to the function:", kwargs)
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

@my_decorator
def add_numbers(a, b):
    result = a + b
    print(f"The sum of {a} and {b} is {result}")

say_hello("Alice")
add_numbers(3, 5)

@my_decorator
def example_function(a, b, c=None, d=None):
    print("Inside example_function")
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)

example_function(1, 2, c=3, d="test")
