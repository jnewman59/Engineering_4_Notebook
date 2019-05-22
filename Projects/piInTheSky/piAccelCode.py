import RPi.GPIO as gpio
from time import sleep
import Adafruit_GPIO.SPI as SPI
import Adafruit_LSM303, math

stage = 0
from operator import truediv
import time
buttonPin = 18
led1Pin = 19
led2Pin = 5

lastLoopTime = 0.0

blinkTimer = 0.0

delayConst = 0.01
delayTime = delayConst

lsm303 = Adafruit_LSM303.LSM303()
#lsm303.mag_rate = Adafruit_LSM303.MAGRATE_220
#lsm303.accel_rate = Adafruit_LSM303.ACCELRATE_220

arbitraryConstant = 1 #9.79937/10.422706978 #hopefully the ratio between the magnitude of measured and real acceleration

sample = 0
accelCalibrateSum = [0.0,0.0,0.0]
downVec = [0.0,0.0,0.0]
activationTimer = 0
timer = 0

deltaV = [0.0,0.0,0.0]

# gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(led1Pin, gpio.OUT)
gpio.setup(led2Pin, gpio.OUT)
gpio.setup(buttonPin, gpio.IN)
stageDelayTimer = 0

def dot(vec1, vec2):
    assert (len(vec1)==len(vec2)), "You can't dot vectors of two different dimensions"
    total = 0
    for i in range(0, len(vec1)):
        total += vec1[i]*vec2[i]
    return total

def delayCalculate():
    global delayTime, lastLoopTime
    currentTime = time.time()
    delayTime = currentTime - lastLoopTime
    lastLoopTime = currentTime


def blink(stage):
    global blinkTimer
    if stage == 0:
        blinkTimer -= (blinkTimer if blinkTimer > 1.0 else 0.0)
        if blinkTimer > 0.5:
            gpio.output(led2Pin, False)
            gpio.output(led1Pin, True)
        else:
            gpio.output(led2Pin, False)
            gpio.output(led1Pin, False)
    elif stage == 1: 
        blinkTimer -= (blinkTimer if blinkTimer > 1.0 else 0.0)
        if blinkTimer > 0.5:
            gpio.output(led2Pin, True)
            gpio.output(led1Pin, False)
        else:
            gpio.output(led1Pin, False)
            gpio.output(led2Pin, False)
    elif stage == 2:
        blinkTimer -= (blinkTimer if blinkTimer > 2.0 else 0.0)
        if blinkTimer > 0.5 and blinkTimer < 1.0:
            gpio.output(led1Pin, True)
            gpio.output(led2Pin, False)
        if blinkTimer > 1.5:
            gpio.output(led2Pin, True)
            gpio.output(led1Pin, False)
        else:
            gpio.output(led1Pin, False)
            gpio.output(led2Pin, False)
    blinkTimer += delayTime
            


def magnitude(vec):
    return math.sqrt(sum([n**2 for n in vec]))

def shriek():
    gpio.output(led1Pin, True)
    gpio.output(led2Pin, True)
    for i in range(0, 10):
        print("shrieking -__--_--_-__-_-_---_---_-_-----_-_-----_-_-_-_-----_--__-_")

def unshriek():
    gpio.output(led1Pin, False)
    gpio.output(led2Pin, False)

def opAdd(*x):
    #print("opadd: args are {}".format(x))
    total = 0
    for i in x:
        #print("opadd: i is {}".format(i))
        total += i
    return total

lastLoopTime = time.time()
while stage == 0:
    delayCalculate()
    stage += not gpio.input(buttonPin)
    blink(stage)
    print("stage 0")
    sleep(delayConst)

while stage == 1:
    delayCalculate()
    if not gpio.input(buttonPin) and stageDelayTimer > 3.0/delayTime:
        stage += 1
        stageDelayTimer = 0
    blink(stage)
    accel = [n*arbitraryConstant/100.0 for n in lsm303.read()[0]]
    accelCalibrateSum = list( map(opAdd, accelCalibrateSum, accel) )
    sample += 1
    print("stage 1, accel = {}".format(accel))
    stageDelayTimer += 1.0
    sleep(delayConst)

blinkTimer = 0.0
downVec = [-n/magnitude(accelCalibrateSum) for n in accelCalibrateSum]

while stage == 2:
    delayCalculate()
    accel = [n*arbitraryConstant/100.0 for n in lsm303.read()[0]]
    blink(stage)
    if math.acos(dot(downVec,[-n for n in accel])/(magnitude(downVec)*magnitude(accel))) > 3.141592653589793238462643383/4.0 or (not gpio.input(buttonPin) and stageDelayTimer >0.5/delayTime):
        stage += 1
    print("stage 2, accel = {}".format(accel))
    stageDelayTimer += 1.0
    sleep(delayConst)

blinkTimer = 0.0
deltaV = [0.0,0.0,0.0]

while stage == 3:
    delayCalculate()
    accel = [n*arbitraryConstant/100.0 for n in lsm303.read()[0]]
    deltaV = list(map(opAdd, deltaV, [n*delayTime for n in accel], [n*9.8*delayTime for n in downVec]))
    if activationTimer>3/delayTime and abs(dot(deltaV, downVec)) < 1:
        shriek()
    else:
        unshriek()
    activationTimer += 1
    print("stage 3, accel = {}, deltaV = {}, activated = {}".format(accel, deltaV, activationTimer>0.5/delayTime))
    sleep(delayConst)
