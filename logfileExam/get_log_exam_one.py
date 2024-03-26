import logging
import datetime
import sys


# 이 함수는 로그 파일을 생성하는 함수이다.
def configure_logger(log_filename, log_level=logging.INFO):
    logging.basicConfig(filename=log_filename, level=log_level, format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    
    # Add a handler to print logs to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
    logging.getLogger().addHandler(console_handler)

# 이 함수는 함수가 실행될 때마다 로그 파일을 생성하는 것을 방지하기 위해 만든 함수이다.
def log_function_execution(func_name, success=True, result=None, error=None):
    log_message = f'Function {func_name} executed {"successfully" if success else "unsuccessfully"}'
    if result is not None:
        log_message += f'. Result: {result}'
    if error:
        log_message += f'. Error: {str(error)}'
    logging.info(log_message)

# System Log
current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
system_log_file = f'system_{current_time}.log'
configure_logger(system_log_file)
logging.info('System event: System initialized successfully.')

# Function 1
func_log_file_1 = f'function_1_{current_time}.log'
configure_logger(func_log_file_1)
def my_function():
    func_name = sys._getframe(0).f_code.co_name
    log_function_execution(func_name)
    try:
        # Function logic here
        result = 10 / 0  # Simulating a failure for demonstration
        log_function_execution(func_name, result=result)
    except Exception as e:
        log_function_execution(func_name, success=False, error=e)

my_function()

# Function 2
func_log_file_2 = f'function_2_{current_time}.log'
configure_logger(func_log_file_2)
def my_function_2():
    func_name = sys._getframe(0).f_code.co_name
    log_function_execution(func_name)
    try:
        # Function logic here
        result = 10 / 2  # Simulating a failure for demonstration
        log_function_execution(func_name, result=result)
    except Exception as e:
        log_function_execution(func_name, success=False, error=e)

my_function_2()

# Error Log
error_log_file = f'error_{current_time}.log'
configure_logger(error_log_file, log_level=logging.ERROR)
try:
    # Code that might raise an error
    result = 10 / 0  # Simulating an error for demonstration
except Exception as e:
    logging.error(f'An error occurred: {str(e)}', exc_info=True)
