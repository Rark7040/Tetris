from hard.main_display.MainDisplay import MainDisplay
from hard.ui.AsyncButtonListener import AsyncButtonListener
from hard.ui.UserResponse import UserResponse


class Hard:
    def __init__(self):
        self.main_display: MainDisplay = MainDisplay()
        self.response: UserResponse = UserResponse()
        self.button_listener: AsyncButtonListener = AsyncButtonListener(self.response)

    def get_main_display(self) -> MainDisplay:
        return self.main_display

    def get_user_response(self) -> UserResponse:
        return self.response
