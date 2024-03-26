from functools import wraps

def simple_decorator(func):
    @wraps(func)  # This ensures that the original function's metadata is preserved
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@simple_decorator
def say_hello():
    """A simple function that prints 'Hello!'"""
    print("Hello!")

# Calling the decorated function
say_hello()

# Accessing metadata of the original function
print("Function name:", say_hello.__name__)
print("Function docstring:", say_hello.__doc__)
