from time import perf_counter as timer_func
from contextlib import contextmanager
import random

def common_items(seq1, seq2):
    """Find common items between two sequences"""
    common = []
    for item in seq1:
        if item in seq2:
            common.append(item)
    return common

@contextmanager
def timer():
    """A simple timing function for routines"""
    try:
        start = timer_func()
        yield
    except Exception as e:
        print(e)
        raise
    finally:
        end = timer_func()
        print(f"Time elapsed: {1000.0*(end - start)}s")

def generate_test_data(n):
    """Generate test data for numerical lists given input size"""
    a1 = random.sample(range(0, 2*n), n)
    a2 = random.sample(range(0, 2*n), n)
    return a1, a2

def perform_test(n, func):
    """Perform test on a given function with generated test data"""
    #a1 = random.sample(range(0, 2*n), n)
    #a2 = random.sample(range(0, 2*n), n)
    a1, a2 = generate_test_data(n)

    with timer() as t:
        result = func(a1, a2)
        #print(f"[{n}] Test result :: , {result}")

def main():
    """Main function to execute the test"""
    # Directly calling common_items with test data
    common_items_result = common_items(*generate_test_data(100))
    print("Common items result:", common_items_result)

    # Using the perform_test function
    perform_test(100, common_items)
    perform_test(200, common_items)
    perform_test(400, common_items)
    perform_test(500, common_items)
    perform_test(800, common_items)
    perform_test(1000, common_items)

# main 함수 실행
if __name__ == "__main__":
    main()