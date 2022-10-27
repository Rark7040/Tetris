from enum import Enum


class Buttons(Enum):

    # 1 is pressed, 0 is released
    RIGHT_ROTATE: int = 0b1
    LEFT_ROTATE: int = 0b01
    RIGHT_MOVE: int = 0b001
    LEFT_MOVE: int = 0b0001
    DOWN_MOVE: int = 0b00001
    RESET: int = 0b000001
