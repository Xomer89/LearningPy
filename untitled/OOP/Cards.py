# Cards

class Card(object):
    """One playing card"""
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Hand(object):
    """Hand - a number of cards for one player"""

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


#main part

card1 = Card(rank="A", suit="c")
print("Here's your card: ")
print(card1)

card2 = Card(rank="2", suit="c")
card3 = Card(rank="3", suit="c")
card4 = Card(rank="4", suit="c")
card5 = Card(rank="5", suit="c")

print("Printing another 4 cards: ")
print(card2)
print(card3)
print(card4)
print(card5)

my_hand = Hand()
print("Printing cards on hand before dealing: ")
print(my_hand)

my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)

print("Printing cards on hand after dealing: ")
print(my_hand)

your_hand = Hand()
my_hand.give(card1, your_hand)
my_hand.give(card2, your_hand)

print("\nI gave you two of my cards")
print("Now you have: ")
print(your_hand)
print("And I have: ")
print(my_hand)

my_hand.clear()
print("\nI dropped my cards and now I have: ")
print(my_hand)

input("\n\nPress ENTER to exit")


