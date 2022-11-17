from __future__ import annotations
import copy


class BitBlock:
    def __init__(self):
        # horizontally bits
        self.bits: list[int] = []

    def set(self, b: int, idx: int | None = None):
        if b < 0b1:
            raise ValueError("this func is expect int of more then 0, was given " + b.__str__() + '('+bin(b)+')')

        if idx is None:
            self.bits.append(b)
            return

        try:
            self.bits[idx] = b

        except IndexError:
            self.bits.append(b)

    def get(self, idx: int, fallback: int | None = None) -> int | None:
        try:
            return self.bits[idx]

        except IndexError:
            return fallback

    def get_all_bits(self) -> list[int]:
        return self.bits

    def get_cloning_bits(self) -> list[int]:
        return copy.deepcopy(self.bits)

    def rotate_to_left(self) -> BitBlock:
        result: BitBlock = BitBlock()

        for b in self.get_cloning_bits():
            i: int = 0

            while b != 0b1:
                stored_b = result.get(i, 0b1)
                stored_b = (stored_b << 1) | (0b1 & b)
                b = b >> 1
                result.set(stored_b, i)
                i += 1

        return result
