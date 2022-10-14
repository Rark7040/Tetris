from hard.main_display.DisplayRefresh import DisplayRefresh
from hard.main_display.RenderController import RenderController
from hard.RPiConf import RPiConf


class MainDisplay:
    MAX_X_LINE: int = 8
    MAX_Y_LINE: int = 14

    def __init__(self):
        self.disref: DisplayRefresh = DisplayRefresh(RPiConf.DISREF_SER, RPiConf.DISREF_SCK, RPiConf.DISREF_RCK)
        self.rencon: RenderController = RenderController(RPiConf.RENCON_SER, RPiConf.RENCON_SCK, RPiConf.RENCON_RCK)

    def on_update(self):
        # TODO refresh
        # TODO render control
        pass  # every ticks
