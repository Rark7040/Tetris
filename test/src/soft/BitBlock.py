from __future__ import annotations
import copy


class BitBlock:
    def __init__(self):
        # horizontally bits
        self.__bits: list[int] = []

    def set(self, b: int, idx: int | None = None):
        if b < 0b1:
            raise ValueError("this func is expect int of more then 0, was given " + b.__str__() + '('+bin(b)+')')

        if idx is None:
            self.__bits.append(b)
            return

        try:
            self.__bits[idx] = b

        except IndexError:
            self.__bits.append(b)

    def get(self, idx: int, fallback: int | None = None) -> int | None:
        try:
            return self.__bits[idx]

        except IndexError:
            return fallback

    def get_all_bits(self) -> list[int]:
        return self.__bits

    def get_cloning_bits(self) -> list[int]:
        return copy.deepcopy(self.__bits)

    def rotate_to_left(self) -> BitBlock:
        result: BitBlock = BitBlock()

        for b in self.get_cloning_bits():
            i: int = 0

            while b != 0b1:
                result.set((result.get(i, 0b1) << 1) | (0b1 & b), i)
                b = b >> 1
                i += 1

        return result
