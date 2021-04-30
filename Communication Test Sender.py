
import RPi.GPIO as GPIO
from time import sleep

shipPresence = {

 '101': 0, '102': 0, '103': 0, '104': 0, '105': 0, '106': 0, '107': 0, '108': 0, \
 '111': 0, '112': 0, '113': 0, '114': 0, '115': 0, '116': 0, '117': 0, '118': 0, \
 '121': 1, '122': 1, '123': 1, '124': 1, '125': 0, '126': 0, '127': 0, '128': 0, \
 '131': 1, '132': 1, '133': 1, '134': 1, '135': 0, '136': 0, '137': 0, '138': 0, \
 '141': 1, '142': 1, '143': 1, '144': 1, '145': 0, '146': 0, '147': 0, '148': 0, \
 '151': 0, '152': 0, '153': 0, '154': 0, '155': 0, '156': 0, '157': 0, '158': 0, \
 '161': 0, '162': 0, '163': 0, '164': 0, '165': 0, '166': 1, '167': 1, '168': 1, \
 '171': 0, '172': 0, '173': 0, '174': 0, '175': 0, '176': 0, '177': 0, '178': 0

}

joystick = [18, 19, 20, 21]
buttons = [25, 26, 27]
senders = [17, 16, 13]
receivers = [6, 5, 4]

GPIO.setmode(GPIO.BCM)
GPIO.setup(joystick, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(buttons, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(senders, GPIO.OUT)
GPIO.setup(receivers, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

"""
#if red button pressed, send signal
while True:
    pressed = False
    GPIO.output(senders[0], 0)
    if (buttons[1] == False):
        while (not pressed):
            print("In the loop")
            if (GPIO.input(buttons[1]) == True):
                GPIO.output(senders[0], 1)
                pressed = True

            else:
                GPIO.output(senders[0], 0)
"""
#start with both senders off
GPIO.output(senders[0], 0)
GPIO.output(senders[1], 0)

print("About to start...")


#start the loop when red button is pressed
pressed = False
while (pressed == False):
    if (GPIO.input(buttons[1]) == True):
        pressed = True

print("RED")

for x in range(10, 18):
    for y in range(1, 9):
        
        location = str(x) + str(y)
        while True:
            if (GPIO.input(receivers[0]) == False):
                break
        
        if (shipPresence[location] == 0): #no ship
            GPIO.output(senders[0], 1)
            GPIO.output(senders[1], 0)
        elif (shipPresence[location] == 1): #ship
            GPIO.output(senders[0], 0)
            GPIO.output(senders[1], 1)


        while True:
            if (GPIO.input(receivers[0]) == True):
                GPIO.output(senders[0], 0)
                GPIO.output(senders[1], 0)
                break

print(shipPresence)
                
        




