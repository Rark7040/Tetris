from hard.U74HC595AG import U74HC595AG


# td62003apgをラップするu74hc595ag
class RenderController(U74HC595AG):

    def __init__(self, ser: int, sck: int, rck: int):
        self.ser = ser
        self.sck = sck
        self.rck = rck

    def shift(self):
        pass

    def serial_input(self, sig: bool):
        pass

    def latch(self):
        pass

