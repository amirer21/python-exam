import logging
import time
from functools import wraps

def get_logger(name=None):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - [%(funcName)s:%(lineno)d] - %(message)s")

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)
    logger.addHandler(console)

    now = time.localtime()
    filename = "log_" + str(now.tm_year) + str(now.tm_mon) + str(now.tm_mday) + str(now.tm_hour) + str(now.tm_min) + str(now.tm_sec)
    file_handler_debug = logging.FileHandler(filename=f"{filename}_debug.log", encoding='utf-8')
    file_handler_debug.setLevel(logging.DEBUG)
    file_handler_debug.setFormatter(formatter)
    logger.addHandler(file_handler_debug)

    file_handler_error = logging.FileHandler(filename=f"{filename}_error.log", encoding='utf-8')
    file_handler_error.setLevel(logging.ERROR)
    file_handler_error.setFormatter(formatter)
    logger.addHandler(file_handler_error)

    return logger

def log_function_call(level=logging.INFO):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger = get_logger(func.__module__)
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                # Log the error along with the traceback
                logger.error("An error occurred: %s", str(e), exc_info=True)
            finally:
                end_time = time.time()
                elapsed_time = end_time - start_time

                # Log function execution time
                logger.log(level, f"Function {func.__name__} executed in {elapsed_time:.6f} seconds")

        return wrapper
    return decorator

@log_function_call()
def example_function():
    # Your code here
    result = 10 / 0  # This will raise a ZeroDivisionError

if __name__ == "__main__":
    example_function()
