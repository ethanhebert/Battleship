
import RPi.GPIO as GPIO
from time import sleep

senders = [17, 16, 13]
receivers = [6, 5, 4]

GPIO.setmode(GPIO.BCM)
GPIO.setup(senders, GPIO.OUT)
GPIO.setup(receivers, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

p2shipPresence = {}
for x in range(10, 18):
    for y in range(1, 9):
        location = str(x) + str(y)
        p2shipPresence[location] = 0
print(p2shipPresence)

"""
while True:
    if (GPIO.input(receivers[0]) == True):
        print("Got it!")
"""
print("Waiting...")

for x in range(10, 18):
    for y in range(1, 9):
        location = str(x) + str(y)
        GPIO.output(senders[0], 0)
        
        while True:
            if (GPIO.input(receivers[0]) == True): #no ship
                p2shipPresence[location] = 0
                break
            elif (GPIO.input(receivers[1]) == True): #ship
                p2shipPresence[location] = 1
                break
            
        GPIO.output(senders[0], 1)

print(p2shipPresence)

        





