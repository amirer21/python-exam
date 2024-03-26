import aiohttp
import asyncio

async def make_request():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:8080') as response:
            if response.status == 200:
                return await response.text()
            else:
                return f"Error: {response.status}"

async def main():
    response = await make_request()
    print("Response:", response)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
