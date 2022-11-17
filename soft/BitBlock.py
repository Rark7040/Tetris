import copy


class BitBlock:
    def __init__(self):
        # horizontally bits
        self.bits: list[int] = []

    def set(self, b: int):
        self.bits.append(b)

    def get_all(self) -> list[int]:
        return self.bits

    def get_cloning_bits(self) -> list[int]:
        return copy.deepcopy(self.bits)

    def rotate_to_left(self) -> list[int]:
        bits: list[int] = self.get_cloning_bits()
        tmp_bits: list[int] = []

        for b in bits:
            i: int = 0

            while b != 0b1:
                try:
                    stored_b = tmp_bits[i]

                except IndexError:
                    stored_b = 0b1

                stored_b = (stored_b << 1) | (0b1 & b)
                b = b >> 1

                try:
                    tmp_bits[i] = stored_b

                except IndexError:
                    tmp_bits.append(stored_b)
                i += 1

        return tmp_bits





