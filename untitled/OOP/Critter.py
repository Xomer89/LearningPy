# Class presentation with private and open methods

class Critter(object):
    """Virtual pet"""

    total = 0
    @staticmethod
    def status():
        print("\nTotal amount of pets:", Critter.total)

    def __init__(self, name, mood):
        print("A new pet created")
        self.name = name #open attribute
        Critter.total += 1
        self.__mood = mood #closed attribute

    def __str__(self):
        rep = "Object from class Critter\n"
        rep += "Name: " + self.name + "\n"
        return rep

    def talk(self):
        print("\nHey! My name's", self.name)
        print("I feel", self.__mood, "\n")

    @staticmethod
    def __private_method():
        print("This is a private method\n")

    def public_method(self):
        print("This is an open method\n")
        self.__private_method()


print("Critter.total = ", end=" ")
print(Critter.total)

crit1 = Critter("Milo", ":-)")
crit1.talk()

crit2 = Critter("Pluto", ":-|")
crit2.talk()

print("Printing crit1: ")
print(crit1)

print("Access to crit1.name: ")
print(crit1.name)

Critter.status()
print("Critter.total = ", end=" ")

print(crit1.total)

crit1.public_method()

crit1._Critter__private_method() #A way to use private methods and variables
input("\n\nPress ENTER to exit.")
