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

                    if (squareStatus[location] == "grayvert"):
                        squareStatus[location] = "grayverthit"
                        img = PhotoImage(file="gamefiles/grayverthit.gif")
                        self.label = Label(self, image=img, background="black")
                        self.label.image = img
                        self.label.grid(row=y, column=x, sticky = NSEW)

                    if (squareStatus[location] == "grayleft"):
                        squareStatus[location] = "graylefthit"
                        img = PhotoImage(file="gamefiles/graylefthit.gif")
                        self.label = Label(self, image=img, background="black")
                        self.label.image = img
                        self.label.grid(row=y, column=x, sticky = NSEW)

                    if (squareStatus[location] == "grayright"):
                        squareStatus[location] = "grayrighthit"
                        img = PhotoImage(file="gamefiles/grayrighthit.gif")
                        self.label = Label(self, image=img, background="black")
                        self.label.image = img
                        self.label.grid(row=y, column=x, sticky = NSEW)

                    if (squareStatus[location] == "grayup"):
                        squareStatus[location] = "grayuphit"
                        img = PhotoImage(file="gamefiles/grayuphit.gif")
                        self.label = Label(self, image=img, background="black")
                        self.label.image = img
                        self.label.grid(row=y, column=x, sticky = NSEW)

                    if (squareStatus[location] == "graydown"):
                        squareStatus[location] = "graydownhit"
                        img = PhotoImage(file="gamefiles/graydownhit.gif")
                        self.label = Label(self, image=img, background="black")
                        self.label.image = img
                        self.label.grid(row=y, column=x, sticky = NSEW)

        self.update_idletasks()
        self.update()
