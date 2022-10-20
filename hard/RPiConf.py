from enum import Enum


class RPiConf(Enum):
    def __init__(self):
        pass

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

    def get_all_pin(self) -> list:
        return [
            self.DISREF_SER,
            self.DISREF_SCK,
            self.DISREF_RCK,
            self.RENCON_SER,
            self.RENCON_SCK,
            self.RENCON_RCK,
            self.BUTTON_RIGHT_ROTATE,
            self.BUTTON_LEFT_ROTATE,
            self.BUTTON_RIGHT_MOVE,
            self.BUTTON_LEFT_MOVE,
            self.BUTTON_DOWN_MOVE,
            self.BUTTON_RESET
            # TODO write members
        ]
