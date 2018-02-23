import random
import time
#Note: C4 is just a key in this game, simulation offline is just equivalent of lights being out
#In this game weapons and abilities are emphasized the most
#WHen you press enter simulation a new grid showing the furniture in a room appears, and when player leaves the simulation the grid disappears
#and the original playing grid remains 
class Room: 
    def __init__(self,furniture=[],number=1,locked=False,lightsOn=True,itemMin=0):       #Initializes room attributes
        self.furniture = furniture   #List of Furniture objects in the Room
        self.number = number  #Number which indicates location on Tkinter Grid from 1 to 49
        self.locked = locked   #Indicates if the room is locked
        self.lightsOn = lightsOn   #Indicates if the room's lights are on
        self.itemMin = itemMin   #Number of items that are not keys required to enter room
    def unlock(self):
        self.locked = False      #Room is no longer locked    
    def turnOnLights(self):
        self.lightsOn = True     #Room can now be looted due to lights being on
class User:
    def __init__(self,backpack=[],location=Room(),health=10,backpackLimit=5):
        self.backpack = backpack #List of Item Objects in backpack
        self.location = location  #Room Object the User is in right now
        self.health = health   #Health of user
        self.backpackLimit = backpackLimit  #Maximum number of objects in backpack, can increase with inventory mods
    def addItem(self,item):
        '''
        Adds item if there is space in backpack. If the item is an inventory mod or health boost, it will 
        simply increase the amount of maximum space in backpack of increase player health, respectively. 
        '''
        if item.classification == 'Space':          #Adds backpack space and displays new limit
            self.backpackLimit += item.space
            print('Your inventory can now hold ' + str(self.backpackLimit) + ' items.')
        elif item.classification == 'Health':
            self.health += item.health
            print('You now have ' + str(self.health) + ' health.')
        elif len(self.backpack) < self.backpackLimit: #Number of current items is less than limit
            self.backpack.append(item)              #Adds item to backpack and displays confirmation
            print("You have picked up " + item.name)
        else:
            print("Your inventory is full. Get a modification to add more space or drop an item.")  #Backpack is full
    def dropItem(self,item):
        if len(self.backpack) == 0:     
            print("Your backpack is empty")
        elif item not in self.backpack:#Error if trying to drop a nonexistent item, will have dropdown menu so this cannot happen
            print("You do not have that item in your backpack.")
        else:
            self.backpack.remove(item)
            print("You have dropped " + item.name)  #Drop confirmation
    def forcedDrop(self,item):
        self.backpack.remove(item)
    def decreaseHealth(self,decrease):
        self.health -= decrease             #Decrease in user health
    def goToRoom(self,newRoom):
        if newRoom.locked == True:      #Room is locked
            print("This room is locked. Find a key in other rooms to unlock it.")
        elif len(self.backpack) < newRoom.itemMin:          #Not enough items in backpack
            print("You need more items to access this room. You are not prepared.")
            #Will implement the type of item restriction for this condition later
        else:
            self.location = newRoom
            print("You are now in Simulation " + str(newRoom.number))   #Changes location to new room and confirmation
    def displayBackpack(self):
        for b in self.backpack: #Displays backpack contents, will soon be in a dropdown menu
            print(b)
    def useItem(self,item):
      if item.classification == "Weapon":
        item.ammo -= 1
class Furniture:
    def __init__(self,item,gridLoc):
        self.item = item        #Item inside furniture
        self.gridLoc = gridLoc  #Location in the inner grid in the simulation (will it be 3 by 3 grid?)
    def removeItem(self):
        if self.item == None:   #Furniture is empty
            print('There is nothing in here. Either you have already looted\nit, or there was never anything to begin with.')
        else:
            self.item = None        #Furniture has become empty, confirmation
            print('The wreckage is now empty.')
    def displayItem(self):  #Displays what is in the furniture and its stats 
        print(self.item.name + '\n')
        self.item.displayStats()
class Item:
    def __init__(self,name,classification,damage,health,accuracy,space,ammo):
        self.name = name        #Name of item
        self.classification = classification #Type of item: weapons, defense, ability, key, or inventory mod
        self.damage = damage    #Damage of item, only applies to weapons, otherwise 0
        self.health = health    #Health of item, only applies to defense, otherwise 0
        self.accuracy = accuracy  #Probability an item hits its intended target times 100, between 0 and 100 for weapons, 100 for abilities, otherwise 0 
        self.space = space #Increment of backpack limit, only applies to inventory mod, otherwise 0
        self.ammo = ammo
    def displayStats(self):
        print(self.name)
        print('Type: ' + self.classification)
        if self.damage != 0:
          print('Damage: ' + str(self.damage))
        if self.accuracy != 0 and self.accuracy != 100:
          print('Accuracy: ' + str(self.accuracy))
        if self.health != 0:
          print('Health: ' + str(self.health))
        if self.space != 0:
          print('Space: ' + str(self.space))
        if self.ammo != 0:
          print('Ammo: ' + str(self.ammo))
        print('\n')
        #Displays each individual attribute except space and health, because those are not true items that can be picked up
        #Does not display redundant information, such as health of C4
possibleDamage = {  #Possible damage given a weapon or ability
  "Automatic Rifle":list(range(40,51)),
  "Revolver":list(range(70,111)),
  "Shotgun":list(range(100,131)),
  "Fusion Accelerator":list(range(90,141)),
  "Linear Fusion Accelerator": list(range(200,301)),
  "Tracer Rifle": list(range(80,101)),
  "Sniper Rifle": list(range(150,276)),
  "Solar Flare": list(range(90,121)),
  "Arc Discharge": list(range(130,171)),
  "Nanite Swarm": list(range(120,171)),
  "Void Slap": list(range(120,201))
}
possibleHealth = list(range(10,21)) #Possible health values in health boosts
possibleSpace = list(range(1,11)) #Possible space values in inventory mods
possibleAccuracy = {  #Possible values of accuracy given a weapon
  "Automatic Rifle": list(range(70,86)),
  "Revolver": list(range(50,71)),
  "Shotgun": list(range(70,86)),
  "Fusion Accelerator": list(range(70,86)),
  "Linear Fusion Accelerator": list(range(40,56)),
  "Tracer Rifle": list(range(60,91)),
  "Sniper Rifle": list(range(50,66))
}
possibleAmmo = {  #Possible amounts of ammo given a weapon
  "Automatic Rifle":list(range(10,16)),
  "Revolver":list(range(8,12)),
  "Shotgun":list(range(6,11)),
  "Fusion Accelerator":list(range(6,12)),
  "Linear Fusion Accelerator": list(range(4,9)),
  "Tracer Rifle": list(range(8,14)),
  "Sniper Rifle": list(range(5,10))
}
possibleItems = ['Automatic Rifle', 'Revolver', 'Shotgun', 'Fusion Accelerator', 'Linear Fusion Accelerator', 'Tracer Rifle', 'C4','Sniper Rifle','Health Boost','Inventory Mod','Solar Flare','Arc Discharge','Nanite Swarm','Void Slap','',''] #Randomly picked from when initializing furniture
possibleClassification = {  #Type of item given a certain item
  'Automatic Rifle': 'Weapon',
  'Tracer Rifle': 'Weapon',
  'Sniper Rifle': 'Weapon',
  'Revolver': 'Weapon',
  'Shotgun': 'Weapon',
  'Fusion Accelerator': 'Weapon',
  'Linear Fusion Accelerator': 'Weapon',
  'Solar Flare': 'Ability',
  'Arc Discharge': 'Ability',
  'Nanite Swarm': 'Ability',
  'Void Slap': 'Ability',
  'Health Boost': 'Health',
  'Inventory Mod': 'Space',
  'C4': 'C4',
  '':''
}
'''
This is just a test creation of the furniture in a room and will probably be
deleted or modified soon. 
'''
a = Room()
f = random.sample([1,2,3,4,5,6,7,8],random.choice([1,2,3,4,5,6,7,8]))
for i in f:
  furnitureItem = random.choice(possibleItems)
  if possibleClassification[furnitureItem] == 'Weapon':
    damage = random.choice(possibleDamage[furnitureItem])
    accuracy = random.choice(possibleAccuracy[furnitureItem])
    ammo = random.choice(possibleAmmo[furnitureItem])
    health = space = 0
  elif possibleClassification[furnitureItem] == 'Ability':
    damage = random.choice(possibleDamage[furnitureItem])
    accuracy = 100
    health = space = ammo = 0
  elif possibleClassification[furnitureItem] == 'Health':
    damage = accuracy = space = ammo = 0
    health = random.choice(possibleHealth)
  elif possibleClassification[furnitureItem] == 'Space':
    damage = accuracy = health = ammo = 0
    space = random.choice(possibleSpace)
  elif possibleClassification[furnitureItem] == 'C4':
    damage = accuracy = health = space = ammo = 0
  else:
    continue
  a.furniture.append(Furniture(Item(furnitureItem,possibleClassification[furnitureItem],damage,health, accuracy,space,ammo),i))
for o in a.furniture:
    o.item.displayStats()
class Enemy:
  def __init__(self,attacks,health):
    self.attacks = attacks
    self.health = health
  def decHealth(self,dec):
    self.health -= dec
  def pickAttack(self):
    x = random.choice(self.attacks.keys())
    return (x,self.attacks[x])
  def selfDestruct(self):
    if self.health < 20:
      print("NOOOOOO! YOU'LL NEVER WIN!")
      return ("Nanite Overload",1000000)
def startBoss():#This will be modified so that it can be printed on the Tkinter grid and formatted properly
  print("So it's true. There is indeed a human that intends to\ndestroy all that I have built.")
  print("What a shame, really. I could have put your....skills\nto good use. I could have made you a most prized lieutenant, despite you being a human.")
  print("However, I can assure you that our virus will cleanse all life\nhere in this solar system, and a new golden age will be brought\nabout. Even if it means that your newfound power goes to waste.")
  p = User()
  Argos = Enemy()
  turn = 1