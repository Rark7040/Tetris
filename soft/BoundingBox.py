from soft import Vector2D


class BoundingBox:
    def __init__(self, start: Vector2D, size: Vector2D):
        super().__init__()
        self.start: Vector2D = start
        self.end: Vector2D = start.add(size)

    def is_inside(self, v2d: Vector2D) -> bool:
        return self.start.x < v2d.x < self.end.x and self.start.y < v2d.y < self.end.y

    # TODO: 1x1マス以上のbbにも対応
    # not inside
    def is_colliding(self, v2d: Vector2D) -> bool:
        if self.is_inside(v2d):
            return False
        return self.start.x - 1 < v2d.x < self.end.x + 1 and self.start.y - 1 < v2d.y < self.end.y + 1
