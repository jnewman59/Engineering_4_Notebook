from picamera import PiCamera, Color
import time

camera = PiCamera()

camera.resolution = (1920, 1080)

camera.start_preview()
for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.annotate_background = Color('blue')
    camera.annotate_foreground = Color('yellow')
    camera.annotate_text = "Effect: %s" % effect
    time.sleep(5)
camera.stop_preview()
