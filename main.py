import RPi.GPIO as GPIO

from hard.RPiConfig import RPiConfig


def main():
    init()


def init():
    GPIO.setmode(GPIO.BCM)

    for pin in RPiConfig:
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)


if __name__ == '__main__':
    main()
