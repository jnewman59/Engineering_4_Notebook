'''

every 1/10 second move forwards one pixel and set vertical coordinate to the measurement
once it reaches the maximum X ir clears the graph and starts over from the Y axis
graph X as 10 - 0 - -10 all above the normal x axis which will be -11 or something

'''


import time, Adafruit_LSM303, Adafruit_SSD1306
import Adafruit_GPIO.SPI as SPI
from PIL import Image, ImageDraw, ImageFont

RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

lsm303 = Adafruit_LSM303.LSM303()
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height

yAxisCoordinates = (15, 0, 15, 50)
xAxisCoordinates = (15, 25, 128, 25)


axisImage = Image.new('1', (width, height))
axisDraw = ImageDraw.Draw(axisImage)

rotateImage = Image.new('1', (width, 17))
rotateDraw = ImageDraw.Draw(rotateImage)

font = ImageFont.load_default()
rotateDraw.text((0,0), "a(m/s^2)", font = font, fill = 255)
rotatedImage = rotateImage.rotate(90, expand=1)

axisImage.paste(rotatedImage,(0,-80))

dataArr = []

while True:
    dataImage = Image.new('1', (width, height))
    dataDraw = ImageDraw.Draw(dataImage)
    accel = lsm303.read()[1][1]
    disp.clear()
    dataArr.append(accel*25/800)
    if len(dataArr)>28:
        dataArr.remove(dataArr[0])
    for i in range(len(dataArr)-1):
        dataDraw.line((4*i+16,dataArr[i]+25,4*i+20,dataArr[i+1]+25),fill=255) 
    #space from Y axis to end of screen: 112px
    #space from X axis to top of screen: 48px

    dataImage.paste(rotatedImage, (0, -80))
    axisImage.paste(dataImage, (0 ,0))
    axisDraw.line(yAxisCoordinates, fill = 255)
    axisDraw.line(xAxisCoordinates, fill = 255)
    axisDraw.text((50, 49), 'Time (s)', font=font, fill=255)

    disp.image(axisImage)
    disp.display()

    time.sleep(0.1)
