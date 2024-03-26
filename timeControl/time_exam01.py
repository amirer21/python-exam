import time
import datetime
import asyncio

async def delayed_connection_message():
    print("Connecting...")
    # 비동기적으로 3초 대기
    await asyncio.sleep(3)
    return "Connection successful"

async def check_connection():
    print("Checking connection...")
    while True:  # 무한 루프로 상태 확인
        print(f"Time: {datetime.datetime.now()}")
        result = await delayed_connection_message()  # 비동기 함수 호출 및 결과 대기
        if result == "Connection successful":
            print("Success")
            break  # 조건 충족 시 루프 종료
        else:
            print("Checking again...")
            await asyncio.sleep(1)  # 비동기적으로 잠시 대기

# 비동기 함수 실행을 위한 이벤트 루프
async def main():
    await check_connection()

    
if __name__ == "__main__":
    asyncio.run(main())
    