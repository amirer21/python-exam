from functools import wraps

class DecoExam:
    def decorator(callable):        
        @wraps(callable)
        def wrapped(self, x, y, *args, **kwargs):
            return callable(self, x, y, *args, **kwargs)
        return wrapped
    
    @decorator
    def add(self, x, y):
        return x + y
    
    @decorator
    async def async_add(self, x, y):
        return x + y
    
    
# main
if __name__ == "__main__":
    deco_exam = DecoExam()
    print(deco_exam.add(1, 2))
