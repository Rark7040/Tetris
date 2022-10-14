from abc import abstractmethod, ABCMeta


class U74HC595AG(metaclass=ABCMeta):
    def __init__(self, ser: int, sck: int, rck: int):
        self.ser = ser
        self.sck = sck
        self.rck = rck

    @abstractmethod
    def shift(self):  # SCK
        pass

    @abstractmethod
    def serial_input(self, sig: bool):  # SER
        pass

    @abstractmethod
    def latch(self):  # RCK
        pass
