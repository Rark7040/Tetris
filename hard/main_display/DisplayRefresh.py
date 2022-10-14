from hard.U74HC595AG import U74HC595AG


# 2つカスケード接続されたu74hc595ag
class DisplayRefresh(U74HC595AG):
    def shift(self):
        pass

    def serial_input(self, sig: bool):
        pass

    def latch(self):
        pass