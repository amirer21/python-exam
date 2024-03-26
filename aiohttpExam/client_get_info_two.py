import aiohttp
import asyncio

async def fetch_server_info(server_id, host, port):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://{host}:{port}/server_info') as response:
            if response.status == 200:
                server_info = await response.json()
                print(f"Server {server_id} Information:")
                print("Server ID:", server_info['server_id'])
                print("Host:", server_info['host'])
                print("Port:", server_info['port'])
                print("Message:", server_info['message'])
            else:
                print(f"Error: Unable to retrieve information for Server {server_id}")

async def main():
    server_info_tasks = [
        fetch_server_info(1, '127.0.0.1', 8081),  # Server 1
        fetch_server_info(2, '127.0.0.1', 8082)  # Server 2
    ]

    await asyncio.gather(*server_info_tasks)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
