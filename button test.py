import RPi.GPIO as GPIO
from time import sleep

#blue = 25
buttons = [25]

GPIO.setmode(GPIO.BCM)
GPIO.setup(buttons, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while True:
    if (GPIO.input(buttons[0]) == True):
        print(1)
        
    else:
        print(0)
