import RPi.GPIO as gpio
from time import sleep
import Adafruit_GPIO.SPI as SPI
import Adafruit_LSM303, math

stage = 0
from operator import add, truediv
buttonPin = 18
alarmPin = 19

delayTime = 0.01

lsm303 = Adafruit_LSM303.LSM303()
#lsm303.mag_rate = Adafruit_LSM303.MAGRATE_220
#lsm303.accel_rate = Adafruit_LSM303.ACCELRATE_220



sample = 0
accelCalibrateSum = [0.0,0.0,0.0]
downVec = [0.0,0.0,0.0]

timer = 0

deltaV = [0.0,0.0,0.0]
posEstimate = [0.0,0.0,0.0]

# gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(alarmPin, gpio.OUT)
gpio.setup(buttonPin, gpio.IN)



while stage == 0:
    stage += gpio.input(buttonPin)
    sleep(delayTime)

while stage == 1:
    stage += gpio.input(buttonPin)
    accel = [n/1000.0 for n in lsm303.read()]
    accelCalibrateSum = list( map(add, accelCalibrateSum, accel) )
    sample += 1
    sleep(delayTime)
downVec = list(map(truediv, accelCalibrateSum, [sample, sample, sample]))
downVec = [n/magnitude(downVec) for n in downVec]

while stage == 2:
    accel = [n/1000.0 for n in lsm303.read()[0]]

    if math.acos(dot(downVec, accel)/(magnitude(vec1)*magnitude(vec2))) > 3.141592653589793238462643383/4.0:
        stage += 1
    sleep(delayTime)

while stage == 3:
    accel = [n/1000.0 for n in lsm303.read()[0]]
    deltaV = map(add, deltaV, [n*delayTime for n in accel], [n*9.8 for n in downVec])
    posEstimate = map(add, posEstimate, [n*delayTime for n in deltaV])
    if dot(deltaV, downVec) < 0.1:
        shriek()
    else:
        unshriek()
    sleep(delayTime)

def dot(vec1, vec2):
    assert (len(vec1)==len(vec2)), "You can't dot vectors of two different dimensions, dummy."
    total = 0
    for i in range(0, len(vec1)):
        total += vec1[i]*vec2[i]
    return total
    
    
def magnitude(vec):
    return math.sqrt(sum([n**2 for n in vec]))

def shriek():
    gpio.output(alarmPin, True)
def unshriek():
    gpio.output(alarmPin, False)
