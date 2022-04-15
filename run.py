import random


board = [["O"] * 5 for x in range(5)]
computer_board = [["O"] * 5 for x in range(5)]
your_ships_coords = []
computer_ships_coords = []


def print_board(board):
    """
    Prints the board 5 x 5 coordinates
    and an horinzontal line to separate the two boards
    """
    print("----------")
    for row in board:
        print(" ".join(row))
    print("----------")


def generate_random_coordinate():
    """
    Generates 2 random coordinates integers
    1 for row and 1 for column
    """
    row = random.randint(1, 5)
    column = random.randint(1, 5)
    return (row, column)


def players_choice():
    """
    player choice of row and column
    raise a ValueError if the number chosen is out of range
    """
    global computer_board
    try:
        row_choice = int(input('Choose your row: '))
        column_choice = int(input('Choose your column: '))
        coordinates = row_choice, column_choice
        if row_choice > 5 or column_choice > 5:
            raise ValueError('Choose a coordinate from 1 to 5')

        if has_already_been_hit(computer_board, coordinates):
            raise ValueError("Already Hit try another coordinate")
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
    if has_already_been_hit(board, comp_coordinates):
        return computers_choice()
    mark_board_with_hits(board, comp_coordinates)
    # print(f'comps Shot :{comp_coordinates}')
    return comp_coordinates


def generate_ship_coordinates():
    """
    Generates coordinates for players ships positions
    and avoid repetitions
    """
    coordinates_list = []
    while len(coordinates_list) < 5:
        ship_coordinates = generate_random_coordinate()
        if ship_coordinates not in coordinates_list:
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
        board[row-1][column-1] = '&'


def mark_board_with_hits(board, hit_coordinate):
    """
    marks players and computers board with hits with a "x"
    and if the players boat is hit turns into '*'
    """
    row, column = hit_coordinate
    if board[row-1][column-1] == '&':
        board[row-1][column-1] = '*'
    else:
        board[row-1][column-1] = 'x'


def has_already_been_hit(board, hit_coordinate):
    row, column = hit_coordinate
    if board[row-1][column-1] == 'x':
        return True
    return False


def restart_game():
    """
    Restarts the game
    """
    global board, computer_board, your_ships_coords, computer_ships_coords
    board = [["O"] * 5 for x in range(5)]
    computer_board = [["O"] * 5 for x in range(5)]
    your_ships_coords = []
    computer_ships_coords = []
    print('''
███████████████████████████████████████████████████████████████
█▄─▄─▀██▀▄─██─▄─▄─█─▄─▄─█▄─▄███▄─▄▄─█─▄▄▄▄█─█─█▄─▄█▄─▄▄─█─▄▄▄▄█
██─▄─▀██─▀─████─█████─████─██▀██─▄█▀█▄▄▄▄─█─▄─██─███─▄▄▄█▄▄▄▄─█
▀▄▄▄▄▀▀▄▄▀▄▄▀▀▄▄▄▀▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▀▄▀▄▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀

rules:

- Choose coordinate from 1 to 5 to hit your
  opponents ships.
- The first to hit the 5 ships wins.
- Your board is the top one
- The computers board is at the bottom
- Your ships are marked with an '&'
- Hits are marked win an 'x'
    ''')
    computer_ships_coords = generate_ship_coordinates()
    # print(f'Printing comp ship coords: {computer_ships_coords}')
    your_ships_coords = generate_ship_coordinates()
    # print(f'Printing my ship coords: {your_ships_coords}')
    mark_board_with_ship_coordinates(your_ships_coords)
    print_board(board)
    print_board(computer_board)
    start_game()


def ask_to_play_again():
    """
    Asks the player at the end of the game if they want to
    play again or quit the game completely
    """
    answer = input('Do you want to play another game y/n? ')
    if answer == "y":
        restart_game()
    elif answer == "n":
        print('''
██████╗░███████╗░█████╗░░█████╗░███████╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝
██████╔╝█████╗░░███████║██║░░╚═╝█████╗░░
██╔═══╝░██╔══╝░░██╔══██║██║░░██╗██╔══╝░░
██║░░░░░███████╗██║░░██║╚█████╔╝███████╗
╚═╝░░░░░╚══════╝╚═╝░░╚═╝░╚════╝░╚══════╝
''')
    else:
        ask_to_play_again()


def start_game():
    """
    Starts the game between the player and the computer
    keep the game going until 5 ships have been hit
    """

    global computer_ships_coords
    global your_ships_coords
    your_score = 0
    comp_score = 0
    while your_score < 5 and comp_score < 5:
        players_shot = players_choice()
        computer_shot = computers_choice()
        # row, column = hit_coordinate

        # Checks for player
        if players_shot in computer_ships_coords:
            your_score += 1
            print("Computer Ship Down!")
        elif players_shot not in computer_ships_coords:
            print("You missed!")
        # Checks for computer
        if computer_shot in your_ships_coords:
            comp_score += 1
            print("Your Ship Down!")
        elif computer_shot not in your_ships_coords:
            print("Players Ship missed!")
        print_board(board)
        print_board(computer_board)
        print(f'Your score:{your_score}')
        print(f'Comp score:{comp_score}')

        if your_score == 5:
            print('''
██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗██╗███╗░░██╗██╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██║████╗░██║██║
░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║██╔██╗██║██║
░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║██║╚████║╚═╝
░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░██║██║░╚███║██╗
░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝
            ''')
        elif comp_score == 5:
            print('''
█▀▀ █▀█ █▀▄▀█ █▀█ █░█ ▀█▀ █▀▀ █▀█   █░█░█ █ █▄░█ █▀
█▄▄ █▄█ █░▀░█ █▀▀ █▄█ ░█░ ██▄ █▀▄   ▀▄▀▄▀ █ █░▀█ ▄█
            ''')
    ask_to_play_again()


def main():
    """
    Main functions
    """
    global computer_ships_coords, your_ships_coords
    print('''
███████████████████████████████████████████████████████████████
█▄─▄─▀██▀▄─██─▄─▄─█─▄─▄─█▄─▄███▄─▄▄─█─▄▄▄▄█─█─█▄─▄█▄─▄▄─█─▄▄▄▄█
██─▄─▀██─▀─████─█████─████─██▀██─▄█▀█▄▄▄▄─█─▄─██─███─▄▄▄█▄▄▄▄─█
▀▄▄▄▄▀▀▄▄▀▄▄▀▀▄▄▄▀▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▀▄▀▄▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀

rules:

- Choose coordinate from 1 to 5 to hit your
  opponents ships.
- The first to hit the 5 ships wins.
- Your board is the top one
- Your ships are marked with an '&'
- The computers board is at the bottom
- Hits are marked win an 'x'
    ''')
    computer_ships_coords = generate_ship_coordinates()
    print(f'Printing comp ship coords: {computer_ships_coords}')
    your_ships_coords = generate_ship_coordinates()
    print(f'Printing my ship coords: {your_ships_coords}')
    mark_board_with_ship_coordinates(your_ships_coords)
    print_board(board)
    print_board(computer_board)
    start_game()


main()
