# A simple class presentaion

class Critter(object):
    """Virtual pet"""

    def __init__(self):
        print("A new pet created")

    def talk(self):
        print("Hey! I'm a pet from class Critter")


crit1 = Critter()
crit2 = Critter()
crit1.talk()
crit2.talk()
input("\n\nPress ENTER to exit.")
