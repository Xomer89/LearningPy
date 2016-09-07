#A virtual pet to take care of

class Critter(object):
    """Virtual pet"""
    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "great"
        elif 5 <= unhappiness <= 10:
            m = "not bad"
        elif 11 <= unhappiness <= 15:
            m = "okay"
        else:
            m = "terrible"
        return m

    def talk(self):
        print("My name is", self.name, "and I feel", self.mood, "now.")
        self.__pass_time()

    def eat(self, food = 4):
        print("OM-NOM-NOM....Thanks")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Wiiiiiiii!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input("What will you call your pet?")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        #Menu
        print("""
        My Pet
        1 - Ask how it feels
        2 - Feed it
        3 - Play with it
        0 - Exit
        """)
        choice = input("Your choice")
        print()

        #Talk to pet
        if choice == "1":
            crit.talk()
        #Feed pet
        elif choice == "2":
            crit.eat()
        #Play with pet
        elif choice == "3":
            crit.play()
        #Exit
        elif choice == "0":
            print("Bye-bye")
        else:
            print("There's no option", choice)

main()
input("\n\nPress ENTER to exit.")

