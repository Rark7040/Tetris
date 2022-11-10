from abc import ABCMeta
import RPi.GPIO as GPIO


class U74HC595AG(metaclass=ABCMeta):
    MAX_BUS_PORT: int = 0

    def __init__(self, ser: int, sck: int, rck: int):
        self.ser: int = ser
        self.sck: int = sck
        self.rck: int = rck

    def __shift(self):  # SCK
        GPIO.output(self.sck, GPIO.HIGH)
        GPIO.output(self.sck, GPIO.LOW)

    def __serial_input(self, sig: bool):  # SER
        GPIO.output(self.ser, GPIO.HIGH if sig else GPIO.LOW)

    def __latch(self):  # RCK
        GPIO.output(self.rck, GPIO.HIGH)
        GPIO.output(self.rck, GPIO.LOW)

    # TODO 後程基板設計を変えて簡略化したい
    def clear(self):
        for _ in range(self.MAX_BUS_PORT):
            self.__serial_input(False)
            self.__shift()

        self.__latch()
