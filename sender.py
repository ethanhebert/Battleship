GPIO.output(senders[1], 0)
    GPIO.output(senders[2], 0)
    for x in range(10, 18):
        for y in range(1, 9):
            
            myLocation = str(x) + str(y)
            theirLocation = str(x-9) + str(y)
            while True:
                if ((GPIO.input(receivers[1]) == False) and (GPIO.input(receivers[2]) == False)):
                    break
            
            if (shipPresence[myLocation] == 0): #you have no ship
                GPIO.output(senders[1], 1)
                GPIO.output(senders[2], 0)
            elif (shipPresence[myLocation] == 1): #you have ship
                GPIO.output(senders[1], 0)
                GPIO.output(senders[2], 1)


            while True:
                if (GPIO.input(receivers[1]) == True): #they have no ship
                    p2shipPresence[theirLocation] = 0
                    GPIO.output(senders[1], 0)
                    GPIO.output(senders[2], 0)
                    break

                elif (GPIO.input(receivers[2]) == True): #they have ship
                    p2shipPresence[theirLocation] = 1
                    GPIO.output(senders[1], 0)
                    GPIO.output(senders[2], 0)
                    break
