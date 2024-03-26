from aiohttp import web
import json

async def get_server_info(request):
    app = request.app
    server_info = {
        'host': app['host'],
        'port': app['port'],
        'message': 'Server running successfully'
    }
    return web.json_response(server_info)

app = web.Application()
app['host'] = '127.0.0.1'
app['port'] = 8080

app.router.add_get('/server_info', get_server_info)

if __name__ == '__main__':
    web.run_app(app)
