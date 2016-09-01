# This is a classic game "Hangman"

import random

#Constants
HANGMAN = (
    """
    |------|
    |      |
    |
    |
    |
    |
    |
    |___________
    """,
    """
    |------|
    |      |
    |      0  |
    |
    |
    |
    |
    |___________
    """,
    """
    |------|
    |      |
    |      0  |   -+-
    |
    |
    |
    |
    |___________
    """,
    """
    |------|
    |      |
    |      0  |   /-+-
    |
    |
    |
    |
    |___________
    """,
    """
    |------|
    |      |
    |      0  |   /-+-/
    |
    |
    |
    |
    |___________
    """,
    """
    |------|
    |      |
    |      0  |   /-+-/
    |      |
    |      |
    |
    |
    |___________
    """,
    """
    |------|
    |      |
    |      0  |   /-+-/
    |      |
    |      |
    |     |
    |     |
    |___________
    """,
    """
    |------|
    |      |
    |      0  |   /-+-/
    |      |
    |      |
    |     | |
    |     | |
    |___________
    """

)
WORDS = ("THERAPY", "BREAD", "CREATIVITY", "ROBOT")
MAX_WRONG = len(HANGMAN) - 1

#Variables
word = random.choice(WORDS)
so_far = "-" * len(word)
wrong = 0
used = []

#MAIN
print("Welcome to the game 'HANGMAN'! GOOD LUCK!")
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nThese are the letters you already tried:\n", used)
    print("\nYour word now looks like this:\n", so_far)
    guess = input("\n\nYour guess is:")
    guess = guess.upper()
    while guess in used:
        print("\nYou tried that letter before")
        guess = input("\n\nYour guess is:")
        guess = guess.upper()
    used.append(guess)
    if guess in word:
        print("\nYes, letter", guess, "is in this word!")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nSorry, there isn't a", guess)
        wrong += 1
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou're hanged :(")
else:
    print("Correct! The word was", so_far)
    input("\n\nPress ENTER for exit")

