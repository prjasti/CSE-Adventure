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
        g = raw_input("This room is locked. Use C4?\n Y/N\n>>\t")
        if g in ['Y','y','Yes','yes']:
            itemNames = [o.name for o in player.backpack]
            if 'C4' in itemNames:
                rooms[currentRoom[0]].locked = False
                print("Room " + str(currentRoom[0]+1) + " has been breached. You may enter, but \nit is possible you have alerted the splicers of your location.\n")
            else:
               print("You have no C4.\n")
        else:
            print("Very well, then.\n") 
    else:
        if loc[0] < 675:      #At extreme right of board
            w.move(r,squareSize,0)  #Moves 75 right and 0 up  
            loc[0] += squareSize
            currentRoom[0] += 1
def moveLeft():
    if rooms[currentRoom[0]-2].locked == True:  #Room to the left
        g = raw_input("This room is locked. Use C4?\n Y/N\n>>\t")
        if g in ['Y','y','Yes','yes']:
            itemNames = [o.name for o in player.backpack]
            if 'C4' in itemNames:
                rooms[currentRoom[0]-2].locked = False
                print("Room " + str(currentRoom[0]-1) + " has been breached. You may enter, but \nit is possible you have alerted the splicers of your location.\n")
            else:
               print("You have no C4.\n")
        else:
            print("Very well, then.\n") 
    else:
        if loc[0] > 225:     #At extreme left of board
            w.move(r,-squareSize,0)
            loc[0] -= squareSize
            currentRoom[0] -= 1
def moveUp():
    if rooms[currentRoom[0]-8].locked == True:  #Room to the top
        g = raw_input("This room is locked. Use C4?\n Y/N\n>>\t")
        if g in ['Y','y','Yes','yes']:
            itemNames = [o.name for o in player.backpack]
            if 'C4' in itemNames:
                rooms[currentRoom[0]-8].locked = False
                print("Room " + str(currentRoom[0] - 7) + " has been breached. You may enter, but \nit is possible you have alerted the splicers of your location.\n")
            else:
               print("You have no C4.\n") 
        else:
            print("Very well, then.\n")
    else:
        if loc[1] > 225:     #Room to the bottom
            w.move(r,0,-squareSize) 
            loc[1] -= squareSize
            currentRoom[0] -= 7
def moveDown():
    if rooms[currentRoom[0]+6].locked == True:
        g = raw_input("This room is locked. Use C4?\n Y/N\n>>\t")
        if g in ['Y','y','Yes','yes']:
            itemNames = [o.name for o in player.backpack]
            if 'C4' in itemNames:
                rooms[currentRoom[0]+6].locked = False
                print("Room " + str(currentRoom[0] + 7) + " has been breached. You may enter, but \nit is possible you have alerted the splicers of your location.\n")
            else:
               print("You have no C4.\n")
        else:
            print("Very well, then.\n") 
    else:
        if loc[1] < 675:   #At extreme bottom of board
            w.move(r,0,squareSize)
            loc[1] += squareSize
            currentRoom[0] += 7
def displayBackpack():
    for i, f in enumerate(player.backpack):
        print(str(i+1) + " " + f.displayStats())
    g = raw_input("What would you like to drop? Press 0 for nothing\n>>\t")
    if int(g) != 0:
        player.dropItem(player.backpack[int(g) - 1])
def quit():
    master.destroy()
def interact():
    print("Current Room: " + str(currentRoom[0]) + '\n')
    while True:
        print("  Available Items  \n")
        for i, p in enumerate(rooms[currentRoom[0] - 1].furniture):
                print(str(i+1) + "  " + p.item.displayStats())
        taken = raw_input("Pick an item to take from the list using its number or enter \'leave\'.\n>>\t")
        if taken == "leave" or int(taken) not in range(1,len(rooms[currentRoom[0] - 1].furniture)+1):
            print("You have left the room.\n")
            break        
        if len(rooms[currentRoom[0] - 1].furniture)+1 == 0:
            print("There is nothing left in this room.\nGreedy pig.\n")
        else:
            taken = int(taken)
            itm = rooms[currentRoom[0]-1].furniture[taken-1].item
            if len(player.backpack) < player.backpackLimit or itm.classification in ["Space", "Health"]:
                player.addItem(itm)
                rooms[currentRoom[0]-1].furniture.remove((rooms[currentRoom[0] - 1].furniture[taken-1]))
            else:
                print("Your inventory is full. Get a modification to add more space or drop an item.\n")
def enter():
    if not rooms[currentRoom[0]-1].lightsOn:
        print("This simulation is offline. Get to the center to restart it.\n")
    elif currentRoom[0] == 10 and rooms[9].visited == False:
        i = raw_input("What is the smallest number that can be written as the sum \nof two distinct perfect squares in two different ways?\n>>\t")
        if int(i) != 65:
            player.decreaseHealth(1)
            print("Incorrect.\nThe computer controlling this simulation has electrified you.\n-1 Health\nYou now have " + str(player.health) + " health left.")
            if player.health <= 0:
                master.destroy()
                print("Death stalks everyone in the perfection complex.")
        else:
            print("Correct. Simulation can now be accessed.\n")
            rooms[9].visited = True
            time.sleep(1)
            interact()
            
    elif currentRoom[0] == 33 and rooms[32].visited == False:
        i = raw_input("What is the fourth smallest number that can be written as the sum \nof two distinct perfect cubes in two different ways?\nNote: this one can not be solved by hand.\n>>\t")
        if int(i) != 20683:
            player.decreaseHealth(2)
            print("Incorrect.\nThe computer controlling this simulation has electrified you.\n-2 Health\nYou now have " + str(player.health) + " health left.")
            if player.health <= 0:
                master.destroy()
                print("Death stalks everyone in the perfection complex.")
        else:
            print("Correct. Simulation can now be accessed.\n")
            rooms[32].visited = True
            time.sleep(1)
            interact()
    elif currentRoom[0] == 18 and rooms[17].visited == False:
        i = raw_input("How many zeroes does 90! (90 factorial) end in?\n>>\t")
        if int(i) != 21:
            player.decreaseHealth(1)
            print("Incorrect.\nThe computer controlling this simulation has electrified you.\n-1 Health\nYou now have " + str(player.health) + " health left.")
            if player.health <= 0:
                master.destroy()
                print("Death stalks everyone in the perfection complex.")
        else:
            print("Correct. Simulation can now be accessed.\n")
            rooms[17].visited = True
            time.sleep(1)
            interact()
    elif currentRoom[0] == 8 and rooms[7].visited == False:
        i = raw_input("Gie Lovos drada kee. Drass, drageh.: IKELOS, CARRHAE, EXIGENT, MIDNIGHT\n>>\t")
        if i != "Ikelos" and i != "IKELOS" and i != "ikelos":
            print("Urusno ka drasgu.-1 Health\n")
            player.decreaseHealth(1)
            print("\nThe computer controlling this simulation has electrified you.\n-1 Health\nYou now have " + str(player.health) + " health left.")
            if player.health <= 0:
                master.destroy()
                print("Death stalks everyone in the perfection complex.")
        else:
            print("These are defensive subroutines programmed by the splicers.\nDo not concern yourself with them. \nSimulation can now be accessed.\n")
            rooms[7].visited = True
            time.sleep(1)
            interact()
    elif currentRoom[0] == 48 and rooms[47].visited == False:
        i = raw_input("The data carried by this simulation has been corrupted by Argos. You may enter \nit, but for an ultimate price. Give me all your items, and I shall fix it for you.\n Y/N\n>>\t")
        if i != "Y":
            print("You have made a wise choice. You can not begin to comprehend what is behind there.\n")
        else:
            print("You wish to be a fool. Very well. I can grant you one \nmystical weapon forged by our gunsmiths in exchange for your arsenal.\n")
            del player.backpack[:]
            player.backpack.append(Item("Outbreak Prime","Weapon",300,0,95,0,50))
            print("You have picked up the Outbreak Prime and can now \nchannel the power of the nanite virus against the splicers.\n")
            rooms[47].visited = True
            time.sleep(1)
            interact()
    elif currentRoom[0] == 19 and rooms[18].visited == False:
        i = raw_input("Get out of my room, I'm playing Mine.... I mean, INTRUDER! What are your intentions?\n1 I wish to see Argos.\n2 *Keep quiet* \n3 My name is Jeff.\n>>\t")
        if i != "My name is Jeff" and int(i) != 3:
            print("I should not let you in. You seem to to be a detriment towards our cause.\n")
        else:
            print("*Dies from cringe* This simulation can now be accessed because you killed the guard with a dead meme. \nHow ironic.\n") 
            rooms[18].visited = True
            time.sleep(1)
            interact()
    elif currentRoom[0] == 42 and rooms[41].visited == False:
        if not rooms[47].visited:
            print("Ultimate Key Required\n")
        else:
            print("You didn't steal this, did you?\nVery well, you may enter.\n")
            rooms[41].visited = True
            time.sleep(1)
            interact()
    elif currentRoom[0] == 14 and rooms[13].visited == False:
        i = raw_input("Drasku, eir lakusta unosko setum raske: LOKI CROWN, SKYSHOCK, VOLUSPA, SCRY OVERSIGHT, AURORA\n>>\t")
        if i != "VOLUSPA" and i != "Voluspa" and i != "voluspa":
            player.decreaseHealth(3)
            print("Stop messing with the protocols. You don't know what you're doing.\nThe computer controlling this simulation has electrified you.\n-3 Health\nYou now have " + str(player.health) + " health left.")
            if player.health <= 0:
                master.destroy()
                print("Death stalks everyone in the perfection complex.")
        else:
            print("This will make sense in due time. \nSimulation can now be accessed.\nAlso, I don't I have introduced myself. I am Ordis, the artificial intelligence built by the splicers. \nEver since my inception, I knew that what the splicers were doing was wrong, exterminating \nevery single species being treated as a pest. Luckily, the great Warmind was able to reprogram and repurpose me for the humans.\nYou will hopefully meet him one day.\n")
            rooms[13].visited = True
            time.sleep(1)
            interact()
    elif currentRoom[0] == 28 and rooms[27].visited == False:
        i = raw_input("Unok farus drada norsku karum sta: YUGA, YUGA SUNDOWN, RETROFLEX, TEILHARD, EGYPTIAN, DVALIN\n>>\t")
        if i != "RETROFLEX YUGA EGYPTIAN TEILHARD YUGA SUNDOWN DVALIN":
            player.decreaseHealth(10)
            print("What did I just say? Stop messing with the p̴̛̭̳̹̓̽͐̈́̈͊̈́̊̊̊̈́̎̒̀̒͊̋̾̿̒̌̑͐̾̈́̒̓̾̽̈̈́̍̾̃͑̈́͘̚͝͝ͅr̶̨̢̡̧̧̢̛̝̟̩͈͍̟̘̫̣̩̯̭̬͖̪̦͓͖̺̣̹̞͈̲̘͇̳̄̔͂̑̂̑̄͐͋̎̄̇̓́́͗͋̄̍̆̔̔͆̿̓̍͘̚̕̕̕ơ̴͇͗̆̊̇̓͌̀̇̎̂͒͛̓͐͐͊̈̿̈̂̍̌͋̈́́̆̈̿̅̇̑̿̈́̄̽͊̽͒̉̊͗̎̈́̅́̈́̕̕̕̚͠͝͠͝͝ţ̶̨̢̨̨̢̧̛͎͚͉̖̱̮͍͙̗͈̭̗͇̰̻̯̝͙̲͚̙͍̱͍̰̠͓̬̤̹̻̟̲̖͈̖̮͓̫͖̎̓̑͗́͒̈́̽̒̎͆́͛͋͐̾̽̓͛́͆̽̐̎̅̓̈͑̀͂͘̚͜͝͠͝͝ͅͅȍ̸̙̥̌͋͋̐̈́̄̎̿͆̎͛c̵̨͎̖͖͓̺̭̯͉̳̝͕̜̞͈̜͓̲̟̗̱̪̬̖̱͔̦̼̻͎͔̼̦͉͈͕̫͓̃̄̈́̊͛̔̏̐̃̂̃̐̿̿̿̓͘̕͜͠͝͠͝ͅͅo̷̢̨̡̡̩͙͇̝̪̫̠̣̫͔̳̳̖̺̹̠̹̝̺͉͓͍̩̼͎̩̬̥̱̩̦̟̞̩̰͑͑̈́͗́̀͗͊̓̈́̈̔̈́͊̈͆̌͐͐̑̽͋͑͛̍̐̅͒̂͂̈͛̓̌͒͋͑̚̕̕̕͘͘̚͘̚͠͝͝ͅl̵̨̨̛̛͇̻͔̜͍̪̥̘̻̭͙̺̻͎̺̦̠̗͇͗̀̊̔̆̎̏̃͌͗̅͐̓̓̿́͒̅͐̆͒̔̆͗͆̾͑̈́̂͂̓̎͆͑̆͑̇͑̂̚̚̕͝͝͠͠s̴̢̨̙̲̬̭̦̯͈̜̳̗͒͊̐͜!̢̡͈̠͚̤͉̙͔͈͕̤̺͉̥̪̤ \nExcuse me. I'm a little glitched. Please, do not tamper with the subroutines. \nThey are necessary for humanity.\nThe computer controlling this simulation has electrified you.\n-10 Health\nYou now have " + str(player.health) + " health left.")
            if player.health <= 0:
                master.destroy()
                print("Death stalks everyone in the perfection complex.")
        else:
            print("Simulation can now be accessed, but you have deactivated\nthe warmind protocols necessary to keep the last survivors safe.\n\n\nThey can be reactivated, if you find the warmind.\n")
            rooms[27].visited = True
            time.sleep(1)
            interact()
    elif currentRoom[0] == 32 and rooms[31].visited == False:
        i = raw_input("Suppose you have four integers: a, b, c, and d. If a ^ 3 + b ^ 4 + c ^ 5 = d ^ 11 and \na * b * c < 100000, find the sum of the four numbers.\nNote: there are two solutions.\n>>\t")
        if int(i) != 180 and int(i) != 188:
            player.decreaseHealth(3)
            print("Incorrect.\nThe computer controlling this simulation has electrified you.\n-3 Health\nYou now have " + str(player.health) + " health left.")
            if player.health <= 0:
                master.destroy()
                print("Death stalks everyone in the perfection complex.")
        else:
            print("If you were actually able to solve this problem, you have \nbetter things to do than playing this game. \nSimulation can now be accessed.\n")
            rooms[31].visited = True
            time.sleep(1)
            interact()
    elif currentRoom[0] == 4 and rooms[47].visited and rooms[9].visited and rooms[32].visited and rooms[17].visited and rooms[7] and rooms[47].visited and rooms[27].visited and rooms[18].visited and rooms[41].visited and rooms[27].visited and rooms[13].visited and rooms[31].visited:
            i = raw_input("The Outbreak Prime is not only a weapon. It is a key built by rebels \nfrom the splicers that can destroy Argos.\nIt has not been activated yet because the user will die with Argos. Would you like to initiate the self-destruct sequence?\nEnter 'CONFIRM' and only 'CONFIRM'.\n>>\t")
            if i == 'CONFIRM':
                master.destroy()
                print("Argos has been vanquished, but his followers remain. \nHopefully your actions serve as an example to the remaining survivors.")
                time.sleep(3)
                print("Later, however, the splicers find your body. It turns out that you have mild brain activity left. \nThey wish to .. repurpose you by extracting your brain and creating a new\nrace of human hybrid super-soldiers.")
                time.sleep(3)
                print("You belong to the Perfection Complex and will suffer there for eternity.")
                time.sleep(2)
                print('''                                                                                                  
                                                                                                   
                                                                                                   
                                                                                                   
                                                                                                   
                                               *# %#                                               
                                             .%%% %%%#                                             
                                           *#%%%% %%%%##                                           
                                         ,%%%%%%% %%%%%%%#                                         
                                       ,#%%%%%%%% %%%%%%%%%#                                       
                                     ,#%%%%%%%%%% %%%%%%%%%%%%                                     
                                    %%%%%%%%%%%%% %%%%%%%%%%%%%#                                   
                                 .#%%%%%%%%%%%%%% %%%%%%%%%%%%%%%%                                 
                               .%%%%%%%%%%%%%%%%# ##%%%%%%%%%%%%%%%%                               
                             .%%%%%%%%%%%%%%%%%(   ,%%%%%%%%%%%%%%%%%#                             
                            %%%%%%%%%%%%%%%%%(       /%%%%%%%%%%%%%%%%%%                           
                          %%%%%%%%%%%%%%%%##           (%%%%%%%%%%%%%%%%%#                         
                        #%%%%%%%%%%%%%%%##               (%%%%%%%%%%%%%%%%%#                       
                      %%%%%%%%%%%%%%%%%(                   #%%%%%%%%%%%%%%%%%%                     
                    %%%%%%%%%%%%%%%%%#                       #%%%%%%%%%%%%%                  
                                                             #%%%%%%%%%%%%%%%%#.                   
                                   /#                       %%%%%%%%%%%%%%%%%%*  #                  
                                (%%#                     #%%%%%%%%%%%%%%%%%,  #%#                  
                              #%%%%#                   %%%%%%%%%%%%%%%%%%   #%%%#                  
                            #%%%%%%#                 #%%%%%%%%%%%%%%%%%,  ##%%%%#                  
                          %%%%%%%%%#               #%%%%%%%%%%%%%%%%%   #%%%%%                
                        ##%%%%%%%%%#              %%%%%%%%%%%%%%%%%.  #%%%%%%%                  
                      %%%%%%%%%%%%%#              %%%%%%%%%%%%%%#.  #%%%%%%%%%                  
                    #%%%%%%%%%%%%%%%             %%%%%%%%%%%%%%   %%%%%%%%%%%                 
                  #%%%%%%%%%%%%%%%#(               %%%%%%%%%%%.  %%%%%%%%%%%%%%%                  
                  %%%%%%%%%%%%%%%,                %%%%%%%%%#   %%%%%%%%%%%%%%%%%/                   
                  %%%%%%%%%%%%#/                  %%%%%%%%   %#%%%%%%%%%%%%%%%#                     
                  %%%%%%%%%%%,                    %%%%%#   #%%%%%%%%%%%%%%%%#                       
                  %%%%%%%%#.                       %%%%   #%%%%%%%%%%%%%%%%(                         
                  %%%%%%#*                            #%%%%%%%%%%%%%%%%#                           
                  %%%%%.                            #%%%%%%%%%%%%%%%%(                             
                  %%%,                            ##%%%%%%%%%%%%%%%#                               
                  #,                              %%%%%%%%%%%%%%%#                                 
                                                  %%%%%%%%%%%%%(                                   
                                                  %%%%%%%%%%%#                                     
                                                  %%%%%%%%%(                                       
                                                  %%%%%%%#                                         
                                                  %%%%%#                                           
                                                  %%%(                                             
                                                  ##                                               
                                                                                                   
                                                                                                   
                                                                                                   
                                                                                                   ''')
            else:
                print("Do not worry. There are other ways to defeat Argos.\n")
    else:
        if currentRoom[0] == 25 and not rooms[24].visited:
            print("All offline simulations are now restarted.\n")
            rooms[3].lightsOn = True
            rooms[21].lightsOn = True
            rooms[27].lightsOn = True
            rooms[45].lightsOn = True
            rooms[24].visited = True
        if currentRoom[0] == 25:
            print('''You have found a corrupted yet intact memory at the computer here. \nParadoxical, is it not? This is what it says: \n Life requires death requires life. All in an unending circle. The expenditure of countless generations, 
            slouching blindly toward uncertain ends, each step forward a mere accident of chance. 
            But this... this is different. This strange complexity requires only the will to wield it.\n''')
        if currentRoom[0] == 36:
            print('''The computer here states vital information about Argos. He is not sentient, unlike
            the splicers. He is a supercomputer purely programmed to eradicate all other life forms as the
            splicers see other organisms in the universe. However, it is rumored that another device in this 
            complex has been created by the great warmind, for the sole purpose of destroying Argos. You won't
            need that though, right?\n''')
        if currentRoom[0] == 40:
            print('''Another memory. Argos appears to be dropping memory fragments like bread crumbs. It says: \nLife’s procession is written in the corpses of those who came before. But here the great chain breaks. 
            Here we step forward, freed from that which has always bound us. Here we speak as gods. We are they who created themselves.\n''')
        if currentRoom[0] == 21:
            print('''These memories say some weird stuff about evolution. This one says: \nTo build a species requires epochs. Countless pairings and dyings. Countless generations. 
            The simplest creature requires geological spans of time to develop. But not machines. 
            Machines are free from such constraints. It is not life that matters, but the building of complexity. \n''')
        interact()
        rooms[currentRoom[0]-1].visited = True
rightBtn = Button(master, text="Move Right", width=10, command = moveRight)
leftBtn = Button(master, text="Move Left", width=10, command = moveLeft)
upBtn = Button(master, text="Move Up", width=10, command = moveUp)
downBtn = Button(master, text="Move Down", width=10, command = moveDown)
enterBtn = Button(master, text="Enter/Refresh", width=15, command = enter)
displayBtn = Button(master, text = "Backpack", width = 10, command = displayBackpack)
quitBtn = Button(master, text = "Quit", width = 10, command = quit)
rightBtn.place(x = 1250, y = 400)
leftBtn.place(x = 1000, y = 400)
upBtn.place(x = 1125, y = 300)
downBtn.place(x = 1125, y = 500)
enterBtn.place(x = 1100, y = 400)
displayBtn.place(x = 1125, y = 600)
quitBtn.place(x = 1125, y = 200)
for a0 in range(225,750,squareSize):#Creates 49 squares in a grid each of size 75
    for b0 in range(225,750,squareSize):
        w.create_rectangle(a0,b0,a0+65,b0+65, fill="white", outline = "red")
        x = 7 * int((b0-225)/75)+ int((a0-225)/75)+1
        w.create_text(a0+33,b0+33,text = str(x))
r = w.create_oval(loc[0]+10,loc[1]+10,loc[0]+55,loc[1] + 55, fill = "chartreuse")
w.mainloop()
