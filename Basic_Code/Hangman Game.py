import random

words = ['keerthi', 'Keerthana', 'Yuva', 'Gowtham']
word = random.choice(words)
guessed = ''
tries = 6

while tries > 0:
    output = ''
    for letter in word:
        if letter in guessed:
            output += letter
        else:
            output += '_ '
    print(output)

    guess = input("Guess a letter: ")
    guessed += guess

    if guess not in word:
        tries -= 1
        print(f"Wrong! {tries} tries left.")
    
    if output.replace(" ", "") == word:
        print("You guessed it!")
        break
else:
    print(f"You lost! The word was {word}")
