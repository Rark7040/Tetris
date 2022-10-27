import asyncio
import time


class ListHolder:
    x: list[int] = []


async def async_loop(holder: ListHolder):
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, test, holder)
    # print(x)


def test(holder: ListHolder):
    for i in range(10):
        time.sleep(0.01)
        holder.x.append(i)


list_holder = ListHolder()
asyncio.get_event_loop().run_until_complete(async_loop(list_holder))

print(list_holder.x)
time.sleep(3)
print(list_holder.x)
