while True:
            if (myTurn == 1):
                break
            
            #receive data set to see where other player fired###########################
            for x in range(10, 18):
                for y in range(1, 9):
                    location = str(x) + str(y)
                    GPIO.output(senders[1], 0)
                    
                    while True:
                        if (GPIO.input(receivers[1]) == True): #they haven't shot there
                            p2shotsTaken[location] = 0
                            break
                        elif (GPIO.input(receivers[2]) == True): #they have shot there
                            p2shotsTaken[location] = 1
                            break

                    GPIO.output(senders[1], 1)

            #wait for p1 to move on from data transfer
            while True:
                if (GPIO.input(receivers[1]) == True):
                    break

            print()
            print("Their shots")
            print(p2shotsTaken)
            
            myTurn = 1
