#import aiohttp
from aiohttp import web

'''
# aiohttp란? 
aiohttp란 파이썬에서 비동기 웹 서버를 개발할 수 있게 해주는 라이브러리이다.

# asyncio란
aiohttp는 asyncio를 기반으로 만들어졌다. asyncio는 비동기 프로그래밍을 위한 라이브러리이다.
asyncio는 이벤트 루프를 사용하여 비동기 프로그래밍을 한다.
이벤트 루프는 이벤트를 받고, 처리하는 역할을 한다.

간단한 aiohttp 서버와 클라이언트를 만들어보자.

#aiohttp web
aiohttp의 web은 다음과 같은 클래스를 제공한다.
Application, Request, Response, StreamResponse, WebSocketResponse
여기서는 Application 클래스를 사용했다.

#aiohttp web Application
Application은 웹 애플리케이션을 나타내는 클래스이다.
Application 클래스는 다음과 같은 메소드를 제공한다.
router : 라우터는 URL 경로를 보고 어떤 핸들러를 실행할지 결정한다.
router.add_get() : GET 요청을 처리하는 핸들러를 추가한다.
형식은 다음과 같다.
- add_get(path, handler, *, name=None, expect_handler=None)
run_app() : 애플리케이션을 실행한다.

aiohttp는 다음과 같은 핸들러를 제공한다.
GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS
여기서는 GET 요청을 처리하는 핸들러를 추가했다.
'''

async def handle(request):
    return web.Response(text="Hello, this is the server!")

app = web.Application()
app.router.add_get('/', handle)

web.run_app(app)