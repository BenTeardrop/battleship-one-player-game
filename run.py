import random


board = [('0') * 5 for x in range(5)]
computer_board = [('0') * 5 for x in range(5)]


def print_board(board):
    """
    Prints the board 5 x 5 coordinates
    and an horinzontal line 
    to separate the two boards
    """
    print ('---------')
    for row in board:
        print(" ".join(row))
    print ('---------')


def generate_random_coordinate():
    """
    Generates 2 random coordinates integers
    1 for row and 1 for column
    """
    row = random.randint(1,5)
    column = random.randint(1,5)
    return (row, column)




print('BATTLESHIP')
print_board(board)
print_board(computer_board)