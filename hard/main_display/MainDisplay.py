from hard.main_display.DisplayRefresh import DisplayRefresh
from hard.main_display.RenderController import RenderController
from hard.RPiConfig import RPiConfig


class MainDisplay:
    MAX_X_LINE: int = 8
    MAX_Y_LINE: int = 14
    is_display_completed: bool = True
    displaying: list[int] = []
    displayed_lines = 0

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

    def display(self, pattern: list[int]):
        self.displaying = pattern
        self.displayed_lines = 0

    def on_update(self):
        self.disref.update()
        # TODO render control

        pass  # every ticks
