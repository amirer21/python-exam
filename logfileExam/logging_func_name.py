import logging
from functools import wraps

# 로깅 기본 설정: 디버그 레벨로 설정하고, 콘솔에 출력되도록 합니다.
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


# def log_function_call(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         # 함수 이름과 파라미터 로깅
#         logging.debug(f"Called function: {func.__name__} with args: {args} and kwargs: {kwargs}")
#         # 원래 함수 호출
#         return func(*args, **kwargs)
#     return wrapper
'''
2024-03-01 22:07:09,695 - DEBUG - Called function: sample_function with args: (1, 2) and kwargs: {'c': 3}
Executing sample_function with a=1, b=2, and c=3
'''


# 파라미터 타입도 추가해서 로깅하는 데코레이터
def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # args와 kwargs에서 각 파라미터의 타입을 추출합니다.
        args_with_types = [(arg, type(arg).__name__) for arg in args]
        kwargs_with_types = {k: (v, type(v).__name__) for k, v in kwargs.items()}
        
        # 함수 이름, 파라미터와 그 타입을 로깅합니다.
        logging.debug(f"Called function: {func.__name__} with args: {args_with_types} and kwargs: {kwargs_with_types}")
        
        # 원래 함수 호출
        return func(*args, **kwargs)
    return wrapper
'''
2024-03-01 22:09:41,827 - DEBUG - Called function: sample_function with args: [(1, 'int'), (2, 'int')] and kwargs: {'c': (3, 'int')}
Executing sample_function with a=1, b=2, and c=3
'''


@log_function_call
def sample_function(a, b, c=None):
    print(f"Executing sample_function with a={a}, b={b}, and c={c}")

# 함수 호출로 로그 확인
sample_function(1, 2, c=3)
