import asyncio
import time


async def async_loop(x: list[int]):
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, test, x)
    # print(x)


def test(x: list[int]):
    for i in range(10):
        time.sleep(0.01)
        x.append(i)


arr = []
asyncio.get_event_loop().run_until_complete(async_loop(arr))

print(arr)
time.sleep(3)
print(arr)
