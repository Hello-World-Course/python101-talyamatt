name = input("Hello, whats your name\ninput:>")
board_size_str = input( f"{name}, please choose board size\ninput:>")
board_size = int(board_size_str)
number_of_mines_str = input( f"{name}, for board size {board_size}, choose number of mines to allocate\ninput:>" )
number_of_mines = int(number_of_mines_str)
print(f"{name}, the board size is: {board_size}, number of mines is: {number_of_mines}. ENJOY!")



