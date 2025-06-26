import random

def Dash_dice():
    return random.randint(1, 6)

while True:
    input("Press Enter to roll the dice...")
    print("You rolled:", Dash_dice())
    if input("Roll again? (y/n): ") != 'y':
        break
    