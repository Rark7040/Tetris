import asyncio
import time


class ListHolder:
    def __init__(self):
        self.x: int = 0b0


async def async_loop(holder: ListHolder):
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, test, holder)


def test(holder: ListHolder):
    time.sleep(0.01)
    holder.x |= 0b1


list_holder = ListHolder()
asyncio.get_event_loop().run_until_complete(async_loop(list_holder))

print(list_holder.x)
time.sleep(1)
print(list_holder.x)
