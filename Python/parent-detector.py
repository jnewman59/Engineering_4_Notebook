import time
from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime

pir = MotionSensor(4)
camera = PiCamera()

filename = "parentDetector.h264"

while True:
    pir.wait_for_motion()
    print("MOTINO IAOINSIN IN")
    print("PRONTING " + filename)
    camera.start_recording(filename)
    time.sleep(5)
    
    pir.wait_for_no_motion()
    print("NO MO ROMEON EMO MNOQN MOATIANO")
    camera.stop_recording()
    time.sleep(0.5)
