import asyncio
from abc import ABCMeta
from enum import Enum

# GPIO numbers
from RPi import GPIO


class RPiConfig(Enum):
    # DisplayRefresh
    DISREF_SER: int = 4
    DISREF_SCK: int = 2
    DISREF_RCK: int = 3

    # RenderController
    RENCON_SER: int = 18
    RENCON_SCK: int = 14
    RENCON_RCK: int = 15

    # Buttons
    BUTTON_RIGHT_ROTATE: int = 0
    BUTTON_LEFT_ROTATE: int = 0
    BUTTON_RIGHT_MOVE: int = 0
    BUTTON_LEFT_MOVE: int = 0
    BUTTON_DOWN_MOVE: int = 0
    BUTTON_RESET: int = 0


class U74HC595AG(metaclass=ABCMeta):
    MAX_BUS_PORT: int = 0

    def __init__(self, ser: int, sck: int, rck: int):
        self.ser: int = ser
        self.sck: int = sck
        self.rck: int = rck
        print(self.ser, self.sck, self.rck)

    def shift(self):  # SCK
        GPIO.output(self.sck, GPIO.HIGH)
        GPIO.output(self.sck, GPIO.LOW)

    def serial_input(self, sig: bool):  # SER
        GPIO.output(self.ser, GPIO.HIGH if sig else GPIO.LOW)

    def latch(self):  # RCK
        GPIO.output(self.rck, GPIO.HIGH)
        GPIO.output(self.rck, GPIO.LOW)

    # TODO 後程基板設計を変えて簡略化したい
    def clear(self):
        for _ in range(self.MAX_BUS_PORT):
            self.serial_input(False)
            self.shift()

        self.latch()


class DisplayRefresh(U74HC595AG):
    MAX_BUS_PORT: int = 16
    USE_BUS_PORT: int = 14

    def __init__(self, ser: int, sck: int, rck: int):
        super().__init__(ser, sck, rck)
        self.pos: int = 1
        self.serial_input(True)
        self.latch()

    def update(self):
        self.pos += 1

        if self.pos > self.USE_BUS_PORT:
            self.pos = 1
            self.clear()
            self.serial_input(True)
            self.latch()

        else:
            self.shift()

        self.latch()


class RenderController(U74HC595AG):
    MAX_BUS_PORT: int = 8

    # 9bit二進数を受け付けます 一番最後のbitは無視されます
    def input_bit(self, pattern: int):
        self.clear()

        while pattern != 0b1:
            dump = pattern & 0b1
            self.serial_input(True if dump == 0b1 else False)
            self.shift()
            pattern = pattern >> 1


class MainDisplay:
    MAX_X_LINE: int = 8
    MAX_Y_LINE: int = 14

    def __init__(self):
        self.is_display_completed: bool = True
        self.displaying: list[int] = []
        self.displayed_lines = 0
        self.disref: DisplayRefresh = DisplayRefresh(
            RPiConfig.DISREF_SER,
            RPiConfig.DISREF_SCK,
            RPiConfig.DISREF_RCK
        )
        self.rencon: RenderController = RenderController(
            RPiConfig.RENCON_SER,
            RPiConfig.RENCON_SCK,
            RPiConfig.RENCON_RCK
        )

    def display(self, pattern: list[int]):
        self.displaying = pattern
        self.displayed_lines = 0
        self.is_display_completed = False

    def __display_line(self):
        try:
            line = self.displaying[self.displayed_lines]

        except IndexError:
            self.is_display_completed = True
            return

        self.rencon.input_bit(line | 0b1_0000_0000)
        self.displayed_lines += 1

    async def async_loop(self):
        loop = asyncio.get_event_loop()
        loop.run_in_executor(None, self.update)

    def update(self):
        while True:
            if self.is_display_completed:
                # 画面のちらつき防止のため、描画対象がない場合は最後に描画したものを描画し続けます
                self.is_display_completed = False
                self.displayed_lines = 0
            # TODO じゅんばん逆かも
            self.disref.update()
            self.__display_line()


display = MainDisplay()
display.display(
    [
        0b_1111_1111,
        0b_1111_1111,
        0b_1111_1111,
        0b_1111_1111,
        0b_1111_1111,
        0b_1111_1111,
        0b_1111_1111,

        0b_1111_1111,
        0b_1111_1111,
        0b_1111_1111,
        0b_1111_1111,
        0b_1111_1111,
        0b_1111_1111,
        0b_1111_1111,
    ]
)
print("!!")
asyncio.get_event_loop().run_until_complete(display.async_loop())
