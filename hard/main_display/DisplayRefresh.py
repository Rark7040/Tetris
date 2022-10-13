from hard.U74HC595AG import U74HC595AG


# 2つカスケード接続されたu74hc595ag
class DisplayRefresh(U74HC595AG):
    update_cnt: int = 0

    def __init__(self, ser: int, sck: int, rck: int):
        self.ser: int = ser
        self.sck: int = sck
        self.rck: int = rck

    def shift(self):
        pass

    def serial_input(self, sig: bool):
        pass

    def latch(self):
        pass

    def update(self):
        pass
