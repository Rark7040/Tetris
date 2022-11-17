from hard.U74HC595AG import U74HC595AG


# 2つカスケード接続されたu74hc595ag
class DisplayRefresh(U74HC595AG):
    MAX_BUS_PORT: int = 16
    USE_BUS_PORT: int = 14

    def __init__(self, ser: int, sck: int, rck: int):
        super().__init__(ser, sck, rck)
        self.pos: int = 1
        self.__serial_input(True)
        self.__latch()

    def update(self):
        self.pos += 1

        if self.pos > self.USE_BUS_PORT:
            self.pos = 1
            self.clear()
            self.__serial_input(True)
            self.__latch()

        else:
            self.__shift()

        self.__latch()
        pass
