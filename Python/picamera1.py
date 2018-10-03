from picamera import PiCamera
import time

myCamera = PiCamera()

myCamera.start_preview()
time.sleep(5)
myCamera.stop_preview()
