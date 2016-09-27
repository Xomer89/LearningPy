#Demonstrates how to import a module

import games, random

print("WELCOME TO THE EASIEST GAME\n")
again = None
while again != "n":
    players = []
    num = games.ask_number(question="How much players are taking part? (2-5): ", low=2, high=5)
    for i in range(num):
        name = input("Name player: ")
        score = random.randrange(100) + 1
        player = games.Player(name, score)
        players.append(player)
    print("Here are the results of the game: ")
    for player in players:
        print(player)
    again = games.ask_yes_no("\nWant to play again? (y/n): ")

input("\n\nPress ENTER ro exit")