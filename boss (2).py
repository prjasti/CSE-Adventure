from tkinter import *
from adventure import *
master = Tk()
root = Canvas(master, width=3000, height=2000)

boss = Enemy([], 800)

Label(master, text=("Your Health:" + player.health)).grid(row=1, column=0) #implements row 1 labels
Label(master, text=("Supreme Leader's Health" + boss.health)).grid(row=1, column=1)

# Create a Tkinter variable
tkvar = Item()

# Lists with options
weapons_options = player.weapons_list()
ability_options = player.ability_list()
attack_options = weapons_options + ability_options

#attack menu
attackMenu = OptionMenu(root, tkvar, attack_options[1], *attack_options)
Label(root, text="Choose a move").grid(row = 2, column = 1)
attackMenu.grid(row = 2, column =0)
tkvar.set('None') # set the default option

def boost_health():
    for i in range(0, len(player.backpack)):
        if player.backpack[i].classification == 'Health':
            del(player.backpack[i])
            player.health += random.randint(10, 21)
            break

#button to use health boost
Button(master, text="Health Boost", command= boost_health()).grid(row=3, column=1)

#commence turn once attack has been selected
if tkvar != "None":
    if tkvar.ammo > 0:
        if (random.randint(1, 101) < tkvar.accuracy):
            boss.health -= random.randint(possibleDamage[tkvar][0], possibleDamage[tkvar][-1])
            tkvar.ammo -= 1
    player.health -= random.randint(10, 30)

    Label(master, text=("Your Health:" + player.health)).grid(row=1, column=0)
    Label(master, text=("Boss' Health" + boss.health)).grid(row=1, column=1)

root.mainloop()