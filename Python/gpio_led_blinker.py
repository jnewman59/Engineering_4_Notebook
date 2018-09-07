"""

Ben Lepsch and Jonah Newman
GPIO LED Blinker

"""


import RPi.GPIO as gpio
from time import sleep

red_pin = 18
blue_pin = 16 # LED Pins

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(red_pin, gpio.OUT)
gpio.setup(blue_pin, gpio.OUT)  # pinMode() but python

running = True

while running:
    blink = input("Enter the number of times for the LEDs to blink or exit to exit.\t")
    if not blink == "exit":
        delay = float(input("How long should it delay in between each blink (in seconds)?\t"))
        blink = int(blink)
        for i in range(blink):
            gpio.output(red_pin, True)
            gpio.output(blue_pin, False)
            sleep(delay)
            gpio.output(red_pin, False)
            gpio.output(blue_pin, True)
            sleep(delay)
        gpio.output(blue_pin, False)
    else:
        running = False

gpio.cleanup()
