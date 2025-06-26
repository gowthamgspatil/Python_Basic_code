import random

number = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1
    if guess == number:
        print(f"Correct! You guessed it in {attempts} tries.")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")
