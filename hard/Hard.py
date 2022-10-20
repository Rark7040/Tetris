from hard.main_display.MainDisplay import MainDisplay
from hard.ui.Buttons import Buttons


class Hard:
    def __init__(self):
        self.main_display: MainDisplay = MainDisplay()
        self.buttons: Buttons = Buttons()

    def get_main_display(self) -> MainDisplay:
        return self.main_display

    def get_buttons(self) -> Buttons:
        return self.buttons
