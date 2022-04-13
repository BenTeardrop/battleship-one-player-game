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

def players_choice():
    """
    player choice of row and column
    and making sure the player doesn't choose 
    a coordinate above 5 
    """
    global computer_board
    try:
        row_choice = int(input('Choose your row: '))
        column_choice = int(input('Choose your column: '))
        coordinates = row_choice, column_choice
        if row_choice and column_choice > 5:
            raise ValueError('stay below 5')
        print(f'your shot:{coordinates}')
        return coordinates
    except ValueError as e:
        print(e)
        return players_choice()


def computers_choice():
    """
    computers choice of coordinates to hit the players ship
    """
    global board
    comp_coordinates = generate_random_coordinate()
    print(f'comps Shot :{comp_coordinates}')
    return comp_coordinates


print('BATTLESHIP')
print_board(board)
print_board(computer_board)



players_choice()
computers_choice()