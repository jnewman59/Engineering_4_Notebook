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
#image = Image.new('1', (width, height))
"""
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

draw.text((0,0), 'Accel Data:', font=font, fill=255)
"""

while True:
    disp.clear()
    
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    
    draw.text((0,0), 'Accel Data:', font=font, fill=255)
    
    accel, mag = lsm303.read()
    
    x_data, y_data, z_data = accel
    
    x_data = str(round((x_data / 100), 3))
    y_data = str(round((y_data / 100), 3))
    z_data = str(round((z_data / 100), 3))

    draw.text((0, 15), 'X: ' + x_data, font=font, fill=255)
    draw.text((0, 30), 'Y: ' + y_data, font=font, fill=255)
    draw.text((0, 45), 'Z: ' + z_data, font=font, fill=255)

    disp.image(image)
    disp.display()
    
    time.sleep(0.5)
