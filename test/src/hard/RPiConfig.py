from enum import Enum


# GPIO numbers
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
