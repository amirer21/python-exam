import aiohttp
from aiohttp import web

async def handle(request):
    return web.Response(text="Hello, this is the server!")

async def handle_second(request):
    return web.Response(text="Hello, this is second handle!")

# 실제로 서버에서는 여러 라우터를 추가할 수 있다.
# 라우터는 URL 경로와 핸들러 함수를 매핑하는 역할을 한다.
# 라우터를 추가할 때는 add_get() 메서드를 사용한다.
# add_get() 메서드는 GET 요청을 처리하는 핸들러를 추가한다.
# 첫 번째 인자는 URL 경로이고, 두 번째 인자는 핸들러 함수이다.

app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/second', handle_second)

# Set the desired domain and port
host = '0.0.0.0'  # Listen on all available network interfaces
port = 8080

web.run_app(app, host=host, port=port)