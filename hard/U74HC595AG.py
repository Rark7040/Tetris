from abc import abstractmethod, ABCMeta


class U74HC595AG(metaclass=ABCMeta):
    @abstractmethod
    def shift(self):  # SCK
        pass

    @abstractmethod
    def serial_input(self, sig: bool):  # SER
        pass

    @abstractmethod
    def latch(self):  # RCK
        pass
