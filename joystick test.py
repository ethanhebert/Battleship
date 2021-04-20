import RPi.GPIO as GPIO
from time import sleep
"""
joystick = [18, 19, 20, 21]

GPIO.setmode(GPIO.BCM)
GPIO.setup(joystick, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while True:
    for i in range(len(joystick)):
        if (GPIO.input(joystick[i]) == 0):
            print(i)


"""
squareStatus = {}


for i in range(0,8):
    for j in range(0,8):
        location = str(10+j) + str(i+1)
        squareStatus[location] = "blue"
        location = str(i+1) + str(j+1)
        squareStatus[location] = "blue"
        print(location)

print(squareStatus)


            
