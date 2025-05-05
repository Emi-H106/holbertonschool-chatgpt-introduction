def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    turn_count = 0

    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, 2) for player {player}: "))
        col = int(input(f"Enter column (0, 1, 2) for player {player}: "))
    except ValueError:
        print("Please enter a number.")
        continue

    if not (0 <= row <= 2 and 0 <= col <= 2):
        print(" Please enter a row and column between 0 and 2.")
        continue

    if board[row][col] != " ":
        print("That spot is already taken.")
        continue

    board[row][col] = player
    turn_count +=1

    if check_winner(board):
        print_board(board)
        print(f"Player {player} wins!")
        break
    elif turn_count == 9:
        print_board(board)
        print("It's a draw!")
        break

    player = "O" if player == "X" else "X"

tic_tac_toe()
