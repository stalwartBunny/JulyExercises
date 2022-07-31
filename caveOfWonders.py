#Text-based dungeon crawler
from sys import exit

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
            room23()
        elif locationY is 5:
            room25()
        elif locationY is 6:
            room26()
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
    if choice == "left" or "Left":
        locationX = locationX - 1
        locationY = locationY + 1
#        return locationX, locationY
    elif choice == "right" or "Right":
        locationX = locationX + 1
        locationY = locationY + 1
#        return locationX, locationY
    else:
        print("You chose neither, turned around, and walked out on this entire excercise.")
        exit(0)
    pcMove(locationX, locationY)

def room21():
    print("Welcome to room 21. You walked through a door, amazing.")

def room41():
    print("Holy cows, you went right through a door and ended up in room 41. Astonishing.")



startRoom()
