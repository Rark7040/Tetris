from enum import Enum


class Buttons(Enum):

    # 1 is pressed, 0 is released
    RIGHT_ROTATE: int = 0b1
    LEFT_ROTATE: int = 0b10
    RIGHT_MOVE: int = 0b100
    LEFT_MOVE: int = 0b1000
    DOWN_MOVE: int = 0b1_0000
    RESET: int = 0b10_0000
