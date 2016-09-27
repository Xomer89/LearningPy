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

class Deck(Hand):
    """Deck of playing cards"""
    def populate(self):
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("No more cards to give!")

#main

deck1 = Deck()
print("There's a new deck of cards.\nHere it is:")
print(deck1)

deck1.populate()
print("There are cards in the deck now.\nHere they are:")
print(deck1)

deck1.shuffle()
print("The cards were shuffled.\nHere they are now:")
print(deck1)

my_hand = Hand()
your_hand = Hand()
hands = [my_hand, your_hand]
deck1.deal(hands, per_hand=5)

print("\nWe both have 5 cards each.")
print("My cards are", my_hand)
print("Your cards are", your_hand)
print("These cards are still in the deck:")
print(deck1)

deck1.clear()
print("Deck dropped.")
print(deck1)

input("\n\nPress ENTER to exit.")