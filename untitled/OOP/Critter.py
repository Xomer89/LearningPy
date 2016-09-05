# A simple class presentaion

class Critter(object):
    """Virtual pet"""

    def __init__(self, name):
        print("A new pet created")
        self.name = name

    def __str__(self):
        rep = "Object from class Critter\n"
        rep += "Name: " + self.name + "\n"
        return rep

    def talk(self):
        print("Hey! I'm a pet from class Critter")


crit1 = Critter("Milo")
crit1.talk()
crit2 = Critter("Pluto")
crit2.talk()
print("Printing crit1: ")
print(crit1)
print("Access to crit1.name: ")
print(crit1.name)
input("\n\nPress ENTER to exit.")
