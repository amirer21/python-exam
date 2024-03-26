import timeit
import random


def common_items(seq1, seq2):
    """Find common items between two sequences"""
    common = []
    for item in seq1:
        if item in seq2:
            common.append(item)
    return common


def test():
    """Test function for common_items"""
    return common_items(a1, a2)


def setup(n):
    """Setup function for generating test data"""
    global a1, a2
    a1 = random.sample(range(0, 2 * n), n)
    a2 = random.sample(range(0, 2 * n), n)


def time_test(setup_size, number_of_tests):
    """Function to time the test function with a given setup size"""
    setup(setup_size)
    t = timeit.Timer('test()', globals=globals())
    return 1000000.0 * t.timeit(number=number_of_tests) / number_of_tests


def main():
    test_sizes = [100, 200, 400, 800]
    number_of_tests = 10000

    for size in test_sizes:
        execution_time = time_test(size, number_of_tests)
        print(f"Execution time for setup size {size}: {execution_time} microseconds")


if __name__ == "__main__":
    main()
