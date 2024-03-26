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

# Server 1
app1 = web.Application()
app1['server_id'] = 1
app1['host'] = '127.0.0.1'
app1['port'] = 8081
app1.router.add_get('/server_info', get_server_info)

if __name__ == '__main__':
    web.run_app(app1, port=app1['port'])
