location = str(x) + str(y)

        if (p2shipPresence[location] == 0): #MISS
            sounds[9].play()
            squareStatus[location] = "bluemiss"
            img = PhotoImage(file="gamefiles/bluemiss.gif")
            self.label = Label(self, image=img, background="black")
            self.label.image = img
            self.label.grid(row=y, column=x, sticky = NSEW)

        
        elif (p2shipPresence[location] == 1): #HIT
            global totalScore
            totalScore += 1
            print(totalScore)
            sounds[8].play()
            squareStatus[location] = "bluehit"
            img = PhotoImage(file="gamefiles/bluehit.gif")
            self.label = Label(self, image=img, background="black")
            self.label.image = img
            self.label.grid(row=y, column=x, sticky = NSEW)

        self.update_idletasks()
        self.update()
