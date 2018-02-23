from tkinter import *
master = Tk()
w = Canvas(master, width=3000, height=2000)
w.pack()
squareSize = 75     #Size of each square
loc = [225,225]     #Starting point of the first rectangle, used to keep track of location
def moveRight():
    if loc[0] < 675:      #At extreme right of board
        w.move(r,squareSize,0)  #Moves 75 right and 0 up  
        loc[0] += squareSize
def moveLeft():
    if loc[0] > 225:     #At extreme left of board
        w.move(r,-squareSize,0)
        loc[0] -= squareSize
def moveUp():
    if loc[1] > 225:    #At extreme top of board
        w.move(r,0,-squareSize) 
        loc[1] -= squareSize
def moveDown():
    if loc[1] < 675:   #At extreme bottom of board
        w.move(r,0,squareSize)
        loc[1] += squareSize
rightBtn = Button(master, text="Move Right", width=10, command = moveRight)
leftBtn = Button(master, text="Move Left", width=10, command = moveLeft)
upBtn = Button(master, text="Move Up", width=10, command = moveUp)
downBtn = Button(master, text="Move Down", width=10, command = moveDown)
rightBtn.place(x = 1200, y = 400)
leftBtn.place(x = 1050, y = 400)
upBtn.place(x = 1125, y = 300)
downBtn.place(x = 1125, y = 500)
for a0 in range(225,750,squareSize):#Creates 49 squares in a grid each of size 75
    for b0 in range(225,750,squareSize):
        w.create_rectangle(a0,b0,a0+65,b0+65, fill="white", outline = "red")
r = w.create_oval(loc[0]+10,loc[1]+10,loc[0]+55,loc[1] + 55, fill = "chartreuse")
w.mainloop()
