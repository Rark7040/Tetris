import copy


class BitBlock:
    bits: list[int] = []

    def get_all(self) -> list[int]:
        return self.bits

    def get_cloning_bits(self) -> list[int]:
        return copy.deepcopy(self.bits)

    def to_horizontal(self) -> list[int]:
        bits: list[int] = self.get_cloning_bits()
        tmp_bits: list[int] = []


