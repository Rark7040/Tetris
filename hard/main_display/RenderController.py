from hard.U74HC595AG import U74HC595AG


# td62003apgをラップするu74hc595ag
class RenderController(U74HC595AG):
    MAX_BUS_PORT: int = 8

    # 9bit二進数を受け付けます 一番最後のbitは無視されます
    def input_bit(self, pattern: int):
        self.clear()

        while pattern != 0b1:
            dump = pattern & 0b1
            self.serial_input(True if dump == 0b1 else False)
            self.shift()
            pattern = pattern >> 1
