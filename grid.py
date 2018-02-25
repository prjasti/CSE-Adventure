from tkinter import *
from adventure import *
master = Tk()
master2 = Tk()
w = Canvas(master, width=3000, height=2000)
d = Canvas(master2, width=300, height=200)
d.pack()
w.pack()
squareSize = 75     #Size of each square
loc = [225,225]     #Starting point of the first rectangle, used to keep track of location
currentRoom = 1 #Current room number; assigns room data through this
def moveRight():
    if loc[0] < 675:      #At extreme right of board
        w.move(r,squareSize,0)  #Moves 75 right and 0 up  
        loc[0] += squareSize
        currentRoom += 1
def moveLeft():
    if loc[0] > 225:     #At extreme left of board
        w.move(r,-squareSize,0)
        loc[0] -= squareSize
        currentRoom -= 1
def moveUp():
    if loc[1] > 225:    #At extreme top of board
        w.move(r,0,-squareSize) 
        loc[1] -= squareSize
        currentRoom -= 7
def moveDown():
    if loc[1] < 675:   #At extreme bottom of board
        w.move(r,0,squareSize)
        loc[1] += squareSize
        currentRoom += 7
def enter():
    d = Canvas(master2, width=300, height=200)
    w.pack()
    squareSize = 75;
    loc2 = [225, 225]
    
rightBtn = Button(master, text="Move Right", width=10, command = moveRight)
leftBtn = Button(master, text="Move Left", width=10, command = moveLeft)
upBtn = Button(master, text="Move Up", width=10, command = moveUp)
downBtn = Button(master, text="Move Down", width=10, command = moveDown)
enterBtn = Button(master, text="Enter", width=10, command = enter)
rightBtn.place(x = 1250, y = 400)
leftBtn.place(x = 1000, y = 400)
upBtn.place(x = 1125, y = 300)
downBtn.place(x = 1125, y = 500)
enterBtn.place(x = 1125, y = 400)
for a0 in range(225,750,squareSize):#Creates 49 squares in a grid each of size 75
    for b0 in range(225,750,squareSize):
        w.create_rectangle(a0,b0,a0+65,b0+65, fill="white", outline = "red")
r = w.create_oval(loc[0]+10,loc[1]+10,loc[0]+55,loc[1] + 55, fill = "chartreuse")
w.mainloop()
for a0 in range(225,750,squareSize):#Creates 49 squares in a grid each of size 75
    for b0 in range(225,750,squareSize):
        d.create_rectangle(a0,b0,a0+65,b0+65, fill="white", outline = "red")
r = w.create_oval(loc[0]+10,loc[1]+10,loc[0]+55,loc[1] + 55, fill = "chartreuse")
w.mainloop()
