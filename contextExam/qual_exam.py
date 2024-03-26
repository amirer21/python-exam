class OuterClass:
    def outer_method(self):
        pass

    class InnerClass:
        def inner_method(self):
            pass

# Accessing the __qualname__ attribute
print(OuterClass.__qualname__)              # Outputs: OuterClass
print(OuterClass.outer_method.__qualname__) # Outputs: OuterClass.outer_method
print(OuterClass.InnerClass.__qualname__)   # Outputs: OuterClass.InnerClass
print(OuterClass.InnerClass.inner_method.__qualname__) # Outputs: OuterClass.InnerClass.inner_method