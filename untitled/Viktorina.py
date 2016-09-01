import sys


def open_file(filename, mode):
    """Opens a file"""
    try:
        the_file = open(filename, mode)
    except IOError as e:
        print("Impossible to open file ", filename, ". The program will be shut down.\n", e)
        input("\n\nPress ENTER to exit.")
        sys.exit()
    else:
        return the_file


def next_line(the_file):
    """Returns formated line from the game file"""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line


def next_block(the_file):
    """Returns next block from game file"""
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    return category, question, answers, correct, explanation


def welcome(title):
    print("\t\tWelcome to Viktorina\n")
    print("\t\t", title, "\n")


def main():
    trivia_file = open_file("viktorina.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0
    """Extraction of the 1st block"""
    category, question, answers, correct, explanation = next_block(trivia_file)
    while category:
        """Printing question"""
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])
        """Getting the answer"""
        answer = input("Your answer is: ")
        """Checking answer"""
        if answer == correct:
            print("\nYes!", end=" ")
            print(explanation)
            score += 1
            print("Score: ", score, "\n\n")
        """Going to the next question"""
        category, question, answers, correct, explanation = next_block(trivia_file)
    trivia_file.close()
    print("That was the last question")
    print("Your score is ", score)


main()
input("\n\nPress ENTER to exit.")
