##############################################################
# Names: Ethan Hebert & Jace Peloquin
# Date: 5-11-21
# Description: This code is the Player 2 component of a
# video game recreation of the famous Battleship boardgame.
# Louisiana Tech CSC-132 Final project.
##############################################################

#here we go
#PLAYER 2

#NOTE - Alt + Esc to exit program

import pygame
from tkinter import *
import RPi.GPIO as GPIO
from time import sleep
from random import randint

class Game(Frame):
    global bgcolor
    
    def __init__(self, container):
        Frame.__init__(self, container, bg=bgcolor)
        container.attributes("-fullscreen", True)

    def setupGUI(self):

        #setup display
        
        #top gap
        self.top = Label(self, height=2, width=100, background=bgcolor)
        self.top.grid(row=0, column=0, columnspan=19)
        
        #left gap
        self.left = Label(self, height=1, width=2, background=bgcolor)
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
        self.mid = Label(self, height=1, width=1, background=bgcolor)
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
        self.right = Label(self, height=1, width=2, background=bgcolor)
        self.right.grid(row=1, column=18, rowspan=10)

        #bottom gap with instructions
        self.bottom = Label(self,  width=50, background=bgcolor, text="", \
                            fg="red", font=("Arial", 20, "bold"), anchor=CENTER, height=2)
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


    #adds locations to the boat dictionaries for sending data later
    def addBoat(self, location):
        
        if (shipCount == 1):
            boat1[location] = 1

        elif (shipCount == 2):
            boat2[location] = 1

        elif (shipCount == 3):
            boat3[location] = 1

        elif (shipCount == 4):
            boat4[location] = 1

        elif (shipCount == 5):
            boat5[location] = 1

        
        
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
                self.addBoat(location)

                location = str(x-1) + str(y)
                squareStatus[location] = "greenleft"
                shipPresence[location] = 1
                img = PhotoImage(file="gamefiles/greenleft.gif")
                self.label = Label(self, image=img, background="black")
                self.label.image = img
                self.label.grid(row=y, column=x-1, sticky = NSEW)
                self.addBoat(location)

                location = str(x+1) + str(y)
                squareStatus[location] = "greenright"
                shipPresence[location] = 1
                img = PhotoImage(file="gamefiles/greenright.gif")
                self.label = Label(self, image=img, background="black")
                self.label.image = img
                self.label.grid(row=y, column=x+1, sticky = NSEW)
                self.addBoat(location)

            else:
                location = str(x) + str(y)
                squareStatus[location] = "grayhor"
                shipPresence[location] = 1
                img = PhotoImage(file="gamefiles/grayhor.gif")
                self.label = Label(self, image=img, background="black")
                self.label.image = img
                self.label.grid(row=y, column=x, sticky = NSEW)
                self.addBoat(location)

                location = str(x-1) + str(y)
                squareStatus[location] = "grayleft"
                shipPresence[location] = 1
                img = PhotoImage(file="gamefiles/grayleft.gif")
                self.label = Label(self, image=img, background="black")
                self.label.image = img
                self.label.grid(row=y, column=x-1, sticky = NSEW)
                self.addBoat(location)

                location = str(x+1) + str(y)
                squareStatus[location] = "grayright"
                shipPresence[location] = 1
                img = PhotoImage(file="gamefiles/grayright.gif")
                self.label = Label(self, image=img, background="black")
                self.label.image = img
                self.label.grid(row=y, column=x+1, sticky = NSEW)
                self.addBoat(location)

        if (rotation == 1):
            if (shipCount < 5):
                location = str(x) + str(y)
                squareStatus[location] = "greenvert"
                shipPresence[location] = 1
                img = PhotoImage(file="gamefiles/greenvert.gif")
                self.label = Label(self, image=img, background="black")
                self.label.image = img
                self.label.grid(row=y, column=x, sticky = NSEW)
                self.addBoat(location)

                location = str(x) + str(y-1)
                squareStatus[location] = "greenup"
                shipPresence[location] = 1
                img = PhotoImage(file="gamefiles/greenup.gif")
                self.label = Label(self, image=img, background="black")
                self.label.image = img
                self.label.grid(row=y-1, column=x, sticky = NSEW)
                self.addBoat(location)

                location = str(x) + str(y+1)
                squareStatus[location] = "greendown"
                shipPresence[location] = 1
                img = PhotoImage(file="gamefiles/greendown.gif")
                self.label = Label(self, image=img, background="black")
                self.label.image = img
                self.label.grid(row=y+1, column=x, sticky = NSEW)
                self.addBoat(location)

            else:
                location = str(x) + str(y)
                squareStatus[location] = "grayvert"
                shipPresence[location] = 1
                img = PhotoImage(file="gamefiles/grayvert.gif")
                self.label = Label(self, image=img, background="black")
                self.label.image = img
                self.label.grid(row=y, column=x, sticky = NSEW)
                self.addBoat(location)

                location = str(x) + str(y-1)
                squareStatus[location] = "grayup"
                shipPresence[location] = 1
                img = PhotoImage(file="gamefiles/grayup.gif")
                self.label = Label(self, image=img, background="black")
                self.label.image = img
                self.label.grid(row=y-1, column=x, sticky = NSEW)
                self.addBoat(location)

                location = str(x) + str(y+1)
                squareStatus[location] = "graydown"
                shipPresence[location] = 1
                img = PhotoImage(file="gamefiles/graydown.gif")
                self.label = Label(self, image=img, background="black")
                self.label.image = img
                self.label.grid(row=y+1, column=x, sticky = NSEW)
                self.addBoat(location)

    def displayText(self, newText):
        self.bottom["text"] = newText
        self.update_idletasks()
        self.update()

    #this function checks which boat you hit
    def boatCheck(self, location):
        global boat1score
        global boat2score
        global boat3score
        global boat4score
        global boat5score

        if (p2boat1[location] == 1):
            boat1score += 1
            if (boat1score == 3):
                sleep(3.5)
                sounds[11].play()

        elif (p2boat2[location] == 1):
            boat2score += 1
            if (boat2score == 3):
                sleep(3.5)
                sounds[11].play()

        elif (p2boat3[location] == 1):
            boat3score += 1
            if (boat3score == 3):
                sleep(3.5)
                sounds[11].play()

        elif (p2boat4[location] == 1):
            boat4score += 1
            if (boat4score == 3):
                sleep(3.5)
                sounds[11].play()

        elif (p2boat5[location] == 1):
            boat5score += 1
            if (boat5score == 3):
                sleep(3.5)
                sounds[11].play()

        sleep(1)

    #this function controls firing at the other player
    def fire(self, x, y):
        location = str(x) + str(y)
        shotsTaken[location] = 1

        if (p2shipPresence[location] == 0): #MISS
            sounds[9].play()
            sendAttack()
            sleep(1.8)
            squareStatus[location] = "greenmiss"
            img = PhotoImage(file="gamefiles/greenmiss.gif")
            self.label = Label(self, image=img, background="black")
            self.label.image = img
            self.label.grid(row=y, column=x, sticky = NSEW)

        
        elif (p2shipPresence[location] == 1): #HIT
            global totalScore
            totalScore += 1
            sounds[8].play()
            sendAttack()
            sleep(1.8)
            squareStatus[location] = "greenhit"
            img = PhotoImage(file="gamefiles/greenhit.gif")
            self.label = Label(self, image=img, background="black")
            self.label.image = img
            self.label.grid(row=y, column=x, sticky = NSEW)
            
        self.update_idletasks()
        self.update()

    #this function displays if your ships have been hit or not
    def updateShips(self, p2shotsTaken):
        global p2totalScore
        
        for x in range(10, 18):
            for y in range(1, 9):
                location = str(x) + str(y)

                if (p2shotsTaken[location] == 1):
                    
                    if (squareStatus[location] == "grayhor"):
                        squareStatus[location] = "grayhorhit"
                        img = PhotoImage(file="gamefiles/grayhorhit.gif")
                        self.label = Label(self, image=img, background="black")
                        self.label.image = img
                        self.label.grid(row=y, column=x, sticky = NSEW)
                        p2totalScore += 1

                    if (squareStatus[location] == "grayvert"):
                        squareStatus[location] = "grayverthit"
                        img = PhotoImage(file="gamefiles/grayverthit.gif")
                        self.label = Label(self, image=img, background="black")
                        self.label.image = img
                        self.label.grid(row=y, column=x, sticky = NSEW)
                        p2totalScore += 1

                    if (squareStatus[location] == "grayleft"):
                        squareStatus[location] = "graylefthit"
                        img = PhotoImage(file="gamefiles/graylefthit.gif")
                        self.label = Label(self, image=img, background="black")
                        self.label.image = img
                        self.label.grid(row=y, column=x, sticky = NSEW)
                        p2totalScore += 1

                    if (squareStatus[location] == "grayright"):
                        squareStatus[location] = "grayrighthit"
                        img = PhotoImage(file="gamefiles/grayrighthit.gif")
                        self.label = Label(self, image=img, background="black")
                        self.label.image = img
                        self.label.grid(row=y, column=x, sticky = NSEW)
                        p2totalScore += 1

                    if (squareStatus[location] == "grayup"):
                        squareStatus[location] = "grayuphit"
                        img = PhotoImage(file="gamefiles/grayuphit.gif")
                        self.label = Label(self, image=img, background="black")
                        self.label.image = img
                        self.label.grid(row=y, column=x, sticky = NSEW)
                        p2totalScore += 1

                    if (squareStatus[location] == "graydown"):
                        squareStatus[location] = "graydownhit"
                        img = PhotoImage(file="gamefiles/graydownhit.gif")
                        self.label = Label(self, image=img, background="black")
                        self.label.image = img
                        self.label.grid(row=y, column=x, sticky = NSEW)
                        p2totalScore += 1

                    if (squareStatus[location] == "blue"):
                        squareStatus[location] = "bluemiss"
                        img = PhotoImage(file="gamefiles/bluemiss.gif")
                        self.label = Label(self, image=img, background="black")
                        self.label.image = img
                        self.label.grid(row=y, column=x, sticky = NSEW)

        print("Other player's score:")
        print(p2totalScore)
        self.update_idletasks()
        self.update()

#send data set of where you fired to other player
def sendAttack():
    print("Now sending data...")
    for x in range(1, 9):
        for y in range(1, 9):
            location = str(x) + str(y)
            print(location)
            
            while True:
                if (GPIO.input(receivers[1]) == False):
                    break
            print("Receiver off")
            
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

    print("Data sent.")
    #move on from the data transfer
    GPIO.output(senders[0], 1)
    sleep(0.5)
    GPIO.output(senders[0], 0)

def titlescreen():
    global title
    global titleStatus
    GPIO.output(senders[2], 0)

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
    #sounds[0].play(loops=-1)

    #default background color
    global bgcolor
    bgcolor = "white"
    
    #title screen easter egg
    easter = 1

    #have to let go of blue button then press it for it to start (no holding button)
    while True:
        if (GPIO.input(buttons[0]) == False):
            sleep(0.05)
            
            while True:
                GPIO.output(senders[2], 0)
                GPIO.output(senders[1], 0)

                #tell other player you've pressed both buttons
                if ((GPIO.input(buttons[1]) == True) and (GPIO.input(buttons[2]) == True)):
                    GPIO.output(senders[2], 1)
                    sleep(0.2)
                    GPIO.output(senders[2], 0)

                #player 1 telling you to switch screen
                if (GPIO.input(receivers[2]) == True):

                    GPIO.output(senders[1], 1)
                    
                    if (easter == 0):
                        sounds[1].stop()
                        #sounds[0].play(loops=-1)
                        bgcolor = "white"
                        
                        img = PhotoImage(file="gamefiles/titleNormal.png")
                        title_label = Label(title, image=img, background="black")
                        title_label.image = img
                        title_label.grid(row=0, column=0, sticky = NSEW)

                        title.update_idletasks()
                        title.update()

                        easter = 1
                        
                    elif (easter == 1):
                        sounds[0].stop()
                        #sounds[1].play(loops=-1)
                        bgcolor = "black"

                        img = PhotoImage(file="gamefiles/titleEaster.png")
                        title_label = Label(title, image=img, background="black")
                        title_label.image = img
                        title_label.grid(row=0, column=0, sticky = NSEW)

                        title.update_idletasks()
                        title.update()
                        
                        easter = 0
                        
                    while True:
                        if ((GPIO.input(buttons[1]) == 0) and (GPIO.input(buttons[2]) == 0) \
                            and (GPIO.input(receivers[2]) == 0)):
                            GPIO.output(senders[2], 0)
                            break

                #blue button
                if (GPIO.input(buttons[0]) == True):
                    GPIO.output(senders[2], 0)
                    GPIO.output(senders[1], 0)
                    sounds[0].stop()
                    sounds[1].stop()
                    #sounds[7].play()
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
    global p2shipPresence
    global titleStatus
    global shipCount
    global myTurn
    global totalScore
    global p2totalScore
    global shotsTaken
    global p2shotsTaken
    global boat1
    global boat2
    global boat3
    global boat4
    global boat5
    global p2boat1
    global p2boat2
    global p2boat3
    global p2boat4
    global p2boat5
    global boat1score
    global boat2score
    global boat3score
    global boat4score
    global boat5score

    #scores start at 0
    totalScore = 0
    p2totalScore = 0
    boat1score = 0
    boat2score = 0
    boat3score = 0
    boat4score = 0
    boat5score = 0

    #player 2 - goes second
    myTurn = 0

    #initial dictionary storing status (hit, miss, or regular) of every square "xy" in grid
    squareStatus = {}

    #dictionary that stores if a ship is in a square to prevent overlap
    shipPresence = {}
    for x in range(10, 18):
        for y in range(1, 9):
            location = str(x) + str(y)
            shipPresence[location] = 0

    #tracks the other player's ships
    p2shipPresence = {}
    for x in range(1, 9):
        for y in range(1, 9):
            location = str(x) + str(y)
            p2shipPresence[location] = 0

    #keeps track of where you've already shot to prevent repeats
    shotsTaken = {}
    for x in range(1, 9):
        for y in range(1, 9):
            location = str(x) + str(y)
            shotsTaken[location] = 0

    #keeps track of where the other player has shot
    p2shotsTaken = {}
    for x in range(10, 18):
        for y in range(1, 9):
            location = str(x) + str(y)
            p2shotsTaken[location] = 0

    #where my boats are
    boat1 = {}
    for x in range(10, 18):
        for y in range(1, 9):
            location = str(x) + str(y)
            boat1[location] = 0

    boat2 = {}
    for x in range(10, 18):
        for y in range(1, 9):
            location = str(x) + str(y)
            boat2[location] = 0

    boat3 = {}
    for x in range(10, 18):
        for y in range(1, 9):
            location = str(x) + str(y)
            boat3[location] = 0

    boat4 = {}
    for x in range(10, 18):
        for y in range(1, 9):
            location = str(x) + str(y)
            boat4[location] = 0

    boat5 = {}
    for x in range(10, 18):
        for y in range(1, 9):
            location = str(x) + str(y)
            boat5[location] = 0

    #where their boats are
    p2boat1 = {}
    for x in range(1, 9):
        for y in range(1, 9):
            location = str(x) + str(y)
            p2boat1[location] = 0

    p2boat2 = {}
    for x in range(1, 9):
        for y in range(1, 9):
            location = str(x) + str(y)
            p2boat2[location] = 0

    p2boat3 = {}
    for x in range(1, 9):
        for y in range(1, 9):
            location = str(x) + str(y)
            p2boat3[location] = 0

    p2boat4 = {}
    for x in range(1, 9):
        for y in range(1, 9):
            location = str(x) + str(y)
            p2boat4[location] = 0

    p2boat5 = {}
    for x in range(1, 9):
        for y in range(1, 9):
            location = str(x) + str(y)
            p2boat5[location] = 0
    

    #start with all senders off
    GPIO.output(senders[0], 0)
    GPIO.output(senders[1], 0)
    GPIO.output(senders[2], 0)


    #counts how many ships you place (stops at 5)
    shipCount = 0

    #make the game window appear now
    window = Toplevel(title)
    window.config(cursor="none")
    b1 = Game(window)
    b1.setupGUI()
    
    #start an in-game song
    #sounds[10].play(loops=-1)

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

        if (myTurn == 0):
            b1.displayText("Waiting for Player 1...")

        #see if it's your turn or not
        while True:
            if (myTurn == 1):
                break
            
            if (GPIO.input(receivers[0]) == True):
                myTurn = 1

            #blue escape button
            if (GPIO.input(buttons[0]) == True):
                sounds[10].stop()
                sounds[7].stop()
                sleep(0.5)
                titleStatus = 1
                window.destroy()
                gameloop()
            
        b1.displayText("Place your ship")
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

                            #now it's the other player's turn
                            GPIO.output(senders[0], 1)
                            myTurn = 0
                            
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

                            #now it's the other player's turn
                            GPIO.output(senders[0], 1)
                            myTurn = 0
                                                    
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

            GPIO.output(senders[0], 0)

            #once 5 ships are placed, move on to gameplay
            if (shipCount == 5):
                #print(squareStatus) # - to test if the ships are stored in right locations
                #print(shipPresence) # - ditto
                break

            if (myTurn == 0):
                b1.displayText("Waiting for Player 1...")

    b1.displayText("Loading the missiles...")

    #exchange ship data with other player (sender)
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

    #send each individual boat data
    for x in range(10, 18):
        for y in range(1, 9):
            
            myLocation = str(x) + str(y)
            theirLocation = str(x-9) + str(y)
            while True:
                if ((GPIO.input(receivers[1]) == False) and (GPIO.input(receivers[2]) == False)):
                    break
            
            if (boat1[myLocation] == 0): #you have no ship
                GPIO.output(senders[1], 1)
                GPIO.output(senders[2], 0)
            elif (boat1[myLocation] == 1): #you have ship
                GPIO.output(senders[1], 0)
                GPIO.output(senders[2], 1)


            while True:
                if (GPIO.input(receivers[1]) == True): #they have no ship
                    p2boat1[theirLocation] = 0
                    GPIO.output(senders[1], 0)
                    GPIO.output(senders[2], 0)
                    break

                elif (GPIO.input(receivers[2]) == True): #they have ship
                    p2boat1[theirLocation] = 1
                    GPIO.output(senders[1], 0)
                    GPIO.output(senders[2], 0)
                    break

    for x in range(10, 18):
        for y in range(1, 9):
            
            myLocation = str(x) + str(y)
            theirLocation = str(x-9) + str(y)
            while True:
                if ((GPIO.input(receivers[1]) == False) and (GPIO.input(receivers[2]) == False)):
                    break
            
            if (boat2[myLocation] == 0): #you have no ship
                GPIO.output(senders[1], 1)
                GPIO.output(senders[2], 0)
            elif (boat2[myLocation] == 1): #you have ship
                GPIO.output(senders[1], 0)
                GPIO.output(senders[2], 1)


            while True:
                if (GPIO.input(receivers[1]) == True): #they have no ship
                    p2boat2[theirLocation] = 0
                    GPIO.output(senders[1], 0)
                    GPIO.output(senders[2], 0)
                    break

                elif (GPIO.input(receivers[2]) == True): #they have ship
                    p2boat2[theirLocation] = 1
                    GPIO.output(senders[1], 0)
                    GPIO.output(senders[2], 0)
                    break

    for x in range(10, 18):
        for y in range(1, 9):
            
            myLocation = str(x) + str(y)
            theirLocation = str(x-9) + str(y)
            while True:
                if ((GPIO.input(receivers[1]) == False) and (GPIO.input(receivers[2]) == False)):
                    break
            
            if (boat3[myLocation] == 0): #you have no ship
                GPIO.output(senders[1], 1)
                GPIO.output(senders[2], 0)
            elif (boat3[myLocation] == 1): #you have ship
                GPIO.output(senders[1], 0)
                GPIO.output(senders[2], 1)


            while True:
                if (GPIO.input(receivers[1]) == True): #they have no ship
                    p2boat3[theirLocation] = 0
                    GPIO.output(senders[1], 0)
                    GPIO.output(senders[2], 0)
                    break

                elif (GPIO.input(receivers[2]) == True): #they have ship
                    p2boat3[theirLocation] = 1
                    GPIO.output(senders[1], 0)
                    GPIO.output(senders[2], 0)
                    break

    for x in range(10, 18):
        for y in range(1, 9):
            
            myLocation = str(x) + str(y)
            theirLocation = str(x-9) + str(y)
            while True:
                if ((GPIO.input(receivers[1]) == False) and (GPIO.input(receivers[2]) == False)):
                    break
            
            if (boat4[myLocation] == 0): #you have no ship
                GPIO.output(senders[1], 1)
                GPIO.output(senders[2], 0)
            elif (boat4[myLocation] == 1): #you have ship
                GPIO.output(senders[1], 0)
                GPIO.output(senders[2], 1)


            while True:
                if (GPIO.input(receivers[1]) == True): #they have no ship
                    p2boat4[theirLocation] = 0
                    GPIO.output(senders[1], 0)
                    GPIO.output(senders[2], 0)
                    break

                elif (GPIO.input(receivers[2]) == True): #they have ship
                    p2boat4[theirLocation] = 1
                    GPIO.output(senders[1], 0)
                    GPIO.output(senders[2], 0)
                    break

    for x in range(10, 18):
        for y in range(1, 9):
            
            myLocation = str(x) + str(y)
            theirLocation = str(x-9) + str(y)
            while True:
                if ((GPIO.input(receivers[1]) == False) and (GPIO.input(receivers[2]) == False)):
                    break
            
            if (boat5[myLocation] == 0): #you have no ship
                GPIO.output(senders[1], 1)
                GPIO.output(senders[2], 0)
            elif (boat5[myLocation] == 1): #you have ship
                GPIO.output(senders[1], 0)
                GPIO.output(senders[2], 1)


            while True:
                if (GPIO.input(receivers[1]) == True): #they have no ship
                    p2boat5[theirLocation] = 0
                    GPIO.output(senders[1], 0)
                    GPIO.output(senders[2], 0)
                    break

                elif (GPIO.input(receivers[2]) == True): #they have ship
                    p2boat5[theirLocation] = 1
                    GPIO.output(senders[1], 0)
                    GPIO.output(senders[2], 0)
                    break

    

    #tell p1 to go to next game phase
    GPIO.output(senders[1], 1)
    sleep(0.05)
    GPIO.output(senders[1], 0)

    GPIO.output(senders[1], 0)
    GPIO.output(senders[2], 0)

    b1.displayText("Waiting for Player 1...")

    
    """
    print("My ships:")
    print(shipPresence)
    print()
    print("Their ships:")
    print(p2shipPresence)
    print()
    print("My boat1:")
    print(boat1)
    print()
    print("Their boat1:")
    print(p2boat1)
    print()
    print("My boat2:")
    print(boat2)
    print()
    print("Their boat2:")
    print(p2boat2)
    print()
    print("My boat3:")
    print(boat3)
    print()
    print("Their boat3:")
    print(p2boat3)
    print()
    print("My boat4:")
    print(boat4)
    print()
    print("Their boat4:")
    print(p2boat4)
    print()
    print("My boat5:")
    print(boat5)
    print()
    print("Their boat5:")
    print(p2boat5)
    """       




    ###LEFT GRID#########################################################################

    #make an initial square to make green
    currentx = 4
    currenty = 4
    b1.green(currentx, currenty)
    window.update_idletasks()
    window.update()

    #Player 2 goes second
    myTurn = 0

    GPIO.output(senders[0], 0)

    while True:
        GPIO.output(senders[1], 0)
        GPIO.output(senders[2], 0)

        while True:
            if (myTurn == 1):
                break
            
            #receive data set to see where other player fired
            for x in range(10, 18):
                for y in range(1, 9):
                    location = str(x) + str(y)
                    GPIO.output(senders[1], 0)
                    
                    while True:
                        print("Waiting...")
                        if (GPIO.input(receivers[1]) == True): #they haven't shot there
                            p2shotsTaken[location] = 0
                            break
                        elif (GPIO.input(receivers[2]) == True): #they have shot there
                            p2shotsTaken[location] = 1
                            break

                        #blue escape button
                        if (GPIO.input(buttons[0]) == True):
                            sounds[10].stop()
                            sounds[7].stop()
                            sleep(0.5)
                            titleStatus = 1
                            window.destroy()
                            gameloop()

                    GPIO.output(senders[1], 1)
                    sleep(0.01)
                    
            print("Got out")
            
            #wait for p1 to move on from data transfer
            while True:
                if (GPIO.input(receivers[0]) == True):
                    GPIO.output(senders[1], 0)
                    GPIO.output(senders[2], 0)
                    break

            sleep(2.3)
            b1.updateShips(p2shotsTaken)

            print()
            print("Their shots:")
            print(p2shotsTaken)
            print("Data received")
            sleep(3.3)
            myTurn = 1

            #blue escape button
            if (GPIO.input(buttons[0]) == True):
                sounds[10].stop()
                sounds[7].stop()
                sleep(0.5)
                titleStatus = 1
                window.destroy()
                gameloop()

        #check if game is over
        if (totalScore == 15):
            sleep(1)
            b1.displayText("YOU WIN")
            sounds[10].stop()
            #sounds[2].play(loops=-1)
            break

        if (p2totalScore == 15):
            sleep(2.1)
            b1.displayText("YOU LOSE")
            sounds[10].stop()
            #sounds[2].play(loops=-1)
            break

                
        b1.displayText("Fire at Player 1")
        #test if the joystick is being moved any direction and go that direction
        #joystick is normally 1 and turns to 0 if pressed that direction
        #up is the direction of the wires on the joystick
        pressed = False
        direction = 4
        if ((GPIO.input(joystick[0]) == True) and (GPIO.input(joystick[1]) == True) \
            and (GPIO.input(joystick[2]) == True) and (GPIO.input(joystick[3]) == True) \
            and (GPIO.input(buttons[1]) == False)):
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

                #red fire button
                if (GPIO.input(buttons[1]) == True):
                    location = str(currentx) + str(currenty)
                    
                    if (shotsTaken[location] == 1): #can't shoot same place twice
                        sounds[5].play()
                    else:
                        b1.fire(currentx, currenty)

                        #see if you sunk a battleship
                        location = str(currentx) + str(currenty)
                        b1.boatCheck(location)                   

                        print()
                        print("My shots:")
                        print(shotsTaken)
                        
                        pressed = True
                        myTurn = 0                

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

            GPIO.output(senders[1], 0)
            GPIO.output(senders[2], 0)

            #check if game is over
            if (totalScore == 15):
                sleep(1)
                b1.displayText("YOU WIN")
                sounds[10].stop()
                #sounds[2].play(loops=-1)
                break

            if (p2totalScore == 15):
                sleep(2.1)
                b1.displayText("YOU LOSE")
                sounds[10].stop()
                #sounds[2].play(loops=-1)
                break
            
            if (myTurn == 0):
                b1.displayText("Waiting for Player 1...")

            

    #end game screen
    while True:
        #blue escape button
        if (GPIO.input(buttons[0]) == True):
            sounds[10].stop()
            sounds[7].stop()
            sounds[2].stop()
            sleep(0.5)
            titleStatus = 1
            window.destroy()
            gameloop()


        
###MAIN CODE###

#initialize the mixer and pygame
pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=1024)
pygame.mixer.init()
pygame.init()

            
#setup switches and sounds
joystick = [18, 19, 20, 21]
buttons = [25, 26, 27]
senders = [17, 16, 13]
receivers = [6, 5, 4]
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

#change any volumes of tracks (0-1)
sounds[0].set_volume(0.8)
sounds[10].set_volume(0.5)
sounds[3].set_volume(0.7)
sounds[1].set_volume(1)

#setup the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(joystick, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(buttons, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(senders, GPIO.OUT)
GPIO.setup(receivers, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


#makes title only appear once
titleStatus = 0

#initialize window
title = Tk()

###LOOP OF GAME###
gameloop()

