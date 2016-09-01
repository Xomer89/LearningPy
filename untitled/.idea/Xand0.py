#Krestiki-Noliki

#GLOBAL CONSTANTS
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

#FUNCTIONS
def instr():
    """Displays instructions to user"""
    print(
        """
        Чтобы сделать ход. введи число от О до 8.  Числа однозначно соответствуют полям
        доски - так. как показано ниже:
            0 | 1 | 2
            3 | 4 | 5
            6 | 7 | 8
        \n
        """
    )

def ask_yes_no(question):
    """Asks a yes\no question"""
    response = None
    while response not in ("y","n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Asks to input number from a range"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def pieces():
    """Defines who'll go first"""
    go_first = ask_yes_no("Want to go first (y/n):")
    if go_first == "y":
        print("OK, you start, use X")
        human = X
        comp = O
    else:
        print("OK, I'll start, use O")
        human = O
        comp = X
    return human, comp

def new_board():
    """Creates a new board for the game"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """Displays the board"""
    print("\n\t", board[0], "|", board[1],"|", board[2])
    print("\t", "---------------------------------------")
    print("\t", board[3], "|", board[4],"|", board[5])
    print("\t", "---------------------------------------")
    print("\t", board[6], "|", board[7],"|", board[8], "\n")

def legal_moves(board):
    """Creates a list of legal moves"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
        return moves

def winner(board):
    """Defines the winner of the game"""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None

def human_move(board, human):
    """Gets the move of a human player"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Your move pick a field (0-8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nThat field is already taken. Pick another one.")
    print("Okay..")
    return move

def comp_move(board, comp, human):
    """Makes moves for the computer player"""
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("I'll pick", end=" ")
    for move in legal_moves(board):
        board[move] = comp
        if winner(board) == comp:
            print(move)
            return move
        board[move] = EMPTY

    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY

    for move in BEST_MOVES:
        for move in legal_moves(board):
            print(move)
            return move

def next_turn(turn):
    '''Who's turn is next X or O'''
    if turn == X:
        return O
    else:
        return X

def congrat_winner(the_winner, comp, human):
    '''Defines the winner and congratulates him'''
    if the_winner != TIE:
        print("Three", the_winner,"in a row!\n")
    else:
        print("It's a tie!\n")
    if the_winner == comp:
        print("I WON!")
    elif the_winner == human:
        print("You WON!")
    elif the_winner == TIE:
        print("We're both Krossav4egi ;)")

def main():
    instr()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = comp_move(board, comp, human)
            board[move] = comp
        display_board(board)
        turn = next_turn(turn)
        the_winner = winner(board)
        congrat_winner(the_winner, comp, human)

main()
inрut("\n\nPress Enterto exit")



