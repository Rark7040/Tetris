import copy

from soft import Vector2d
from soft.BitBlock import BitBlock


class FallingBlock(BitBlock):
    MAX_LIFE_TIME = 20

    def __init__(self, v2d: Vector2d):
        super().__init__()
        self.lifetime = self.MAX_LIFE_TIME
        self.v2d: Vector2d = v2d

    def reset_life(self):
        self.lifetime: int = self.MAX_LIFE_TIME

    def falling(self):
        self.v2d.y -= 1
        self.on_move()

    def on_colliding(self):
        self.lifetime -= 1

    def on_move(self):
        self.reset_life()
        # and more ...?

    def is_controllable(self) -> bool:
        return 0 < self.lifetime

    def get_cloning_vector(self) -> Vector2d:
        return copy.deepcopy(self.v2d)