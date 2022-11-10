import asyncio

from hard.main_display.MainDisplay import MainDisplay
from hard.ui.AsyncButtonListener import AsyncButtonListener
from hard.ui.UserResponse import UserResponse


# TODO: ハード制御用のスレッドを生成
class Hard:
    def __init__(self):
        self.main_display: MainDisplay = MainDisplay()
        self.response: UserResponse = UserResponse()
        self.button_listener: AsyncButtonListener = AsyncButtonListener(self.response)

    def __run_asynces(self):
        asyncio.get_event_loop().run_until_complete(self.button_listener.async_loop())
        asyncio.get_event_loop().run_until_complete(self.main_display.async_loop())

    def get_main_display(self) -> MainDisplay:
        return self.main_display

    def get_user_response(self) -> UserResponse:
        return self.response
