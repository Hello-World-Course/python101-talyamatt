name = None
board_size = None
number_of_mines = None

def get_user_parameters():
    global  name
    global  board_size
    global  number_of_mines


    player_name_input = input("Hello, whats your name")

    if len(player_name_input) > 2:
        name = player_name_input
    else:
        print("Your name is too short")
        return

    board_size_input = input(f"{name}, please choose board size")

    temp_board_size = int(board_size_input)

    if 0 < temp_board_size < 26:
        board_size = temp_board_size
    else:
        print(f"{name}, you have entered illegal board size")
        return

    number_of_mines_input = input(f"{name}, for board size {board_size}, choose number of mines to allocate")

    temp_number_of_mines = int(number_of_mines_input)

    max_mines_allowed = (board_size * board_size) // 2

    if 0 < temp_number_of_mines <= max_mines_allowed:
        number_of_mines = temp_number_of_mines
    else:
        print(f"{name}, you have entered illegal number of mines")
        return

    if name is not None and board_size is not None and number_of_mines is not None:
        print(f"{name}, the board size is: {board_size}, number of mines is: {number_of_mines}. ENJOY!")


