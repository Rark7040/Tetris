import asyncio
import time

from hard.ui.UserResponse import UserResponse


# HACK: 普通にやばい書き方してるからいい方法が見つかり次第修正
class AsyncButtonListener:

    def __init__(self, response: UserResponse):
        self.response = response

    async def async_loop(self):
        loop = asyncio.get_event_loop()
        loop.run_in_executor(None, self.listen)

    def listen(self):
        while True:
            time.sleep(0.05)
            # TODO: check buttons state
