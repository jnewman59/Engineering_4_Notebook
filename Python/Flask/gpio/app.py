#Ben Lepsch and Jonah Newman

from flask import Flask, render_template, request
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

app = Flask(__name__)

led1 = False
led2 = False

@app.route("/", methods=["GET","POST"])
def index():
        led1 = GPIO.input(17)
        led2 = GPIO.input(18)
	if request.method == "POST":
                msg = request.form.get("onBtn")
                if msg == "LED1":
                        led1 = not led1
                        GPIO.output(17,led1)
                        print("led 1 turned "+ "on" if led1 else "off")
                elif msg == "LED2":
                        led2 = not led2
                        GPIO.output(18,led2)
                        print("led 2 turned "+ "on" if led2 else "off")
	else:
		GPIO.output(17,GPIO.LOW)
		msg = "No click yet."
	button1 = "Turjn LED 1 " + ("off" if led1 else "on")
	button2 = "Tjurn LED 2 " + ("off" if led2 else "on")
	return render_template("index.html", msg=msg, button1=button1, button2=button2)

if __name__ == "__main__":
        #global led1, led2
        #led1 = False
        #led2 = False
	app.run(host="0.0.0.0",port=80,debug=True)



