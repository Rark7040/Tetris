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

    def get_all_pin(self) -> list:
        return [
            self.DISREF_SER,
            self.DISREF_SCK,
            self.DISREF_RCK,
            self.RENCON_SER,
            self.RENCON_SCK,
            self.RENCON_RCK
            # TODO write members
        ]
