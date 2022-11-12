def print_board(entries):
    line = "+---+---+---+"
    output = line
    n = 0
    for entry in entries:
        if n % 3 == 0:
            output = output + "\n| "
        else:
            output = output + " | "
        output = output + str(entry)
        if n % 3 == 2:
            output = output + " |\n"
            output = output + line
        n = n + 1
    print(output)
    print()

def game_over(board, space_num):
    print_board(board)
    print("GAME OVER")
    print(board[space_num], "has won")
    exit()

def is_row_winner(board, row_number):
    up_one = board[row_number] + 1
    up_two = board[row_number] + 2
    if board[row_number] == board[up_one] and board[up_one] == board[up_two]:
        return True
#notes
# index[0] : 1 : 1
# index[3] : 4 : 2
# index[6] : 7 : 3

def top_row_is_winner(board):
    if board[0] == board[1] and board[1] == board[2]:
        return True

    # if board[0] == board[1] and board[1] == board[2]:
    #     return True

def middle_row_is_winner(board):
    if board[3] == board[4] and board[4] == board[5]:
        return True

def bottom_row_is_winner(board):
    if board[6] == board[7] and board[7] == board[8]:
        return True

def left_column_is_winner(board):
    if board[0] == board[3] and board[3] == board[6]:
        return True

def middle_column_is_winner(board):
    if board[1] == board[4] and board[4] == board[7]:
        return True

def right_column_is_winner(board):
    if board[2] == board[5] and board[5] == board[8]:
        return True

def left_diagonal_is_winner(board):
    if board[0] == board[4] and board[4] == board[8]:
        return True

def right_diagonal_is_winner(board):
    if board[2] == board[4] and board[4] == board[6]:
        return True

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
current_player = "X"

for move_number in range(1, 10):
    print_board(board)
    response = input("Where would " + current_player + " like to move? ")
    space_number = int(response) - 1
    board[space_number] = current_player

    if is_row_winner(board, 0):
        game_over(board, 0)
    elif middle_row_is_winner(board):
        game_over(board, 3)
    elif bottom_row_is_winner(board):
        game_over(board, 6)
    elif left_column_is_winner(board):
        game_over(board, 0)
    elif middle_column_is_winner(board):
        game_over(board, 1)
    elif right_column_is_winner(board):
        game_over(board, 2)
    elif left_diagonal_is_winner(board):
        game_over(board, 0)
    elif right_diagonal_is_winner(board):
        game_over(board, 2)

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

print("It's a tie!")
