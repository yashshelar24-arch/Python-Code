import math

# Print the board
def print_board(board):
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")
    print()

# Check winner
def check_winner(board):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for combo in win_combos:
        if (board[combo[0]] == board[combo[1]] ==
                board[combo[2]] != " "):
            return board[combo[0]]

    if " " not in board:
        return "Draw"

    return None

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)

    if winner == "X":
        return -1
    elif winner == "O":
        return 1
    elif winner == "Draw":
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)

        return best_score


# Find the best move for AI
def best_move(board):
    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move

# Main game loop
def play_game():
    board = [" "] * 9

    print("You are X. Computer is O.")
    print("Positions are numbered from 0 to 8.")
    print_board(board)

    while True:
        # Player move
        try:
            move = int(input("Enter your move (0-8): "))

            if move < 0 or move > 8:
                print("Invalid position. Enter a number from 0 to 8.")
                continue

            if board[move] != " ":
                print("Invalid move. Try again.")
                continue

            board[move] = "X"

        except ValueError:
            print("Please enter a valid number.")
            continue

        print_board(board)

        winner = check_winner(board)

        if winner is not None:
            break

        # Computer move
        ai_move = best_move(board)
        board[ai_move] = "O"

        print("Computer places O at position", ai_move)
        print_board(board)

        winner = check_winner(board)

        if winner is not None:
            break

    # Display result
    if winner == "Draw":
        print("It's a Draw!")
    else:
        print("Winner is:", winner)

# Run the game
play_game()
