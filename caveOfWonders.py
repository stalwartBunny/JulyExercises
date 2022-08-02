#Text-based dungeon crawler
from sys import exit
import random

pcHP = 6
lightAttack = 2
heavyAttack = 4

class Mon:

    name = "Rabid Dog"
    HP = 4
    attack1 = "Bite"
    attack1Dmg = 1
    attack2 = "Chomp Chomp Chomp"
    attack2Dmg = 3

    def __init__(self, name, HP, attack1, attack1Dmg, attack2, attack2Dmg):
        self.name = name
        self.HP = HP
        self.attack1 = attack1
        self.attack1Dmg = attack1Dmg
        self.attack2 = attack2
        self.attack1Dmg = attack2Dmg

    def func(self):
        print("After calling the func method...")
        print(f"{self.name}'s HP is {self.HP}, {self.attack1} deals {self.attack1Dmg}, {self.attack2} deals {attack2Dmg}.")
        print("....function end....")

    #putridBeast = Mon("Putrid Beast", 4, "Swipe", 1, "Lunge", 2)
    #putridBeast.func()
    #print(putridBeast.HP)
def combat():
    seed = random.randint(1,11)
    seed2 = random.randint(1,11)
    pcHP = pcHP #work to do, make it recognize and pull pcHP from public variable
    lightAttack = lightAttack #work to do, make it recognize and pull pcHP from public variable
    heavyAttack = heavyAttack #work to do, make it recognize and pull pcHP from public variable


    if seed == 1:
        monster = Mon("Putrid Beast", 4, "Swipe", 1, "Lunge", 2)
    elif seed == 2:
        monster = Mon("Rabid Dog", 2, "Bite", 1, "Chomp Chomp Chomp", 3)
    elif seed == 3:
        monster = Mon("Church Servant", 7, "Cane Strike", 2, "Arcade Missile", 4)
    elif seed == 4:
        monster = Mon("Church Giant", 9, "Towering Slash", 4, "Stomp Stomp", 3)
    elif seed == 5:
        monster = Mon("Lab Rat", 3, "Nibble", 1, "Swarm", 3)
    elif seed == 6:
        monster = Mon("Mad One", 6, "Sickle Slash", 3, "Overhead Cleave", 5)
    elif seed == 7:
        monster = Mon("Maneater Boar", 8, "Ggreeeeeee!", 6, "*Snort Snort*", 0)
    elif seed == 8:
        monster = Mon("Gravekeeper Scorpion", 5, "Poisoned Pincers", 2, "Swarm", 4)
    elif seed == 9:
        monster = Mon("Keeper of the Old Lords", 6, "Sword Slash", 2, "Flame Spray", 5)
    elif seed == 10:
        monster = Mon("Hunter Mob", 7, "Axe Swing", 3, "Rifle Shot", 4)

    print(f"You look around for loot only to find a {monster}!")

    while monster.HP > 0 and pcHP > 0:
        print(f"The {monster} is readying to attack, what do you do?")
        combatChoice = input("Light attack, heavy attack, dodge, or escape >>>")
        randomRoll = random.randomint(1, 10)
        if randomRoll % 3 != 0:
            if combatChoice == "light attack" or combatChoice == "Light Attack" or combatChoice == "Light attack" or combatChoice == "light Attack":
                if seed2 % 2 == 0:
                    print(f"You exchange blows. The enemy used {monster.attack1}!")
                    monster.HP = monster.HP - lightAttack
                    pcHP = pcHP - monster.attack1Dmg
                elif seed2 % 2 != 0:
                    print(f"You exchange blows. The enemy used {monster.attack2}!")
                    monster.HP = monster.HP - lightAttack
                    pcHP = pcHP - monster.attack2Dmg
            elif combatChoice == "heavy attack" or combatChoice == "Heavy Attack" or combatChoice == "Heavy attack" or combatChoice == "heavy Attack":
                if seed2 % 2 == 0:
                    print(f"You exchange blows. The enemy used {monster.attack1}!")
                    pcHP = pcHP - monster.attack1Dmg
                    monster.HP = monster.HP - heavyAttack
                    pcHP = pcHP + 1
                elif seed2 % 2 != 0:
                    print(f"You exchange blows. The enemy used {monster.attack2}!")
                    pcHP = pcHP - monster.attack2Dmg
                    monster.HP = monster.HP - heavyAttack
                    pcHP = pcHP + 1
            elif combatChoice == "Dodge" or combatChoice == "dodge":
                if randomRoll % 2 == 0:
                    print(f"The blow missed!. You retaliate for big damage!")
                    monster.HP = monster.HP - heavyAttack
                    pcHP = pcHP + 1
                else:
                    if seed2 % 2 == 0:
                        print(f"You try to dodge and take half damage from {monster.attack1}.")
                        if monster.attack1 % 2 == 0:
                            pcHP = pcHP - (monster.attack1Dmg / 2)
                        else:
                            pcHP = pcHP - ((monster.attackDmg - 1) / 2)
                    else:
                        print(f"You try to dodge and take half damage from {monster.attack2}.")
                        if monster.attack1 % 2 == 0:
                            pcHP = pcHP - (monster.attack2Dmg / 2)
                        else:
                            pcHP = pcHP - ((monster.attackDmg - 1) / 2)
            elif combatChoice == "escape" or combatChoice == "Escape":
                print("You flee the way you came!")
                return(pcHP)
                pcMove(locationX, locationY)
            else:
                print("Invalid input, try again.")
    else:
        if combatChoice == "heavy attack" or combatChoice == "Heavy Attack" or combatChoice == "Heavy attack" or combatChoice == "heavy Attack":
            print("Your blow lands and their's misses!")
            monster.HP = monster.HP - heavyAttack
            pcHP = pcHP + 1
        elif combatChoice == "light attack" or combatChoice == "Light Attack" or combatChoice == "Light attack" or combatChoice == "light Attack":
            print("Your blow lands and their's misses!")
            monster.HP = monster.HP - lightAttack

    if pcHP == 0:
        print("Oh no! You died! That's the way the cookie crumbles.")
        exit(0)

    if monster.HP == 0:
        "You defeated the monster! Good for you! You take the loot and run!"
        pcMove(locationX, locationY)

    return(pcHP)

def pcMove(locationX, locationY):
    if locationX is 3:
        if locationY is 0:
            startRoom()
        elif locationY is 5:
            room35()
        elif locationY is 6:
            room36()
        elif locationY is 7:
            room37()
    elif locationX is 2:
        if locationY is 1:
            room21()
        elif locationY is 3:
            room23()
        elif locationY is 5:
            room25()
        elif locationY is 6:
            room26()
    elif locationX is 1:
        if locationY is 2:
            room12()
        elif locationY is 4:
            room14()
    elif locationX is 4:
        if locationY is 1:
            room41()
        elif locationY is 3:
            room43()
        elif locationY is 5:
            room45()
        elif locationY is 6:
            room46()
    elif locationX is 5:
        if locationY is 2:
            room52()
        elif locationY is 4:
            room54()
    else:
        print("You seem to have fallen off the map somehow. Let's go back to the beginning.")
        startRoom()


def startRoom():
    name = input("Please enter your name: ")
    print("Welcome to the Cave of Wonders. It's a wonder it exists at all!")
    print(f"We thank you, {name}, for coming here today. \n I'm sure inside you'll find your deepest desires.")
    locationX = 3
    locationY = 0
    choice = input("There is a door to your left and a door to your right. Which do you take?  >>>")
    if choice == "left" or choice == "Left":
        locationX = locationX - 1
        locationY = locationY + 1
#        return locationX, locationY
    elif choice == "right" or choice == "Right":
        locationX = locationX + 1
        locationY = locationY + 1
#        return locationX, locationY
    else:
        print("You chose neither, turned around, and walked out on this entire excercise.")
        exit(0)
    pcMove(locationX, locationY)

def room21():
    print("Welcome to room 21. You walked through a door, amazing. It has a north and west exit.")
    locationX = 2
    locationY = 1
    choice = input("Choose either forward or left: >>>")
    if choice == "Left" or choice == "left":
        locationX = locationX - 1
        locationY = locationY + 1
    elif choice == "forward" or choice == "Forward":
        locationY = locationY + 2
    else:
        print("You mumble to yourself incoherently and try that again...")

    pcMove(locationX, locationY)

def room41():
    print("Holy cows, you went right through a door and ended up in room 41. Astonishing. It has a north and east exit. ")
    locationX = 4
    locationY = 1
    choice = input("There is a door forward and a door right, choose one:  >>>")
    if choice == "forward" or choice == "Forward":
        locationY = locationY + 2
    elif choice == "right" or choice == "Right":
        locationX = locationX + 1
        locationY = locationY + 1
    else:
        print("You chose neither, turned around, and walked out on this entire excercise.")

    pcMove(locationX, locationY)

def room12():
    print("Welcome to room 12. It's a dead end, so you want to return the way you came with your loot but something is wrong...")
    combat()
    locationX = 2
    locationY = 1
    pcMove(locationX, locationY)

def room52():
    print("Welcome to room 52. It's a dead end, so you return the way you came with your loot.")
    locationX = 4
    locationY = 1
    pcMove(locationX, locationY)

def room23():
    print("Room 23 welcomes you. It exits to a hallway that breaks into three directions (all four, counting the way you came.)")
    locationX = 2
    locationY = 3
    choice = input("Left, right, forward, or back; which do you take?  >>>")
    if choice == "left" or choice == "Left":
        locationX = locationX - 1
        locationY = locationY + 1
    elif choice == "right" or choice == "Right":
        locationX = locationX + 2
    elif choice == "forward" or choice == "Forward":
        locationY = locationY + 2
    elif choice == "back" or choice == "Back":
        locationY = locationY - 2
    else:
        print("You chose neither, turned around, and walk back the way you came.")

    pcMove(locationX, locationY)

def room43():
    print("Room 43 welcomes you. It exits to a hallway that breaks into three directions (all four, counting the way you came.)")
    locationX = 4
    locationY = 3
    choice = input("Left, right, forward, or back; which do you take? >>>")
    if choice == "left" or choice == "Left":
        locationX = locationX - 2
        locationY = locationY + 0
    elif choice == "right" or choice == "Right":
        locationX = locationX + 1
        locationY = locationY + 1
    elif choice == "forward" or choice == "Forward":
        locationY = locationY + 2
    elif choice == "back" or choice == "Back":
        locationY = locationY - 2
    else:
        print("You have chosen an illegitimate move. Try again.")

    pcMove(locationX, locationY)


def room14():
    print("Room 14 is a dead end and you leave the way you came.")
    print(" ")
    locationX = 2
    locationY = 3
    pcMove(locationX, locationY)

def room54():
    print("Room 54 is a dead end and you leave the way you came.")
    print(" ")
    locationX = 4
    locationY = 3

    pcMove(locationX, locationY)

def room25():
    print("Room 25 has one exit northward. You go through it.")
    print(" ")
    locationX = 2
    locationY = 6

    pcMove(locationX, locationY)

def room45():
    print("Room 45 has one exit northward. You go through it.")
    print(" ")
    locationX = 4
    locationY = 6

    pcMove(locationX, locationY)

def room26():
    print("Room 26 leads to one room forward that looks peaceful and one spiral stairwell that leads to the tallest tower.")
    locationX = 2
    locationY = 6
    choice = input("??? >>>")
    if choice == "forward" or choice == "Forward":
        locationX = locationX + 1
        locationY = locationY + 1
    elif choice == "stairwell" or choice == "Stairwell":
        locationX = locationX + 1
    else:
        print("You have chosen an illegitimate move. Try again.")

    pcMove(locationX, locationY)

def room36():
    print("You arrive at the base of the tower, which also has a slide down to the start point.")
    choice = input("Tower or start? >>> ")
    locationX    = 3
    locationY = 6
    if choice == "Tower" or choice == "tower":
        locationY = locationY - 1
    else:
        print("You take the slip n slide back to the beginning!")
        startRoom()
    pcMove(locationX, locationY)
def room46():
    print("Room 46 leads to one room northward that looks peaceful and one spiral stairwell that leads to the tallest tower.")
    locationX = 4
    locationY = 6
    choice = input("??? >>>")
    if choice == "forward" or choice == "Forward":
        locationX = locationX -1
        locationY = locationY + 1
    elif choice == "stairwell" or choice == "Stairwell":
        locationX = locationX - 1
    else:
        print("You have chosen an illegitimate move. Try again.")


    pcMove(locationX, locationY)

def room37():
    print("Room 37 is a bedroom for servants that has gone unused for some time. Exits left and right.")
    locationX = 3
    locationY = 7
    choice = input("??? >>>")
    if choice == "left" or choice == "Left":
        locationX = locationX - 1
        locationY = locationY - 1
    elif choice == "right" or choice == "Right":
        locationX = locationX + 1
        locationY = locationY - 1
    else:
        print("You have chosen an illegitimate move. Try again.")

    pcMove(locationX, locationY)

def room35():
    print("Room 35 is the tower peak boss battle to purge the beast. You did it!")
    print("Thanks for playing!")
    exit(0)


startRoom()
