#Demonstrates cooperation between objects

class Player(object):
    """The Player"""
    def blast(self, enemy):
        print("The Player shoots the enemy \n")
        enemy.die()

class Alien(object):
    """The evil Alien invader"""
    def die(self):
        print("The Alien shouts: '!!!NOOOOOOOOOOOOOOOOOO!!!'\n")

print("\t\tThe Death of the Alien\n")
hero = Player()
invader = Alien()
hero.blast(invader)

input("\n\nPress ENTER to exit")