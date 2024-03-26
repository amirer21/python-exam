import aiohttp
import asyncio

#async 키워드가 함수 앞에 붙으면 그 함수는 비동기 함수가 된다.
#await 는 비동기 함수를 호출할 때 사용하는 키워드이다.
#await 키워드는 비동기 함수를 호출하고 그 함수의 실행이 완료될 때까지 기다린다.
#async with : async with 블록을 사용하면 with 블록 안의 코드를 비동기로 실행할 수 있다.
async def fetch_server_info():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:8080/server_info') as response:
            if response.status == 200:
                return await response.json()

async def main():
    server_info = await fetch_server_info()
    print("Server Information:", server_info)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
