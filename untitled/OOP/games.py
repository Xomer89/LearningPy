#Games
#Demonstrates creation of a module

class Player(object):
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep

def ask_yes_no(question):
    """Ask a question with a yes/no answer"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Asks to input number form a specific range"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

if __name__ == "__main__":
    print("You run the direct module, you didn't import it")
    input("\n\nPress ENTER to exit.")
