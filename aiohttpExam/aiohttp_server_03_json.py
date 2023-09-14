import aiohttp
from aiohttp import web
import platform
import uiautomation as winapi
import os
import json  # Import the json module

async def handle(request):
    return web.Response(text="Hello, this is the server!")

async def handle_second(request):
    return web.Response(text="Hello, this is second handle!")

# 서버에서 JSON을 반환하는 예제이다.
# platform 모듈을 사용하여 서버의 운영체제 정보를 JSON으로 반환한다.
# uiAutomation 모듈을 사용하여 서버의 정보를 JSON으로 반환한다.
# json 객체 : get_device_info 함수에서 반환하는 딕셔너리를 JSON으로 변환한다.
async def get_device_info(request):
    width, height = winapi.GetScreenSize()
    info = {
        'screen_width': width,
        'screen_height': height,
        'platform': platform.system(),
        'platform_version': platform.machine(),
        'product_model': platform.node(),
        'build_target_country': os.environ.get("LANG", "INT"),
        'build_version_release': platform.release(),
        'hw_revision': platform.processor(),
        'revision': platform.version(),
        'os_version': platform.release(),
    }
    # Set the Content-Type header to application/json
    return web.json_response(info)

app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/second', handle_second)
app.router.add_get('/getDeviceInfo', get_device_info)

# Set the desired domain and port
host = '0.0.0.0'  # Listen on all available network interfaces
port = 8080

web.run_app(app, host=host, port=port)