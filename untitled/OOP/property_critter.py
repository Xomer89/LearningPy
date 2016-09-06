#Classes with Properties

class Critter(object):
    """Virtual pet"""
    def __init__(self, name):
        print("A new pet is created")
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("A name of a pet cannot be an empty string\n")
        else:
            self.__name = new_name
            print("Name successfully changed to", self.__name)

    def talk(self):
        print("My name is", self.name)


crit = Critter("Milo")
crit.talk()
print("This pet's name is", crit.name)

crit.name = ""

print(crit.name)