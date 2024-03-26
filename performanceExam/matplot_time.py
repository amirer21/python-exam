import math
import timeit
import random

import matplotlib.pyplot as plt

xdata = [100, 200, 400, 800, 1000]
ydata = [36, 65, 140, 287, 358]


def plot(xdata, ydata):
    """Plot a range of ydata (on y-axis) against xdata (on x-axis)"""
    plt.plot(xdata, ydata)
    plt.show()


def plot_many(xdata, ydatas):
    """Plot a sequence of ydatas (on y-axis) against xdata (on x-axis)"""
    for ydata in ydatas:
        plt.plot(xdata, ydata)
    plt.show()


def common_items(seq1, seq2):
    """Find common items between two sequences, version 2.0"""
    seq_dict1 = {item: 1 for item in seq1}
    for item in seq2:
        try:
            seq_dict1[item] += 1
        except KeyError:
            pass
    return [item[0] for item in seq_dict1.items() if item[1] > 1]


def setup(n):
    """Setup function for generating test data"""
    global a1, a2
    a1 = random.sample(range(0, 2 * n), n)
    a2 = random.sample(range(0, 2 * n), n)


def test():
    """Test function for common_items"""
    return common_items(a1, a2)


def time_test(setup_size, number_of_tests):
    """Function to time the test function with a given setup size"""
    setup(setup_size)
    t = timeit.Timer('test()', globals=globals())
    return 1000000.0 * t.timeit(number=number_of_tests) / number_of_tests


def main():
    plot(xdata, ydata)
    # case 1
    ydata2 = xdata
    # case 2
    #ydata2 = list(map(lambda x: 0.35 * x, xdata))
    plot_many(xdata, [ydata, ydata2])

    test_sizes = [100, 200, 400, 800, 1000]
    number_of_tests = 10000

    for size in test_sizes:
        execution_time = time_test(size, number_of_tests)
        print(f"Execution time for setup size {size}: {execution_time} microseconds")


if __name__ == "__main__":
    main()