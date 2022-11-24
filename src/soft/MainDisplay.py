from src.soft.BitBlock import BitBlock
from src.soft.FallingBlock import FallingBlock


class MainDisplay(BitBlock):
    MAX_X_LINE: int = 8
    MAX_Y_LINE: int = 13  # idx is start from 0
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

    # TODO: 1x1マス以上のbbにも対応
    def add_block(self):
        block: FallingBlock = FallingBlock(self.GATE_X, self.GATE_Y)
        block.set(0b11)
        self.falling_blocks.append(block)

    def get_falling_blocks(self) -> list[FallingBlock]:
        return self.falling_blocks

    # TODO: 1x1マス以上のbbにも対応
    def render(self, block: FallingBlock):
        x = block.v2d.x + block.bb.x
        y = block.v2d.y

        line = self.get(y)
        b = 0b1 << x

        self.set(line & b, y)

    # TODO: 1x1マス以上のbbにも対応
    def clear(self, block: FallingBlock):
        x = block.v2d.x + block.bb.x
        y = block.v2d.y

        line = self.get(y)
        b = 0b1 << x

        self.set(line & ~b, y)

    # TODO: 1x1マス以上のbbにも対応
    def can_falling(self, block: FallingBlock) -> bool:
        x = block.v2d.x
        y = block.v2d.y + 1  # check under block

        line = self.get(y)
        b = 0b1 << x
        return block.v2d.y < self.MAX_Y_LINE or line & b != b

    def place(self, block: FallingBlock):
        self.render(block)
        self.blocks.append(block)
        self.falling_blocks.remove(block)

    def can_add_block(self) -> bool:
        return len(self.falling_blocks) == 0

    def update(self):
        self.calc_falling_blocks()

        if self.can_add_block():
            self.add_block()

    def calc_falling_blocks(self):
        for idx, block in self.falling_blocks:
            self.clear(block)

            if self.can_falling(block):
                block.falling()
                self.render(block)

            else:
                block.on_colliding()
                self.render(block)
