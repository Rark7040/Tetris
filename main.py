import RPi.GPIO as GPIO

from hard.RPiConf import RPiConf


def main():
    init()
    print("noop")


def init():
    conf = RPiConf()
    GPIO.setmode(GPIO.BCM)

    for pin in conf.get_all_pin():
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)


if __name__ == '__main__':
    main()
