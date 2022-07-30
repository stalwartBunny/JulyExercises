from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Well that's not too greedy. You win!")
        exit(0)
    else:
        dead("Greed is bad mmmkay. You die under all that gold, ")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can now go through it.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("This made the bear angry and it eats your head.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("This is an invalid action. (Action list: take honey, taunt bear, open door)")

def cthulu_room():
    print("Here you find the great and ominous Cthulu.")
    print("It stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well, that was tasty!")
    else:
        cthulu_room()

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
        print("You are in a dark room.")
        print("You see a green, green flame.")
        print("There are doors, one to your right and left.")
        print("Which do you take?")

        choice = input("> ")

        if choice == "left":
            bear_room()
        elif choice == "right":
            cthulu_room()
        else:
            dead("You stumble around until dead of starvation.")
start()
