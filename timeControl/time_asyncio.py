import asyncio

async def delayed_connection_message():
    print("Connecting...")
    await asyncio.sleep(5)  # 비동기적으로 5초 대기
    return "Connection successful"

async def check_connection():
    print("Checking connection...")
    try:
        # asyncio.wait_for을 사용하여 delayed_connection_message 호출 시 3초 타임아웃 설정
        result = await asyncio.wait_for(delayed_connection_message(), timeout=3)
        if result == "Connection successful":
            print("Success")
    except asyncio.TimeoutError:
        # 타임아웃 발생 시 출력
        print("Connect error - Operation timed out")

async def main():
    await check_connection()

if __name__ == "__main__":
    asyncio.run(main())