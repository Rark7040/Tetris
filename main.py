import RPi.GPIO as GPIO

from hard.RPiConf import RPiConf


def main():
    init()


def init():
    GPIO.setmode(GPIO.BCM)

    for pin in RPiConf:
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)


if __name__ == '__main__':
    main()
