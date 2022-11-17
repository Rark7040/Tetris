from soft.BitBlock import BitBlock
from soft.FallingBlock import FallingBlock


class MainDisplay(BitBlock):
    MAX_X_LINE: int = 8
    MAX_Y_LINE: int = 13 # idx is start from 0
    GATE_X: int = round(MAX_X_LINE / 2)
    GATE_Y: int = 0

    def __init__(self):
        super().__init__()
        self.falling_blocks: list[FallingBlock] = []
        self.blocks: list[BitBlock] = []
        self.__init_lines()

    def __init_lines(self):
        for i in range(self.MAX_Y_LINE):
            self.set(0b1 << self.MAX_X_LINE)

    def add_block(self):
        block: FallingBlock = FallingBlock(self.GATE_X, self.GATE_Y)
        block.set(0b11)
        self.falling_blocks.append(block)

    # TODO: 1x1マス以上のbbにも対応
    def render(self, block: FallingBlock):
        x = block.v2d.x + block.bb.x
        y = block.v2d.y

        line = self.get(y)
        b = 0b1 << x

        self.set(line & b, y)

    def clear(self, block: FallingBlock):
        x = block.v2d.x + block.bb.x
        y = block.v2d.y

        line = self.get(y)
        b = 0b1 << x

        self.set(line & ~b, y)

    def is_under_bounds(self, block: FallingBlock) -> bool:
        return self.MAX_Y_LINE < block.v2d.y

    def place(self, block: FallingBlock):
        self.render(block)


    def update(self):
        for block in self.falling_blocks:
            self.clear(block)
            block.falling()
            self.render(block)


