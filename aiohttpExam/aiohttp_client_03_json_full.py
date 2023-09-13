import aiohttp
import asyncio
import requests

async def fetch_url(url):
    """
        ClientSession() 은 aiohttp의 핵심 클래스이다.
        이 클래스는 HTTP 클라이언트의 상태를 유지하고, 쿠키를 저장하고, 리다이렉션을 처리하고,
        기본 인증을 지원하며, 프록시를 지원하며, 기타 많은 기능을 제공한다.
        이 클래스는 단일 웹 서버에 대한 모든 요청을 처리하는 데 사용할 수 있다.
    """
    async with aiohttp.ClientSession() as session:
        # get() 메소드는 GET 요청을 보내고, 응답을 기다린다.
        async with session.get(url) as response:
            return await response.text()

async def fetch_device_info(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main():
    url = "http://localhost:8080"  # Assuming the server is running locally on port 8080
    response = await fetch_url(url)
    print("Server Response:", response)
    
    #server response: Hello, this is second handle!
    second_url = "http://localhost:8080/second"
    response = await fetch_url(second_url)
    print("Server Response seconde :", response)

    # Fetching DeviceInfo from the '/getDeviceInfo' endpoint
    device_info_url = "http://localhost:8080/getDeviceInfo"
    device_info = await fetch_device_info(device_info_url)
    print("Device Info:", device_info)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

