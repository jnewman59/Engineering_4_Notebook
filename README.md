Engineering 4 Notebook
Jonah Newman and Ben Lepsch

# Assignments

## Raspberry Pi Zero Intro

### Lessons Learned

Set up Raspberry Pi Zero, connected it to monitor, booted it, and wrote a simple bash script to print "Hello World" 10 times using a loop. We learned how to output text to the shell, run a script, and use a for loop in a bash script.

### Code

[helloWorld.sh](/Scripts/helloWorld.sh)

## Mathematica Intro

### Lessons Learned

Started Wolfram Mathematica on Raspi 0 to practice basic commands. We learned how to evaluate expressions, define and operate on lists, plot lists, derive and integrate functions, and create a dynamic plot of a function with constants controlled by user input through sliders. 

### Code

[firstproject.nb](/Mathematica/firstproject.nb)

## Python Intro

### Lessons Learned

Wrote a Python script (using IDLE) to print "Hello World" 10 times by looping. Then made a dice roller program that uses the built-in random library to generate a random integer between 1 and 6 inclusive repeatedly at the user's request, then end the program when prompted.

### Code

[helloWorld.py](/Python/helloWorld.py)

[automatic_dice.py](/Python/automatic_dice.py)

## Python - Calculator

### Lessons Learned

Wrote a Python script that when given two real numbers a and b outputs a+b, a-b, a\*b, a/b, a%b, and a^b. Learned how to iterate over dictionary keys and use lambda notation.

### Code

[calculator.py](/Python/calculator.py)

## Python - Quadratic Solver

### Lessons Learned

Wrote a Python script that when given the coefficients of a quadratic equation finds all real solutions. Learned how to use conditional expressions, and that it's not always the right choice to use conditional expressions.

### Code

[quadraticSolver.py](/Python/quadraticSolver.py)

## Git Intro

### Lessons Learned

Created git repository for our engineering notebook, made a github account, and linked our repo to one on github. Learned how to initialize a git repository, link it to a remote (hosted on Github), make commits, and push to the remote. 

## Git - Forks and Clones

### Lessons Learned

Forked a repository owned by the chssigma github account, cloned it to our computer, edited the users file in the appropriate directory, committed, pushed, and submitted a pull request to merge our edits back into the original repo. Learned how to fork and clone a git repository, as well as how to make and comment on a pull request.

## Git - Engineering Notebook

### Lessons Learned

Started the actual Engineering 4 notebook in our notebook repo by writing it in the README using Markdown. Learned how to use vim more effectively and how to format in Markdown.

## Python - Strings and Loops

### Lessons Learned

Wrote a Python program to split a string across a delimiting character (in this case " "), then print it out letter by letter.

### Code

[stringSplitter.py](/Python/stringSplitter.py)

## Python - Hangman

### Lessons Learned

Wrote a Python program to play hangman with the user after a word has been inputted. Learned how to execute terminal commands from within a python script.

### Code

[hangman.py](/Python/hangman.py)

## Bash - GPIO Pins

### Lessons Learned

Wrote a bash script that uses GPIO pins on the Pi to make an external LED blink (after soldering a male-male header to those pins). Learned how to use GPIO output from a Pi Zero.

### Code 

[ledBlink.sh](/Scripts/ledBlink.sh)

## Python - GPIO Pins

### Lessons Learned

We wrote the same script as in the last assignment but using Python instead of bash, meaning we can now integrate GPIO pins/external sensors or displays into projects coded in Python.

### Code

[gpio_led_blinker.py](/Python/gpio_led_blinker.py)

## SSH - GPIO Pins

### Lessons Learned

We learned how to ssh into a pi from a chromebook. This is cool because it lets us edit stuff on the pi without needing to be next to it, but we didn't really use it because the pi's IP usually changes when it restarts.


## Hello Flask

### Lessons Learned

We learned how to write an extremely basic Flask app that would be visible on a local network.

### Code

[app.py](/Python/Flask/hello_world/app.py)

## GPIO with Flask

### Lessons Learned

We learned how to write a more advanced Flask app that uses an HTML template and a form to send data back to the server. Basically, there are two buttons on the website that turn on or off two LEDs hooked up to the pi. 

### Code

[app.py](/Python/Flask/gpio/app.py)
[index.html](/Python/Flask/gpio/templates/index.html)

## GPIO I2C



### Lessons Learned

This assignment taught us how to use an i2c accelerometer and display at the same time while only taking up 2 pins on the pi. THe accelerometer also came in handy in our later Pi in the Sky project.

### Code 

[gpio_i2c.py](/Python/gpio_i2c.py)

## Headless



### Lessons Learned

This assignment was just the last assignment but the display graphed the output from one accelerometer axis and we couldn't run the program from the pi, it had to run at startup or we had to ssh in and run it there. We chose to run it at startup instead of ssh because of the variable IP address of the pi, and this came in handy during the Pi in the Sky project where we had to run the code on startup.

### Code 

[headless.py](/Python/headless.py)

## Pi Camera



### Lessons Learned

This was three smaller assignments - (1) make a program that opens a window of what the camera sees then closes it after 5 seconds, (2) a program that opens a window of what the camera sees and loops through all of the possible effects, then saves a picture for five of the effects, and (3) opens a window for 10 seconds and saves it as a video.

### Code 

[picamera1.py](/Python/picamera1.py)
[picamera2.py](/Python/picamera2.py)
[picamera3.py](/Python/picamera3.py)

## Hack your Stuff



### Lessons Learned

This assignment was to figure out how to turn on and off an alarm using the pi. It wasn't really new stuff, just using what we learned in the GPIO assignment and previous knowledge of how to wire a circuit. We didn't even write code for this, we just wired the switch to the pi's 5 volt output pin.

## Copypasta 1

### Lessons Learned

This assignment taught us how to use a motion detector and have motion trigger the camera to start recording.

### Code

[motion_camera.py](/Python/motion_camera.py)

## Copypasta 2

### Lessons Learned

This assignment taught us how to take a picture with the pi camera when a button was pressed, so combining the GPIO-Python assignment with the camera assignment.

### Code

[pbsm.py](/Python/pbsm.py)

# Projects

## [Pi in the Sky](https://github.com/blepsch57/piinthesky)
