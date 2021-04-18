#here we go

#NOTE - Alt + Esc to exit program

import pygame
from tkinter import *
import RPi.GPIO as GPIO
from time import sleep

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
        for i in range(0,8):
            for j in range(0,8):
                img = PhotoImage(file="gamefiles/blue.gif")
                self.label = Label(self, image=img, background="black")
                self.label.image = img
                self.label.grid(row=1+i, column=j+1, sticky = NSEW)

        #middle gap
        self.mid = Label(self, height=1, width=1, background="white")
        self.mid.grid(row=0, column=9, rowspan=10)

        #right grid
        for i in range(0,8):
            for j in range(0,8):
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
        img = PhotoImage(file="gamefiles/blue.gif")
        self.label = Label(self, image=img, background="black")
        self.label.image = img
        self.label.grid(row=y, column=x, sticky = NSEW)
        
    #make a square green
    def green(self, x, y):
        img = PhotoImage(file="gamefiles/green.gif")
        self.label = Label(self, image=img, background="black")
        self.label.image = img
        self.label.grid(row=y, column=x, sticky = NSEW)

        
        
###MAIN CODE###
#default screen size
WIDTH = 765
HEIGHT = 450

#setup switches and sounds
joystick = [18, 19, 20, 21]

#setup the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(joystick, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#initialize the window        
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("Battleship")
window.configure(background="light gray")

#initialize pygame
pygame.init()

#create an instance of the game
b1 = Game(window)
b1.setupGUI()

#make an initial square to make green
currentx = 4
currenty = 4
b1.green(currentx, currenty)

#render the GUI in the main loop
#window.mainloop()
window.update_idletasks() #same as mainloop but allows frame to update
window.update()



###LOOP OF GAME###
while True:

    #test if the joystick is being moved any direction and go that direction
    pressed = False
    while (not pressed):      
        for i in range(len(joystick)):
            while (GPIO.input(joystick[i]) == True):
                direction = i
                pressed = True

    if (direction == 0): #UP
        if (currenty != 1):
            b1.blue(currentx, currenty) #change the previous square to blue
            currentx += 0
            currenty += -1
            b1.green(currentx, currenty) #change the new square to green

    if (direction == 1): #DOWN
        if (currenty != 8):
            b1.blue(currentx, currenty)
            currentx += 0
            currenty += 1
            b1.green(currentx, currenty)

    if (direction == 2): #LEFT
        if (currentx != 1):
            b1.blue(currentx, currenty)
            currentx += -1
            currenty += 0
            b1.green(currentx, currenty)

    if (direction == 3): #RIGHT
        if (currentx != 8):
            b1.blue(currentx, currenty)
            currentx += 1
            currenty += 0
            b1.green(currentx, currenty)

    window.update_idletasks()
    window.update()

    sleep(0.2) #a little gap so it doesn't read the same direction multiple times


    

