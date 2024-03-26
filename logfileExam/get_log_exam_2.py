import logging
import sys

# Configure the logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# System Log
logging.info('System event: System initialized successfully.')

# Function Log
def my_function():
    func_name = sys._getframe(0).f_code.co_name
    logging.info(f'Function {func_name} is being executed.')
    try:
        # Function logic here
        result = 10 / 2  # Simulating a successful execution
        logging.info(f'Function {func_name} executed successfully. Result: {result}')
    except Exception as e:
        logging.error(f'Function {func_name} execution failed: {str(e)}')

my_function()

# Error Log
try:
    # Code that might raise an error
    result = 10 / 0  # Simulating an error for demonstration
except Exception as e:
    logging.error(f'An error occurred: {str(e)}')
