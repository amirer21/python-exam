from aiohttp import web
import json

async def get_server_info(request):
    app = request.app
    server_info = {
        'server_id': app['server_id'],
        'host': app['host'],
        'port': app['port'],
        'message': 'Server running successfully'
    }
    return web.json_response(server_info)

# Server 2
app2 = web.Application()
app2['server_id'] = 2
app2['host'] = '127.0.0.1'
app2['port'] = 8082
app2.router.add_get('/server_info', get_server_info)

if __name__ == '__main__':
    web.run_app(app2, port=app2['port'])
