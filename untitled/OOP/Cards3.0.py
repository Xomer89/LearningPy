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

class Unprintable_Card(Card):
    def __str__(self):
        return "<No printing>"

class Positionable_Card(Card):
    """Card which can be face up or down"""
    def __init__(self, rank, suit, face_up=True):
        super(Positionable_Card, self).__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super(Positionable_Card, self).__str__()
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up

#main

card1 = Card("A", "c")
card2 = Unprintable_Card("A", "d")
card3 = Positionable_Card("A", "h")

print("Object Card:", card1)

print("Object Unprintable_Card:", card2)

print("Object Positionable_Card:", card3)

print("Flipping the Positionable_Card")
card3.flip()
print("Object Positionable_Card:", card3)

input("\n\nPress ENTER to exit")
