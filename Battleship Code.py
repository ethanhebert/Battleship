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


def titlescreen():
    global title
    global titleStatus

    if (titleStatus == 0):
        
        title.attributes("-fullscreen", True)

        title_label = Label(title, text="BATTLESHIP", font=("Helvetica", 18))
        title_label.pack()

    title.update_idletasks() #same as mainloop but allows frame to update
    title.update()

    #start the title music
    sounds[0].play(loops=-1)

    #have to let go of blue button then press it for it to start (no holding button)
    while True:
        if (GPIO.input(buttons[0]) == False):
            sleep(0.05)
            while True:
                if (GPIO.input(buttons[0]) == True):
                    sounds[0].stop()
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
    global titleStatus

    #initial dictionary storing status (hit, miss, or regular) of every square "xy" in grid
    squareStatus = {}

    #make the game window appear now
    window = Toplevel(title)
    b1 = Game(window)
    b1.setupGUI()
    
    #start an in-game song
    sounds[1].play(loops=-1)

    #make an initial square to make green
    currentx = 4
    currenty = 4
    b1.green(currentx, currenty)

    #render the GUI in the main loop
    #window.mainloop()
    window.update_idletasks() #same as mainloop but allows frame to update
    window.update()

    #have to let go of blue button to start game
    while True:
        if (GPIO.input(buttons[0]) == False):
            break

    #MAIN GAME LOOP#
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
                    sounds[1].stop()
                    sleep(0.5)
                    titleStatus = 1
                    window.destroy()
                    gameloop()

            if (direction == 3): #UP
                if (currenty != 1):
                    b1.blue(currentx, currenty) #change the previous square to blue
                    currentx += 0
                    currenty += -1
                    b1.green(currentx, currenty) #change the new square to green

            if (direction == 2): #DOWN
                if (currenty != 8):
                    b1.blue(currentx, currenty)
                    currentx += 0
                    currenty += 1
                    b1.green(currentx, currenty)

            if (direction == 1): #LEFT
                if (currentx != 1):
                    b1.blue(currentx, currenty)
                    currentx += -1
                    currenty += 0
                    b1.green(currentx, currenty)

            if (direction == 0): #RIGHT
                if (currentx != 8):
                    b1.blue(currentx, currenty)
                    currentx += 1
                    currenty += 0
                    b1.green(currentx, currenty)

            window.update_idletasks()
            window.update()


        
###MAIN CODE###

#initialize pygame
pygame.init()

#setup switches and sounds
joystick = [18, 19, 20, 21]
buttons = [25]
sounds = [
        pygame.mixer.Sound("gamefiles/battleshiptitle.wav"),
        pygame.mixer.Sound("gamefiles/suge.wav")
         ]

sounds[0].set_volume(0.5)

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

