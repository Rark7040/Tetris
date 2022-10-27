from enum import Enum


# GPIO numbers
class RPiConfig(Enum):
    # DisplayRefresh
    DISREF_SER: int = 0
    DISREF_SCK: int = 0
    DISREF_RCK: int = 0

    # RenderController
    RENCON_SER: int = 0
    RENCON_SCK: int = 0
    RENCON_RCK: int = 0

    # Buttons
    BUTTON_RIGHT_ROTATE: int = 0
    BUTTON_LEFT_ROTATE: int = 0
    BUTTON_RIGHT_MOVE: int = 0
    BUTTON_LEFT_MOVE: int = 0
    BUTTON_DOWN_MOVE: int = 0
    BUTTON_RESET: int = 0
