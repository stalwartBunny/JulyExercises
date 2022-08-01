#Text-based dungeon crawler
from sys import exit

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
    if choice == "Left" or choice == "Left":
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
    print("Welcome to room 12. It's a dead end, so you return the way you came with your loot.")
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
