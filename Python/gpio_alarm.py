"""
Ben and Jonah
GPIO alarm
"""

import RPi.GPIO as gpio
from time import sleep
import random

gpio.setwarnings(False)

alarmPin = 11
switchPin = 37

gpio.setmode(gpio.BOARD)
gpio.setup(alarmPin, gpio.OUT)
gpio.setup(switchPin, gpio.IN)

while True:
        if gpio.input(switchPin):
                sleep(random.uniform(0.05, 0.1))
                gpio.output(alarmPin, True)
                print("on")
                sleep(random.uniform(0.025, 0.05))
                gpio.output(alarmPin, False)
                print("off")

gpio.cleanup()
