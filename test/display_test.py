import time

import RPi.GPIO as GPIO

shift_srclk = 0
shift_rclk = 0
shift_ser = 0

sync_srclk = 0
sync_rclk = 0
sync_ser = 0

GPIO.setmode(GPIO.BCM)

GPIO.setup(shift_srclk, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(shift_rclk, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(shift_ser, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(sync_srclk, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(sync_rclk, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(sync_ser, GPIO.OUT, initial=GPIO.LOW)


class ShiftRegister:
    MAX = 14
    now_input = 0

    def __init__(self):
        self.input(1)
        self.deploy()

    def on_update(self):
        self.shift()
        self.deploy()

        print(self.now_input)

    def deploy(self):
        GPIO.output(shift_rclk, GPIO.HIGH)
        # time.sleep(0.01)
        GPIO.output(shift_srclk, GPIO.LOW)

    def input(self, sig: int):
        GPIO.output(shift_ser, GPIO.HIGH if sig == 1 else GPIO.LOW)

    def shift(self):
        self.now_input += 1

        if self.now_input > self.MAX:
            self.now_input = 0
            self.clear()
            self.input(1)

        GPIO.output(shift_srclk, GPIO.HIGH)
        # time.sleep(0.01)
        GPIO.output(shift_srclk, GPIO.LOW)

    def clear(self):
        for _ in range(16):
            self.input(0)
            GPIO.output(shift_srclk, GPIO.HIGH)
            # time.sleep(0.01)
            GPIO.output(shift_srclk, GPIO.LOW)

        self.deploy()


class TransistorArray:

    def output(self, b: int):
        self.clear()

        while b != 0b1:
            dump = b & 0b1
            self.input(dump)
            self.shift()
            b = b >> 1

            print(bin(b))

        self.deploy()

    def deploy(self):
        GPIO.output(sync_rclk, GPIO.HIGH)
        # time.sleep(0.01)
        GPIO.output(sync_rclk, GPIO.LOW)

    def input(self, sig: int):
        GPIO.output(sync_ser, GPIO.HIGH if sig == 1 else GPIO.LOW)

    def shift(self):
        GPIO.output(sync_srclk, GPIO.HIGH)
        # time.sleep(0.01)
        GPIO.output(sync_srclk, GPIO.LOW)

    def clear(self):
        for _ in range(16):
            self.input(0)
            GPIO.output(sync_srclk, GPIO.HIGH)
            # time.sleep(0.01)
            GPIO.output(sync_srclk, GPIO.LOW)

        self.deploy()


# 1ビット目は無視される
bits = 0b111001100

shift = ShiftRegister()
sync = TransistorArray()

for _ in range(10000):
    time.sleep(0.005)
    shift.on_update()
    sync.output(bits)

GPIO.cleanup()