import random

words = ["python", "programming", "hangman", "developer", "code"]
word = random.choice(words)
guessed = ["_"] * len(word)
tries = 6

while tries > 0 and "_" in guessed:
    print("Word:", " ".join(guessed))
    guess = input("Guess a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        tries -= 1
        print(f"Wrong guess! {tries} tries left.")

if "_" not in guessed:
    print("You guessed it! Word was:", word)
else:
    print("Out of tries! Word was:", word)
