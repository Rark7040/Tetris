import asyncio
import time
import RPi.GPIO as GPIO

from src.hard.RPiConfig import RPiConfig
from src.hard.ui.Buttons import Buttons
from src.hard.ui.UserResponse import UserResponse


class AsyncButtonListener:
    def __init__(self, response: UserResponse):
        self.response = response

    async def async_loop(self):
        loop = asyncio.get_event_loop()
        loop.run_in_executor(None, self.listen)

    def listen(self):
        while True:
            time.sleep(0.05)
            self.__check_button(Buttons.RIGHT_ROTATE, RPiConfig.BUTTON_RIGHT_ROTATE)
            self.__check_button(Buttons.LEFT_ROTATE, RPiConfig.BUTTON_LEFT_ROTATE)
            self.__check_button(Buttons.RIGHT_MOVE, RPiConfig.BUTTON_RIGHT_MOVE)
            self.__check_button(Buttons.LEFT_MOVE, RPiConfig.BUTTON_LEFT_MOVE)
            self.__check_button(Buttons.DOWN_MOVE, RPiConfig.BUTTON_DOWN_MOVE)
            self.__check_button(Buttons.RESET, RPiConfig.BUTTON_RESET)

    def __check_button(self, button: int, gpio: int):
        is_pressed = GPIO.input(gpio) == 0  # TODO: 動作確認

        if is_pressed:
            self.response.write(button)

        else:
            self.response.clear(button)
