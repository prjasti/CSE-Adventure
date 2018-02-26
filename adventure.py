'''
Description: This file initializes rooms with random weapons, their location, their locked and lightsOn state, and minimum item
requirements. It also initializes players, along with methods such as dropping and adding items, and the player's backpack, 
location, and health. It also gives possible values to each of the types of weapons and abilities in terms of damage, accuracy, 
and ammo. 
'''
import random
import time
#Note: C4 is just a key in this game, simulation offline is just equivalent of lights being out
#In this game weapons and abilities are emphasized the most
#WHen you press enter simulation a new grid showing the furniture in a room appears, and when player leaves the simulation the grid disappears
#and the original playing grid remains 
'''
Story: You are lost in the labyrinth known as the perfection complex in a remote
facility in Russia. Humanity has been exterminated by the splicers, a technologically advanced
alien species that wants to spread their nanite virus to colonize the entirety of the Milky Way Galaxy for themselves.
You are one of humanity's remaining survivors, but you are powerless, and the splicers are looking for you as you
are at the heart of the splicer operation on Earth. Move through rooms, collecting abilities, mods, and weapons, in order to defeat
enemies until you reach the exit, where the leader, Argos, will be waiting for you....
'''
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
    def useItem(self,item):         #Returns weapon used and damage it does and depletes ammo if it is a weapon
      if item.classification == "Weapon":
        item.ammo -= 1
      return [item.name,item.damage]
    def weapons_list(backpack):
        weapons_array = []
        for item in backpack:
            if item.classification == "Weapon":
                weapons_array.append(item)
        return weapons_array
    def ability_list(backpack):
        attributes_array = []
        for item in backpack:
            if item.classification == "Ability":
                attributes_array.append(item)
        return attributes_array
class Furniture:
    def __init__(self,item):
        self.item = item        #Item inside furniture
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
        text = self.name + '\n' + 'Type: ' + self.classification + '\n'
        if self.damage != 0:
          text += 'Damage: ' + str(self.damage) + '\n'
        if self.accuracy != 0 and self.accuracy != 100:
          text += 'Accuracy: ' + str(self.accuracy) + '\n'
        if self.health != 0:
          text += 'Health: ' + str(self.health) + '\n'
        if self.space != 0:
          text += 'Space: ' + str(self.space) + '\n'
        if self.ammo != 0:
          text += 'Ammo: ' + str(self.ammo) + '\n'
        return text
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
possibleItems = ['Automatic Rifle', 'Revolver', 'Shotgun', 'Fusion Accelerator', 'Linear Fusion Accelerator', 'Tracer Rifle', 'C4','Sniper Rifle','Health Boost','Inventory Mod','Solar Flare','Arc Discharge','Nanite Swarm','Void Slap'] #Randomly picked from when initializing furniture
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
player = User()
playerItems = []
rooms = []  #List to store rooms to assign to the grid
for a0 in range(1,49):     
  f = random.choice([1,2,3,4,5,6,7,8]) #Picks a random subset of the numbers 1 to 8
  a = Room(furniture = [])
  for i in range(f):
    furnitureItem = random.choice(possibleItems) #Picks random name from possibleItems
    if possibleClassification[furnitureItem] == 'Weapon':
      damage = random.choice(possibleDamage[furnitureItem])  #Picks possible damage from given weapon
      accuracy = random.choice(possibleAccuracy[furnitureItem]) #Picks possible accuracy from given weapon
      ammo = random.choice(possibleAmmo[furnitureItem]) #Picks possible ammo count from given weapon
      health = space = 0  #Assigns redundant variables as 0 
    elif possibleClassification[furnitureItem] == 'Ability': #Pretty much the same for the next four classifications
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
    a.furniture.append(Furniture(Item(furnitureItem,possibleClassification[furnitureItem],damage,health, accuracy,space,ammo)))  #Adds to list of furniture in the room
  a.number = a0   
  a.locked = True if a0 in [7,13,19,25,31,37,43] else False   #All rooms along the diagonal from bottom left to top right are locked
  a.lightsOn = False if a0 in [4,22,28,46] else True #All midpoints of the square of the grid are offline
  a.itemMin = 5 if a0 in [7,13,19,25,31,37,43] else 0   #All rooms along same diagonal have minimum item requirements
  rooms.append(a)
class Enemy:
  def __init__(self,attacks,health):
    self.attacks = attacks
    self.health = health
  def decHealth(self,dec):
    self.health -= dec
  def pickAttack(self):
    x = random.choice(self.attacks.keys())
    return [x,self.attacks[x]]
