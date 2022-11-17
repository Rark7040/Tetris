import asyncio

from hard.main_display.DisplayRefresh import DisplayRefresh
from hard.main_display.RenderController import RenderController
from hard.RPiConfig import RPiConfig


class MainDisplay:
    MAX_X_LINE: int = 8
    MAX_Y_LINE: int = 14

    def __init__(self):
        self.is_display_completed: bool = True
        self.displaying: list[int] = []
        self.displayed_lines = 0
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
        self.is_display_completed = False

    def __display_line(self):
        try:
            line = self.displaying[self.displayed_lines]

        except IndexError:
            self.is_display_completed = True
            return

        self.rencon.input_bit(line | 0b1_0000_0000)
        self.displayed_lines += 1

    async def async_loop(self):
        loop = asyncio.get_event_loop()
        loop.run_in_executor(None, self.update)

    def update(self):
        while True:
            if self.is_display_completed:
                # 画面のちらつき防止のため、描画対象がない場合は最後に描画したものを描画し続けます
                self.is_display_completed = False
                self.displayed_lines = 0
            # TODO じゅんばん逆かも
            self.disref.update()
            self.__display_line()
