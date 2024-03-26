#System Log (Printed and Logged):
import logging
import datetime
import sys

# Configure the logger
current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
log_file = 'system_{}.log'.format(current_time)

logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Add a handler to print logs to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
logging.getLogger().addHandler(console_handler)

# Log a system event
logging.info('System event: System initialized successfully.')


#Function Execution Log (Printed and Logged):
import logging
import datetime

# Configure the logger
current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
func_log_file = 'function_execution_{}.log'.format(current_time)

# Configure the logger
logging.basicConfig(filename=func_log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Add a handler to print logs to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
logging.getLogger().addHandler(console_handler)

def my_function():
    logging.info(sys._getframe(0).f_code.co_name)    
    try:
        # Function logic here
        result = 10 / 0  # Simulating a failure for demonstration
        logging.info('Function executed successfully. Result: {}'.format(result))
    except Exception as e:
        logging.error('Function 111 execution failed: {}'.format(str(e)), exc_info=True)

my_function()

def my_function_2():
    logging.info(sys._getframe(0).f_code.co_name)    
    try:
        # Function logic here
        result = 10 / 2  # Simulating a failure for demonstration
        logging.info('Function executed successfully. Result: {}'.format(result))
    except Exception as e:
        logging.error('Function 222 execution failed: {}'.format(str(e)), exc_info=True)

my_function_2()

#Error Log (Printed and Logged):
import logging
import datetime

# Configure the logger
current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
error_log_file = 'error_{}.log'.format(current_time)

# Configure the logger
logging.basicConfig(filename=error_log_file, level=logging.ERROR, format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Add a handler to print logs to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
logging.getLogger().addHandler(console_handler)

try:
    # Code that might raise an error
    result = 10 / 0  # Simulating an error for demonstration
except Exception as e:
    logging.error('An error occurred: {}'.format(str(e)), exc_info=True)
