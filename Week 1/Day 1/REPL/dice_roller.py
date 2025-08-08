import random

dice_sides = int(input("Enter number of sides on the dice: "))
rolls = int(input("How many times to roll?: "))

for _ in range(rolls):
    print("You rolled:", random.randint(1, dice_sides))


