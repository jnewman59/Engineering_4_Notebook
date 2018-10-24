from picamera import PiCamera
from time import sleep
from gpiozero import Button

camera = PiCamera()


button = Button(17)

frame = 0

while True:
    try:
        camera.start_preview()
        button.wait_for_press()
        frame += 1
        camera.capture('../Pictures/frame%03d.png' % frame)
        sleep(2)
    except KeyboardInterrupt:
        camera.stop_preview()
        break
