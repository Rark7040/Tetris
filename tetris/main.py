import RPi.GPIO as GPIO

from test.tetris.hard.RPiConfig import RPiConfig


def main():
    init()


def init():
    GPIO.setmode(GPIO.BCM)

    for pin in RPiConfig:
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)




def final():
    GPIO.cleanup()


if __name__ == '__main__':
    main()
