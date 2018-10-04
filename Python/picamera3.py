from picamera import PiCamera, Color
import time

camera = PiCamera()

camera.resolution = (500, 500)

camera.start_preview()
camera.start_recording('/home/pi/Documents/Engineering_4_Notebook/Python/video.h264')
time.sleep(10)
camera.stop_recording()
camera.stop_preview()
