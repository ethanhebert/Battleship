if (GPIO.input(buttons[1]) == True):
                    location = str(currentx) + str(currenty)
                    
                    if (shotsTaken[location] == 1): #can't shoot same place twice
                        sounds[5].play()
                    else:
                        b1.fire(currentx, currenty)

                        #send data set of where you fired to other player
                        for x in range(1, 9):
                            for y in range(1, 9):
                                
                                location = str(x) + str(y)
                                while True:
                                    if (GPIO.input(receivers[1]) == False):
                                        break
                                
                                if (shotsTaken[location] == 0): #you haven't shot there
                                    GPIO.output(senders[1], 1)
                                    GPIO.output(senders[2], 0)
                                elif (shotsTaken[location] == 1): #you've shot there
                                    GPIO.output(senders[1], 0)
                                    GPIO.output(senders[2], 1)

                                while True:
                                    if (GPIO.input(receivers[1]) == True):
                                        GPIO.output(senders[1], 0)
                                        GPIO.output(senders[2], 0)
                                        break

                        #move on from the data transfer
                        GPIO.output(senders[1], 1)
                        sleep(0.05)
                        GPIO.output(senders[1], 0)
                        

                        print()
                        print("My shots:")
                        print(shotsTaken)
                        
                        pressed = True
                        myTurn = 0
