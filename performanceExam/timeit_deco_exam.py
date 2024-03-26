import timeit
import random
from functools import wraps

# Global variables for setup size and number of tests
setup_size = 100
number_of_tests = 10000
# Global lists for storing test data
a1, a2 = [], []


def time_test_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global setup_size, number_of_tests
        setup(setup_size)
        t = timeit.Timer(lambda: func(*args, **kwargs), globals=globals())
        execution_time = 1000000.0 * t.timeit(number=number_of_tests) / number_of_tests
        print(f"Execution time for setup size {setup_size}: {execution_time} microseconds")
        return func(*args, **kwargs)

    return wrapper


def common_items(seq1, seq2):
    """Find common items between two sequences"""
    common = []
    for item in seq1:
        if item in seq2:
            common.append(item)
    return common


def setup(n):
    """Setup function for generating test data"""
    global a1, a2
    a1 = random.sample(range(0, 2 * n), n)
    a2 = random.sample(range(0, 2 * n), n)


@time_test_decorator
def test():
    """Test function for common_items"""
    return common_items(a1, a2)


def main():
    test()  # This will automatically time the test function


if __name__ == "__main__":
    main()
