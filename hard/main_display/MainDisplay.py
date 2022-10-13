from hard.main_display.DisplayRefresh import DisplayRefresh
from hard.main_display.RenderController import RenderController


class MainDisplay:
    MAX_X_LINE = 8
    MAX_Y_LINE = 14

    def __init__(self):
        self.disref = DisplayRefresh
        self.rencon = RenderController

    def on_update(self):
        # TODO refresh
        # TODO render control
        pass  # every ticks
