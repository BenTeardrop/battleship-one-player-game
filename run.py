import random


board = [["O"] * 5 for x in range(5)]
computer_board = [["O"] * 5 for x in range(5)]
your_ships_coords = []
computer_ships_coords = []

def print_board(board):
    """
    Prints the board 5 x 5 coordinates
    and an horinzontal line 
    to separate the two boards
    """
    print("----------")
    for row in board:
        print(" ".join(row))

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

    """
    global computer_board
    try:
        row_choice = int(input('Choose your row: '))
        column_choice = int(input('Choose your column: '))
        coordinates = row_choice, column_choice
        if row_choice and column_choice > 5:
            raise ValueError('stay below 5')
        # print(f'your shot:{coordinates}')
        mark_board_with_hits(computer_board, coordinates)
        return coordinates
    except ValueError as e:
        print(e)
        return players_choice()

def computers_choice():
    """
    computers choice of coordinates to hit the boat
    """
    global board
    comp_coordinates = generate_random_coordinate()
    mark_board_with_hits(board, comp_coordinates)
    # print(f'comps Shot :{comp_coordinates}')
    return comp_coordinates

def generate_ship_coordinates():
    """
    Generates coordinates for players ships postions
    """
    coordinates_list = []
    for x in range(0,5):
        ship_coordinates = generate_random_coordinate()
        coordinates_list.append(ship_coordinates)
    # print(f'Ship coordinates: {coordinates_list}')
    return coordinates_list


def mark_board_with_ship_coordinates(coordinates_list):
    """
    marks the board with @ where the players
    coordinates are.
    """
    global board
    for coordinate in coordinates_list:
        row, column = coordinate
        board[row-1][column-1] = '@'


def mark_board_with_hits(board, hit_coordinate):
    """
    marks players board with computers hits
    """
    row, column = hit_coordinate

    board[row-1][column-1] = 'x'

def start_game():
    """
    Starts the game between the player and the computer
    """

    global computer_ships_coords
    global your_ships_coords
    your_score = 0
    comp_score = 0
    while your_score < 5 or comp_score < 5:
        players_shot = players_choice()
        computer_shot = computers_choice()


        # Checks for player
        if players_shot in computer_ships_coords:
            your_score += 1

            print("Computer Ship Down!")
        elif players_shot not in computer_ships_coords:
            print("You miss!")
        elif your_score == 5 :
            print('You Win!')

         # Checks for computer
        if computer_shot in your_ships_coords:
            comp_score += 1
            print("Your Ship Down!")
        elif computer_shot not in your_ships_coords:
            print("Comp miss!")
        elif comp_score == 5 :
            print('Comp Win!')

        print_board(board)
        print_board(computer_board)
        print(f'Your score:{your_score}')
        print(f'Comp score:{comp_score}')



def main():
    """
    Main functions
    """
    global computer_ships_coords, your_ships_coords
    print('BATTLESHIP\nrules: choose coordinate from 1 to 5 to hit you oponent\n the first to hit the 5 ships wins')
    # print('Printing comp ship coords')
    computer_ships_coords = generate_ship_coordinates()
    # print('Printing my ship coords')
    your_ships_coords = generate_ship_coordinates()
    mark_board_with_ship_coordinates(your_ships_coords)
    print_board(board)
    print_board(computer_board)
    start_game()


main()