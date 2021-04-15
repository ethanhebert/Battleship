#here we go

import pygame
from tkinter import *

class Game(Frame):
    #class variables
    
    def __init__(self, container):
        Frame.__init__(self, container)

    def setupGUI(self):

        #setup display
        #self.display = Label(self, height=1, width=WIDTH, background="white")
        #self.display.grid(row=0, column=0, columnspan=10)

        #setup the 2 grids and gaps in between
        
        #top gap
        self.top = Label(self, height=1, width=100, background="light gray")
        self.top.grid(row=0, column=0, columnspan=19)
        
        #left gap
        self.left = Label(self, height=1, width=2, background="light gray")
        self.left.grid(row=1, column=0, rowspan=10)
        
        #left grid
        for i in range(0,8):
            for j in range(0,8):
                img = PhotoImage(file="gamefiles/blue.gif")
                self.label = Label(self, image=img, background="black")
                self.label.image = img
                self.label.grid(row=1+i, column=j+1, sticky = NSEW)

        #middle gap
        self.mid = Label(self, height=1, width=1, background="light gray")
        self.mid.grid(row=0, column=9, rowspan=10)

        #right grid
        for i in range(0,8):
            for j in range(0,8):
                img = PhotoImage(file="gamefiles/blue.gif")
                self.label = Label(self, image=img, background="black")
                self.label.image = img
                self.label.grid(row=1+i, column=10+j, sticky = NSEW)

        #right gap
        self.right = Label(self, height=1, width=2, background="light gray")
        self.right.grid(row=1, column=18, rowspan=10)

        #bottom gap
        self.bottom = Label(self,  width=100, background="light gray")
        self.bottom.grid(row=9, column=0, columnspan=19)

        #display it all once done
        self.pack(fill=BOTH, expand=1)

        
        

        
###MAIN CODE###
#default screen size
WIDTH = 765
HEIGHT = 450

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

#render the GUI in the main loop
window.mainloop()

