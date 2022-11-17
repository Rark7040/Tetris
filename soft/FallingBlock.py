from soft.BitBlock import BitBlock


class FallingBlock(BitBlock):

    def __init__(self):
        super().__init__()
        self.__x: int = 0
        self.__y: int = 0

