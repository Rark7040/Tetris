import time

import RPi.GPIO as GPIO

shift_srclk = 2
shift_rclk = 3
shift_ser = 4

sync_srclk = 14
sync_rclk = 15
sync_ser = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(shift_srclk, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(shift_rclk, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(shift_ser, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(sync_srclk, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(sync_rclk, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(sync_ser, GPIO.OUT, initial=GPIO.LOW)


class ShiftRegister:
    MAX = 14

    def __init__(self):
        self.now_input = 0
        self.clear()
        self.input(1)
        self.deploy()
        pass

    def on_update(self):
        self.shift()
        self.deploy()
        time.sleep(0.7)

    def deploy(self):
        GPIO.output(shift_rclk, GPIO.HIGH)
        # time.sleep(0.5)
        GPIO.output(shift_rclk, GPIO.LOW)

    def input(self, sig: int):
        print("input")
        GPIO.output(shift_ser, GPIO.HIGH if sig == 1 else GPIO.LOW)
        self.deploy()

    def shift(self):
        print("shift")
        self.now_input += 1

        if self.now_input >= self.MAX:
            self.now_input = 0
            self.clear()
            self.input(1)

        GPIO.output(shift_srclk, GPIO.HIGH)
        # time.sleep(0.5)
        GPIO.output(shift_srclk, GPIO.LOW)

    # TODO 後程基板設計を変えて簡略化したい
    def clear(self):
        print("clear")
        for _ in range(16):
            self.input(0)
            self.deploy()
            GPIO.output(shift_srclk, GPIO.LOW)
            GPIO.output(shift_srclk, GPIO.HIGH)
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

        self.deploy()

    def deploy(self):
        GPIO.output(sync_rclk, GPIO.HIGH)
        # time.sleep(0.01)
        GPIO.output(sync_rclk, GPIO.LOW)

    def input(self, sig: int):
        # time.sleep(0.5)
        GPIO.output(sync_ser, GPIO.HIGH if sig == 1 else GPIO.LOW)
        self.deploy()

    def shift(self):
        GPIO.output(sync_srclk, GPIO.HIGH)
        # time.sleep(0.01)
        GPIO.output(sync_srclk, GPIO.LOW)

    def clear(self):
        for _ in range(16):
            self.input(0)
            self.deploy()
            GPIO.output(sync_srclk, GPIO.HIGH)
            # time.sleep(0.01)
            GPIO.output(sync_srclk, GPIO.LOW)

        self.deploy()


# 1ビット目は無視される
bits = [
    0b1_0000_0000,
    0b1_0000_0000,
    0b1_0000_0000,
    0b1_0000_0000,
    0b1_0000_0000,
    0b1_0000_0000,
    0b1_0000_0000,

    0b1_0000_0000,
    0b1_0000_0000,
    0b1_0000_0000,
    0b1_0000_0000,
    0b1_0000_0000,
    0b1_0000_0000,
    0b1_0000_0000,
]

shift = ShiftRegister()
sync = TransistorArray()
shift.clear()
print("shift clear")
time.sleep(3.0)
print("sync clear")
shift.clear()

time.sleep(3.0)
i = 0
for _ in range(10000):
    time.sleep(0.1)

    if i >= len(bits):
        i = 0

    print(i)
    sync.output(bits[i])
    shift.on_update()
    i += 1

GPIO.cleanup()