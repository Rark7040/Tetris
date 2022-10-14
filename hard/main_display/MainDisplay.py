from hard.main_display.DisplayRefresh import DisplayRefresh
from hard.main_display.RenderController import RenderController
from hard.RPiConf import RPiConf


class MainDisplay:
    MAX_X_LINE: int = 8
    MAX_Y_LINE: int = 14

    def __init__(self):
        conf: RPiConf = RPiConf()
        self.disref: DisplayRefresh = DisplayRefresh(conf.DISREF_SER, conf.DISREF_SCK, conf.DISREF_RCK)
        self.rencon: RenderController = RenderController(conf.RENCON_SER, conf.RENCON_SCK, conf.RENCON_RCK)

    def on_update(self):
        # TODO refresh
        # TODO render control
        pass  # every ticks
