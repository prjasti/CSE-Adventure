from tkinter import *
from adventure import *
master = Tk()
w = Canvas(master, width=3000, height=2000)
w.pack()
squareSize = 75     #Size of each square
loc = [225,225]     #Starting point of the first rectangle, used to keep track of location
currentRoom = [1] #Current room number; assigns room data through this
def moveRight():
    if rooms[currentRoom[0]].locked == True:  #Room to the right
        g = raw_input("This room is locked. Use C4? Y/N")
        if g == 'Y':
            if Item('C4','C4',0,0,0,0,0) not in player.backpack:
                rooms[currentRoom[0]].locked = False 
            else:
               print("You have no C4") 
    else:
        if loc[0] < 675:      #At extreme right of board
            w.move(r,squareSize,0)  #Moves 75 right and 0 up  
            loc[0] += squareSize
            currentRoom[0] += 1
def moveLeft():
    if rooms[currentRoom[0]-2].locked == True:  #Room to the left
        g = raw_input("This room is locked. Use C4? Y/N")
        if g == 'Y':
            if Item('C4','C4',0,0,0,0,0) not in player.backpack:
                rooms[currentRoom[0]-2].locked = False
            else:
               print("You have no C4") 
    else:
        if loc[0] > 225:     #At extreme left of board
            w.move(r,-squareSize,0)
            loc[0] -= squareSize
            currentRoom[0] -= 1
def moveUp():
    if rooms[currentRoom[0]-8].locked == True:  #Room to the top
        g = raw_input("This room is locked. Use C4? Y/N")
        if g == 'Y':
            if Item('C4','C4',0,0,0,0,0) not in player.backpack:
                rooms[currentRoom[0]-8].locked = False
            else:
               print("You have no C4") 
    else:
        if loc[1] > 225:     #Room to the bottom
            w.move(r,0,-squareSize) 
            loc[1] -= squareSize
            currentRoom[0] -= 7
def moveDown():
    if rooms[currentRoom[0]+6].locked == True:
        g = raw_input("This room is locked. Use C4? Y/N")
        if g == 'Y':
            if Item('C4','C4',0,0,0,0,0) not in player.backpack:
                rooms[currentRoom[0]+6].locked = False
            else:
               print("You have no C4") 
    else:
        if loc[1] < 675:   #At extreme bottom of board
            w.move(r,0,squareSize)
            loc[1] += squareSize
            currentRoom[0] += 7
def displayBackpack():
    for i, f in enumerate(player.backpack):
        print(str(i+1) + " " + f.displayStats())
    g = raw_input("What would you like to drop? Press 0 for nothing")
    if int(g) != 0:
        player.dropItem(player.backpack[int(g) - 1])
def enter():
    if not rooms[currentRoom[0]-1].lightsOn:
        print("This simulation is offline. Get to the center to restart it.")
    else:
        if currentRoom[0] == 25:
            print("All offline simulations are now restarted.")
            rooms[3].lightsOn = True
            rooms[21].lightsOn = True
            rooms[27].lightsOn = True
            rooms[45].lightsOn = True
        print("Current Room: " + str(currentRoom[0]))
        for i, p in enumerate(rooms[currentRoom[0] - 1].furniture):
            print(str(i+1) + "  " + p.item.displayStats())
        taken = raw_input("Pick an item to take from the list using its number or enter \'leave\'.")
        if taken == "leave" or int(taken) not in range(1,len(rooms[currentRoom[0] - 1].furniture)+1):
            print("You have left the room.")
        else:
            taken = int(taken)
            itm = rooms[currentRoom[0]-1].furniture[taken-1].item
            if len(player.backpack) < player.backpackLimit or itm.classification in ["Space", "Health"]:
                player.addItem(itm)
                rooms[currentRoom[0]-1].furniture.remove((rooms[currentRoom[0] - 1].furniture[taken-1]))
            else:
                print("Your inventory is full. Get a modification to add more space or drop an item.")
rightBtn = Button(master, text="Move Right", width=10, command = moveRight)
leftBtn = Button(master, text="Move Left", width=10, command = moveLeft)
upBtn = Button(master, text="Move Up", width=10, command = moveUp)
downBtn = Button(master, text="Move Down", width=10, command = moveDown)
enterBtn = Button(master, text="Enter/Refresh", width=15, command = enter)
displayBtn = Button(master, text = "Backpack", width = 10, command = displayBackpack)
rightBtn.place(x = 1250, y = 400)
leftBtn.place(x = 1000, y = 400)
upBtn.place(x = 1125, y = 300)
downBtn.place(x = 1125, y = 500)
enterBtn.place(x = 1100, y = 400)
displayBtn.place(x = 1125, y = 600)
for a0 in range(225,750,squareSize):#Creates 49 squares in a grid each of size 75
    for b0 in range(225,750,squareSize):
        w.create_rectangle(a0,b0,a0+65,b0+65, fill="white", outline = "red")
r = w.create_oval(loc[0]+10,loc[1]+10,loc[0]+55,loc[1] + 55, fill = "chartreuse")
w.mainloop()
