people = 20
cats = 30
dogs = 15

if people < cats:
    print(f"There's too many cats! {cats} is too many! The end is nigh!")

if people > cats :
    print(f"{people} people can handle {cats} cats. We'll be fine.")

if people < dogs:
    print("We will all drown in drool.")

if people > dogs:
    print(f"We outnumber the slobber monsters {people} to {dogs}.")

dogs += 5

if people >= dogs:
    print("We at least equal dogs in number.")

if people <= dogs:
    print("We are either at or beyond the puppy precipice.")

if people == dogs:
    print("People are dogs.")
