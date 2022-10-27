from hard.main_display.DisplayRefresh import DisplayRefresh
from hard.main_display.RenderController import RenderController
from hard.RPiConfig import RPiConfig


class MainDisplay:
    MAX_X_LINE: int = 8
    MAX_Y_LINE: int = 14

    def __init__(self):
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

    def on_update(self):
        # TODO refresh
        # TODO render control

        pass  # every ticks
