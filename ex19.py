def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheese.")
    print(f"You have {boxes_of_crackers} boxes of crackers.")
    print("That's enough for a party! \n")

print("We can feed the function direct values, like 20 and 30:")
cheese_and_crackers(20, 30)

print("Or we can use variables in our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can do math inside too!")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine both variables and math:")
cheese_and_crackers(amount_of_cheese * 5, amount_of_crackers / 2)
