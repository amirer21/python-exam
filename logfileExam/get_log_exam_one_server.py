import logging
import aiohttp
from aiohttp import web
import asyncio
import datetime
import sys

# Configure loggers
current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

def configure_logger(log_filename, log_level=logging.INFO):
    logging.basicConfig(filename=log_filename, level=log_level, format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    
    # Add a handler to print logs to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
    logging.getLogger().addHandler(console_handler)
    
# System Log
system_log_file = f'system_{current_time}.log'
configure_logger(system_log_file)
logging.info('System event: System initialized successfully.')

# Function Log
# 이 부분은 함수가 실행될 때마다 로그 파일이 생성되는 것을 방지하기 위해
# 함수가 실행될 때마다 로그 파일을 생성하는 것이 아니라
# 로그 파일을 생성하는 함수를 따로 만들어서 사용한다.
func_log_file = f'function_{current_time}.log'
configure_logger(func_log_file)
def log_function_execution(func_name, success=True, result=None, error=None):    
    log_message = f'Function {func_name} executed {"successfully" if success else "unsuccessfully"}'
    if result is not None:
        log_message += f'. Result: {result}'
    if error:
        log_message += f'. Error: {str(error)}'
    logging.info(log_message)

async def handle(request):
    func_name = sys._getframe(0).f_code.co_name
    log_function_execution(func_name)

    try:
        # Simulate some async logic here
        await asyncio.sleep(2)
        return web.Response(text="Request handled successfully!")
    except Exception as e:
        log_function_execution(func_name, success=False, error=e)
        return web.Response(text="Internal Server Error", status=500)

app = web.Application()
app.router.add_get('/', handle)

if __name__ == '__main__':
    web.run_app(app)
