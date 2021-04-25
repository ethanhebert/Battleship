#here we go

#NOTE - Alt + Esc to exit program

import pygame
from tkinter import *
import RPi.GPIO as GPIO
from time import sleep
from random import randint

class Game(Frame):
    #class variables
    
    def __init__(self, container):
        Frame.__init__(self, container, bg="white")
        container.attributes("-fullscreen", True)

    def setupGUI(self):

        #setup display
        
        #top gap
        self.top = Label(self, height=2, width=100, background="white")
        self.top.grid(row=0, column=0, columnspan=19)
        
        #left gap
        self.left = Label(self, height=1, width=2, background="white")
        self.left.grid(row=1, column=0, rowspan=10)
        
        #left grid
        global img
        for i in range(0,8):
            for j in range(0,8):
                #j is x, i is y

                
                location = str(j+1) + str(i+1)
                squareStatus[location] = "blue"
                img = PhotoImage(file="gamefiles/blue.gif")
                self.label = Label(self, image=img, background="black")
                self.label.image = img
                self.label.grid(row=1+i, column=j+1, sticky = NSEW)
                
                
                #TEST - makes a random board layout for testing functionality
                """
                crazy = randint(1,3)
                if (crazy == 1):
                    location = str(j+1) + str(i+1)
                    squareStatus[location] = "blue"
                    img = PhotoImage(file="gamefiles/blue.gif")
                    self.label = Label(self, image=img, background="black")
                    self.label.image = img
                    self.label.grid(row=1+i, column=j+1, sticky = NSEW)

                elif (crazy == 2):
                    location = str(j+1) + str(i+1)
                    squareStatus[location] = "bluehit"
                    img = PhotoImage(file="gamefiles/bluehit.gif")
                    self.label = Label(self, image=img, background="black")
                    self.label.image = img
                    self.label.grid(row=1+i, column=j+1, sticky = NSEW)

                elif (crazy == 3):
                    location = str(j+1) + str(i+1)
                    squareStatus[location] = "bluemiss"
                    img = PhotoImage(file="gamefiles/bluemiss.gif")
                    self.label = Label(self, image=img, background="black")
                    self.label.image = img
                    self.label.grid(row=1+i, column=j+1, sticky = NSEW)
                """
                

        #middle gap
        self.mid = Label(self, height=1, width=1, background="white")
        self.mid.grid(row=0, column=9, rowspan=10)

        #right grid
        for i in range(0,8):
            for j in range(0,8):
                #j is x, i is y
                location = str(10+j) + str(i+1)
                squareStatus[location] = "blue"
                img = PhotoImage(file="gamefiles/blue.gif")
                self.label = Label(self, image=img, background="black")
                self.label.image = img
                self.label.grid(row=1+i, column=10+j, sticky = NSEW)

        #right gap
        self.right = Label(self, height=1, width=2, background="white")
        self.right.grid(row=1, column=18, rowspan=10)

        #bottom gap
        self.bottom = Label(self,  width=100, background="white")
        self.bottom.grid(row=9, column=0, columnspan=19)

        #display it all once done
        self.pack(fill=BOTH, expand=1)


    #make a square blue
    def blue(self, x, y):
        location = str(x) + str(y)
        
        #if previous square is regular
        if (squareStatus[location] == "blue" or squareStatus[location] == "green"):
            squareStatus[location] = "blue"
            img = PhotoImage(file="gamefiles/blue.gif")
            self.label = Label(self, image=img, background="black")
            self.label.image = img
            self.label.grid(row=y, column=x, sticky = NSEW)

        #if previous square is hit
        elif (squareStatus[location] == "bluehit" or squareStatus[location] == "greenhit"):
            squareStatus[location] = "bluehit"
            img = PhotoImage(file="gamefiles/bluehit.gif")
            self.label = Label(self, image=img, background="black")
            self.label.image = img
            self.label.grid(row=y, column=x, sticky = NSEW)

        #if previous square is miss
        elif (squareStatus[location] == "bluemiss" or squareStatus[location] == "greenmiss"):
            squareStatus[location] = "bluemiss"
            img = PhotoImage(file="gamefiles/bluemiss.gif")
            self.label = Label(self, image=img, background="black")
            self.label.image = img
            self.label.grid(row=y, column=x, sticky = NSEW)

        #for placing ships
        elif (squareStatus[location] == "greenhor"):
            squareStatus[location] = "grayhor"
            img = PhotoImage(file="gamefiles/grayhor.gif")
            self.label = Label(self, image=img, background="black")
            self.label.image = img
            self.label.grid(row=y, column=x, sticky = NSEW)

        elif (squareStatus[location] == "greenvert"):
            squareStatus[location] = "grayvert"
            img = PhotoImage(file="gamefiles/grayvert.gif")
            self.label = Label(self, image=img, background="black")
            self.label.image = img
            self.label.grid(row=y, column=x, sticky = NSEW)

        elif (squareStatus[location] == "greenup"):
            squareStatus[location] = "grayup"
            img = PhotoImage(file="gamefiles/grayup.gif")
            self.label = Label(self, image=img, background="black")
            self.label.image = img
            self.label.grid(row=y, column=x, sticky = NSEW)

        elif (squareStatus[location] == "greendown"):
            squareStatus[location] = "graydown"
            img = PhotoImage(file="gamefiles/graydown.gif")
            self.label = Label(self, image=img, background="black")
            self.label.image = img
            self.label.grid(row=y, column=x, sticky = NSEW)

        elif (squareStatus[location] == "greenleft"):
            squareStatus[location] = "grayleft"
            img = PhotoImage(file="gamefiles/grayleft.gif")
            self.label = Label(self, image=img, background="black")
            self.label.image = img
            self.label.grid(row=y, column=x, sticky = NSEW)

        elif (squareStatus[location] == "greenright"):
            squareStatus[location] = "grayright"
            img = PhotoImage(file="gamefiles/grayright.gif")
            self.label = Label(self, image=img, background="black")
            self.label.image = img
            self.label.grid(row=y, column=x, sticky = NSEW)
        
        
    #make a square green
    def green(self, x, y):
        location = str(x) + str(y)

        #if previous square is regular
        if (squareStatus[location] == "blue" or squareStatus[location] == "green"):
            squareStatus[location] = "green"
            img = PhotoImage(file="gamefiles/green.gif")
            self.label = Label(self, image=img, background="black")
            self.label.image = img
            self.label.grid(row=y, column=x, sticky = NSEW)

        #if previous square is hit
        elif (squareStatus[location] == "bluehit" or squareStatus[location] == "greenhit"):
            squareStatus[location] = "greenhit"
            img = PhotoImage(file="gamefiles/greenhit.gif")
            self.label = Label(self, image=img, background="black")
            self.label.image = img
            self.label.grid(row=y, column=x, sticky = NSEW)

        #if previous square is miss
        elif (squareStatus[location] == "bluemiss" or squareStatus[location] == "greenmiss"):
            squareStatus[location] = "greenmiss"
            img = PhotoImage(file="gamefiles/greenmiss.gif")
            self.label = Label(self, image=img, background="black")
            self.label.image = img
            self.label.grid(row=y, column=x, sticky = NSEW)

        #for placing ships
        elif (squareStatus[location] == "grayhor"):
            squareStatus[location] = "greenhor"
            img = PhotoImage(file="gamefiles/greenhor.gif")
            self.label = Label(self, image=img, background="black")
            self.label.image = img
            self.label.grid(row=y, column=x, sticky = NSEW)

        elif (squareStatus[location] == "grayvert"):
            squareStatus[location] = "greenvert"
            img = PhotoImage(file="gamefiles/greenvert.gif")
            self.label = Label(self, image=img, background="black")
            self.label.image = img
            self.label.grid(row=y, column=x, sticky = NSEW)

        elif (squareStatus[location] == "grayup"):
            squareStatus[location] = "greenup"
            img = PhotoImage(file="gamefiles/greenup.gif")
            self.label = Label(self, image=img, background="black")
            self.label.image = img
            self.label.grid(row=y, column=x, sticky = NSEW)

        elif (squareStatus[location] == "graydown"):
            squareStatus[location] = "greendown"
            img = PhotoImage(file="gamefiles/greendown.gif")
            self.label = Label(self, image=img, background="black")
            self.label.image = img
            self.label.grid(row=y, column=x, sticky = NSEW)

        elif (squareStatus[location] == "grayleft"):
            squareStatus[location] = "greenleft"
            img = PhotoImage(file="gamefiles/greenleft.gif")
            self.label = Label(self, image=img, background="black")
            self.label.image = img
            self.label.grid(row=y, column=x, sticky = NSEW)

        elif (squareStatus[location] == "grayright"):
            squareStatus[location] = "greenright"
            img = PhotoImage(file="gamefiles/greenright.gif")
            self.label = Label(self, image=img, background="black")
            self.label.image = img
            self.label.grid(row=y, column=x, sticky = NSEW)

        
    def gray(self, x, y, rotation):
        
        if (rotation == 0):
            if (shipCount < 5):
                location = str(x) + str(y)
                squareStatus[location] = "greenhor"
                shipPresence[location] = 1
                img = PhotoImage(file="gamefiles/greenhor.gif")
                self.label = Label(self, image=img, background="black")
                self.label.image = img
                self.label.grid(row=y, column=x, sticky = NSEW)

                location = str(x-1) + str(y)
                squareStatus[location] = "greenleft"
                shipPresence[location] = 1
                img = PhotoImage(file="gamefiles/greenleft.gif")
                self.label = Label(self, image=img, background="black")
                self.label.image = img
                self.label.grid(row=y, column=x-1, sticky = NSEW)

                location = str(x+1) + str(y)
                squareStatus[location] = "greenright"
                shipPresence[location] = 1
                img = PhotoImage(file="gamefiles/greenright.gif")
                self.label = Label(self, image=img, background="black")
                self.label.image = img
                self.label.grid(row=y, column=x+1, sticky = NSEW)

            else:
                location = str(x) + str(y)
                squareStatus[location] = "grayhor"
                shipPresence[location] = 1
                img = PhotoImage(file="gamefiles/grayhor.gif")
                self.label = Label(self, image=img, background="black")
                self.label.image = img
                self.label.grid(row=y, column=x, sticky = NSEW)

                location = str(x-1) + str(y)
                squareStatus[location] = "grayleft"
                shipPresence[location] = 1
                img = PhotoImage(file="gamefiles/grayleft.gif")
                self.label = Label(self, image=img, background="black")
                self.label.image = img
                self.label.grid(row=y, column=x-1, sticky = NSEW)

                location = str(x+1) + str(y)
                squareStatus[location] = "grayright"
                shipPresence[location] = 1
                img = PhotoImage(file="gamefiles/grayright.gif")
                self.label = Label(self, image=img, background="black")
                self.label.image = img
                self.label.grid(row=y, column=x+1, sticky = NSEW)

        if (rotation == 1):
            if (shipCount < 5):
                location = str(x) + str(y)
                squareStatus[location] = "greenvert"
                shipPresence[location] = 1
                img = PhotoImage(file="gamefiles/greenvert.gif")
                self.label = Label(self, image=img, background="black")
                self.label.image = img
                self.label.grid(row=y, column=x, sticky = NSEW)

                location = str(x) + str(y-1)
                squareStatus[location] = "greenup"
                shipPresence[location] = 1
                img = PhotoImage(file="gamefiles/greenup.gif")
                self.label = Label(self, image=img, background="black")
                self.label.image = img
                self.label.grid(row=y-1, column=x, sticky = NSEW)

                location = str(x) + str(y+1)
                squareStatus[location] = "greendown"
                shipPresence[location] = 1
                img = PhotoImage(file="gamefiles/greendown.gif")
                self.label = Label(self, image=img, background="black")
                self.label.image = img
                self.label.grid(row=y+1, column=x, sticky = NSEW)

            else:
                location = str(x) + str(y)
                squareStatus[location] = "grayvert"
                shipPresence[location] = 1
                img = PhotoImage(file="gamefiles/grayvert.gif")
                self.label = Label(self, image=img, background="black")
                self.label.image = img
                self.label.grid(row=y, column=x, sticky = NSEW)

                location = str(x) + str(y-1)
                squareStatus[location] = "grayup"
                shipPresence[location] = 1
                img = PhotoImage(file="gamefiles/grayup.gif")
                self.label = Label(self, image=img, background="black")
                self.label.image = img
                self.label.grid(row=y-1, column=x, sticky = NSEW)

                location = str(x) + str(y+1)
                squareStatus[location] = "graydown"
                shipPresence[location] = 1
                img = PhotoImage(file="gamefiles/graydown.gif")
                self.label = Label(self, image=img, background="black")
                self.label.image = img
                self.label.grid(row=y+1, column=x, sticky = NSEW)
        
def titlescreen():
    global title
    global titleStatus

    if (titleStatus == 0):
        
        title.attributes("-fullscreen", True) #fullscreen, no cursor
        title.config(cursor="none")

    img = PhotoImage(file="gamefiles/titleNormal.png")
    title_label = Label(title, image=img, background="black")
    title_label.image = img
    title_label.grid(row=0, column=0, sticky = NSEW)

    title.update_idletasks() #same as mainloop but allows frame to update
    title.update()

    #start title music
    sounds[0].play(loops=-1)
    
    #title screen easter egg
    easter = 1

    #have to let go of blue button then press it for it to start (no holding button)
    while True:
        if (GPIO.input(buttons[0]) == False):
            sleep(0.05)
            
            while True:
                if ((GPIO.input(buttons[1]) == True) and (GPIO.input(buttons[2]) == True)):
                    if (easter == 0):
                        sounds[1].stop()
                        sounds[0].play(loops=-1)
                        
                        img = PhotoImage(file="gamefiles/titleNormal.png")
                        title_label = Label(title, image=img, background="black")
                        title_label.image = img
                        title_label.grid(row=0, column=0, sticky = NSEW)

                        title.update_idletasks()
                        title.update()

                        easter = 1
                        
                    elif (easter == 1):
                        sounds[0].stop()
                        sounds[1].play(loops=-1)

                        img = PhotoImage(file="gamefiles/titleEaster.png")
                        title_label = Label(title, image=img, background="black")
                        title_label.image = img
                        title_label.grid(row=0, column=0, sticky = NSEW)

                        title.update_idletasks()
                        title.update()
                        
                        easter = 0
                        
                    while True:
                        if ((GPIO.input(buttons[1]) == 0) and (GPIO.input(buttons[2]) == 0)):
                            break
                        
                if (GPIO.input(buttons[0]) == True):
                    sounds[0].stop()
                    sounds[1].stop()
                    sounds[7].play()
                    #title.destroy()
                    break
            break



def gameloop():

    #start by displaying the title screen
    titlescreen()

    global title
    global window
    global b1
    global squareStatus
    global shipPresence
    global titleStatus
    global shipCount

    #initial dictionary storing status (hit, miss, or regular) of every square "xy" in grid
    squareStatus = {}

    #dictionary that stores if a ship is in a square to prevent overlap
    shipPresence = {}
    for x in range(10, 18):
        for y in range(1, 9):
            location = str(x) + str(y)
            shipPresence[location] = 0

    #counts how many ships you place (stops at 5)
    shipCount = 0

    #make the game window appear now
    window = Toplevel(title)
    window.config(cursor="none")
    b1 = Game(window)
    b1.setupGUI()
    
    #start an in-game song
    sounds[10].play(loops=-1)

    #render the GUI in the main loop
    #window.mainloop()
    window.update_idletasks() #same as mainloop but allows frame to update
    window.update()

    #have to let go of blue button to start game
    while True:
        if (GPIO.input(buttons[0]) == False):
            break

    #MAIN GAME LOOP#

    ###RIGHT GRID###

    currentx = 13
    currenty = 4
    
    #make a 3-long ship
    b1.green(currentx, currenty)
    b1.green(currentx+1, currenty)
    b1.green(currentx-1, currenty)
    
    #horizontal = 0, vertical = 1
    rotation = 0
    
    window.update_idletasks()
    window.update()
    
    while True:
        
        #test if the joystick is being moved any direction and go that direction
        #joystick is normally 1 and turns to 0 if pressed that direction
        #up is the direction of the wires on the joystick
        pressed = False
        direction = 4
        if ((GPIO.input(joystick[0]) == True) and (GPIO.input(joystick[1]) == True) \
            and (GPIO.input(joystick[2]) == True) and (GPIO.input(joystick[3]) == True) \
            and (GPIO.input(buttons[2]) == False) and (GPIO.input(buttons[1]) == False)):
            sleep(0.05) #this section ensures it doesn't move 2 in one direction
            
            while (not pressed):      
                for i in range(len(joystick)):
                    while (GPIO.input(joystick[i]) == False):
                        direction = i
                        pressed = True

                #blue escape button
                if (GPIO.input(buttons[0]) == True):
                    sounds[10].stop()
                    sounds[7].stop()
                    sleep(0.5)
                    titleStatus = 1
                    window.destroy()
                    gameloop()

                #white rotation button
                if (GPIO.input(buttons[2]) == True):
                    
                    if (rotation == 0):
                        if (currenty != 1 and currenty != 8):
                            sounds[12].play()
                            rotation = 1

                            b1.blue(currentx-1, currenty)
                            b1.blue(currentx+1, currenty)
                            
                            b1.green(currentx, currenty-1)
                            b1.green(currentx, currenty+1)
                        else:
                            sounds[5].play()
                        
                    elif (rotation == 1):
                        if (currentx != 10 and currentx != 17):
                            sounds[12].play()
                            rotation = 0

                            b1.blue(currentx, currenty-1)
                            b1.blue(currentx, currenty+1)
                            
                            b1.green(currentx-1, currenty)
                            b1.green(currentx+1, currenty)
                        else:
                            sounds[5].play()

                    pressed = True
                    direction = 4

                    window.update_idletasks()
                    window.update()

                #red placement button
                if (GPIO.input(buttons[1]) == True):
                    
                    location = str(currentx) + str(currenty)
                    locationup = str(currentx) + str(currenty-1)
                    locationdown = str(currentx) + str(currenty+1)
                    locationleft = str(currentx-1) + str(currenty)
                    locationright = str(currentx+1) + str(currenty)
                    
                    if (rotation == 0):
                        if ((shipPresence[location] == 1) \
                            or (shipPresence[locationleft] == 1) \
                            or (shipPresence[locationright] == 1)):
        
                            sounds[5].play()
                            
                        else:
                            sounds[6].play()
                            shipCount += 1
                            b1.gray(currentx, currenty, rotation)
                            
                                
                            pressed = True
                            direction = 4

                            window.update_idletasks()
                            window.update()
                            
                    if (rotation == 1):
                        if ((shipPresence[location] == 1) \
                            or (shipPresence[locationup] == 1) \
                            or (shipPresence[locationdown] == 1)):
        
                            sounds[5].play()
                            
                        else:
                            sounds[6].play()
                            shipCount += 1
                            b1.gray(currentx, currenty, rotation)
                            
                                
                            pressed = True
                            direction = 4

                            window.update_idletasks()
                            window.update()
                                                    
            if (direction == 3): #UP
                if (rotation == 0):
                    if (currenty != 1):
                        sounds[3].play()
                        b1.blue(currentx, currenty) #change the previous squares to blue
                        b1.blue(currentx-1, currenty)
                        b1.blue(currentx+1, currenty)
                        currentx += 0
                        currenty += -1
                        b1.green(currentx, currenty) #change the new squares to green
                        b1.green(currentx-1, currenty)
                        b1.green(currentx+1, currenty)

                elif (rotation == 1):
                    if (currenty != 2):
                        sounds[3].play()
                        b1.blue(currentx, currenty)
                        b1.blue(currentx, currenty-1)
                        b1.blue(currentx, currenty+1)
                        currentx += 0
                        currenty += -1
                        b1.green(currentx, currenty)
                        b1.green(currentx, currenty-1)
                        b1.green(currentx, currenty+1)

            if (direction == 2): #DOWN
                if (rotation == 0):
                    if (currenty != 8):
                        sounds[3].play()
                        b1.blue(currentx, currenty) 
                        b1.blue(currentx-1, currenty)
                        b1.blue(currentx+1, currenty)
                        currentx += 0
                        currenty += 1
                        b1.green(currentx, currenty)
                        b1.green(currentx-1, currenty)
                        b1.green(currentx+1, currenty)

                elif (rotation == 1):
                    if (currenty != 7):
                        sounds[3].play()
                        b1.blue(currentx, currenty)
                        b1.blue(currentx, currenty-1)
                        b1.blue(currentx, currenty+1)
                        currentx += 0
                        currenty += 1
                        b1.green(currentx, currenty)
                        b1.green(currentx, currenty-1)
                        b1.green(currentx, currenty+1)

            if (direction == 1): #LEFT
                if (rotation == 0):
                    if (currentx != 11):
                        sounds[3].play()
                        b1.blue(currentx, currenty)
                        b1.blue(currentx-1, currenty)
                        b1.blue(currentx+1, currenty)
                        currentx += -1
                        currenty += 0
                        b1.green(currentx, currenty)
                        b1.green(currentx-1, currenty)
                        b1.green(currentx+1, currenty)

                elif (rotation == 1):
                    if (currentx != 10):
                        sounds[3].play()
                        b1.blue(currentx, currenty)
                        b1.blue(currentx, currenty-1)
                        b1.blue(currentx, currenty+1)
                        currentx += -1
                        currenty += 0
                        b1.green(currentx, currenty)
                        b1.green(currentx, currenty-1)
                        b1.green(currentx, currenty+1)

            if (direction == 0): #RIGHT
                if (rotation == 0):
                    if (currentx != 16):
                        sounds[3].play()
                        b1.blue(currentx, currenty)
                        b1.blue(currentx-1, currenty)
                        b1.blue(currentx+1, currenty)
                        currentx += 1
                        currenty += 0
                        b1.green(currentx, currenty)
                        b1.green(currentx-1, currenty)
                        b1.green(currentx+1, currenty)

                elif (rotation == 1):
                    if (currentx != 17):
                        sounds[3].play()
                        b1.blue(currentx, currenty)
                        b1.blue(currentx, currenty-1)
                        b1.blue(currentx, currenty+1)
                        currentx += 1
                        currenty += 0
                        b1.green(currentx, currenty)
                        b1.green(currentx, currenty-1)
                        b1.green(currentx, currenty+1)

            window.update_idletasks()
            window.update()

            #once 5 ships are placed, move on to gameplay
            if (shipCount == 5):
                break




    ###LEFT GRID###

    #make an initial square to make green
    currentx = 4
    currenty = 4
    b1.green(currentx, currenty)
    window.update_idletasks()
    window.update()

    while True:
        
        #test if the joystick is being moved any direction and go that direction
        #joystick is normally 1 and turns to 0 if pressed that direction
        #up is the direction of the wires on the joystick
        pressed = False
        direction = 4
        if ((GPIO.input(joystick[0]) == True) and (GPIO.input(joystick[1]) == True) \
            and (GPIO.input(joystick[2]) == True) and (GPIO.input(joystick[3]) == True)):
            sleep(0.05) #this section ensures it doesn't move 2 in one direction
            
            while (not pressed):      
                for i in range(len(joystick)):
                    while (GPIO.input(joystick[i]) == False):
                        direction = i
                        pressed = True

                if (GPIO.input(buttons[0]) == True):
                    sounds[10].stop()
                    sounds[7].stop()
                    sleep(0.5)
                    titleStatus = 1
                    window.destroy()
                    gameloop()

            if (direction == 3): #UP
                if (currenty != 1):
                    sounds[3].play()
                    b1.blue(currentx, currenty) #change the previous square to blue
                    currentx += 0
                    currenty += -1
                    b1.green(currentx, currenty) #change the new square to green

            if (direction == 2): #DOWN
                if (currenty != 8):
                    sounds[3].play()
                    b1.blue(currentx, currenty)
                    currentx += 0
                    currenty += 1
                    b1.green(currentx, currenty)

            if (direction == 1): #LEFT
                if (currentx != 1):
                    sounds[3].play()
                    b1.blue(currentx, currenty)
                    currentx += -1
                    currenty += 0
                    b1.green(currentx, currenty)

            if (direction == 0): #RIGHT
                if (currentx != 8):
                    sounds[3].play()
                    b1.blue(currentx, currenty)
                    currentx += 1
                    currenty += 0
                    b1.green(currentx, currenty)

            window.update_idletasks()
            window.update()

        


        
###MAIN CODE###

#initialize the mixer and pygame
pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=512)
pygame.init()

            
#setup switches and sounds
joystick = [18, 19, 20, 21]
buttons = [25, 26, 27]
sounds = [
        pygame.mixer.Sound("gamefiles/battleshiptitle.wav"),
        pygame.mixer.Sound("gamefiles/suge.wav"),
        pygame.mixer.Sound("gamefiles/victory.wav"),
        pygame.mixer.Sound("gamefiles/move.wav"),
        pygame.mixer.Sound("gamefiles/select.wav"),
        pygame.mixer.Sound("gamefiles/error.wav"),
        pygame.mixer.Sound("gamefiles/dropship.wav"),
        pygame.mixer.Sound("gamefiles/horn.wav"),
        pygame.mixer.Sound("gamefiles/hitsound.wav"),
        pygame.mixer.Sound("gamefiles/misssound.wav"),
        pygame.mixer.Sound("gamefiles/waves.wav"),
        pygame.mixer.Sound("gamefiles/yousunkmybattleship.wav"),
        pygame.mixer.Sound("gamefiles/rotation.wav")
         ]

#chnage any volumes of tracks (0-1)
sounds[0].set_volume(0.8)
sounds[10].set_volume(0.5)
sounds[3].set_volume(0.7)
sounds[1].set_volume(1)

#setup the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(joystick, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(buttons, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


#makes title only appear once
titleStatus = 0

#initialize window
title = Tk()

###LOOP OF GAME###
gameloop()

