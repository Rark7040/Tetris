from enum import Enum


class Test(Enum):
    RED = 0
    BLUE = 1
    YELLOW = 2


print(repr(Test.BLUE))