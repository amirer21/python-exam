import logging
from functools import wraps
import datetime

# 현재 시간을 포함한 로그 파일 이름 생성
current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = f"logs_{current_time}.log"

# 로깅 기본 설정: 디버그 레벨로 설정하고, 파일에 출력되도록 합니다.
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename=log_filename,
                    filemode='w')  # 파일 모드: 새로 쓰기 ('w'), 이어 쓰기 ('a')

# 전역 카운터 초기화
function_call_order = 0

#global function_call_order

def log_function_call_with_order(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global function_call_order
        function_call_order += 1  # 함수 호출 시 카운터 증가
        
        # args와 kwargs에서 각 파라미터의 타입을 추출
        args_with_types = [(arg, type(arg).__name__) for arg in args]
        kwargs_with_types = {k: (v, type(v).__name__) for k, v in kwargs.items()}
        
        # 함수 이름, 순서, 파라미터와 그 타입을 로깅
        logging.debug(f"#{function_call_order} Called function: {func.__name__} with args: {args_with_types} and kwargs: {kwargs_with_types}")
        
        return func(*args, **kwargs)
    return wrapper



@log_function_call_with_order
def sample_function(a, b, c=None):
    print(f"Executing sample_function with a={a}, b={b}, and c={c}")

@log_function_call_with_order
def another_function(x):
    print(f"Executing another_function with x={x}")

# 함수 호출로 로그 확인
another_function("hello")
sample_function(1, 'test', c=3.14)
another_function("hello")
another_function("hello")
sample_function(2, 'example', c=None)