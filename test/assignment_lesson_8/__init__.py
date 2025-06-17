get_user_parameters()

name = None
board_size = None
number_of_mines = None


def get_user_parameters():
    global name
    global board_size
    global number_of_mines

    # Get player name with validation loop
    while name is None:
        player_name_input = input("Hello, what's your name? ")

        if len(player_name_input.strip()) > 2:
            name = player_name_input.strip()
        else:
            print("Your name is too short (must be more than 2 characters)")

    # Get board size with validation loop
    while board_size is None:
        try:
            board_size_input = input(f"{name}, please choose board size (1-25): ")
            temp_board_size = int(board_size_input)

            if 0 < temp_board_size < 26:
                board_size = temp_board_size
            else:
                print(f"{name}, you have entered illegal board size. Please enter a number between 1 and 25.")
        except ValueError:
            print("Please enter a valid number.")

    # Get number of mines with validation loop
    while number_of_mines is None:
        try:
            max_mines_allowed = (board_size * board_size) // 2
            number_of_mines_input = input(
                f"{name}, for board size {board_size}x{board_size}, choose number of mines (1-{max_mines_allowed}): ")
            temp_number_of_mines = int(number_of_mines_input)

            if 0 < temp_number_of_mines <= max_mines_allowed:
                number_of_mines = temp_number_of_mines
            else:
                print(
                    f"{name}, you have entered illegal number of mines. Please enter a number between 1 and {max_mines_allowed}.")
        except ValueError:
            print("Please enter a valid number.")

    print(f"{name}, the board size is: {board_size}x{board_size}, number of mines is: {number_of_mines}. ENJOY!")


# Call the function
get_user_parameters()
