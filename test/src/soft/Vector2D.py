from __future__ import annotations


class Vector2D:
    def __init__(self, x: int, y: int):
        super().__init__()
        self.x: int = x
        self.y: int = y

    def add(self, v2d: Vector2D) -> Vector2D:
        new: Vector2D = Vector2D(self.x, self.y)
        new.x += v2d.x
        new.y += v2d.y
        return new
