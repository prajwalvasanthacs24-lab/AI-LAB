import math

HUMAN = 'X'
AI = 'O'
EMPTY = ' '

def print_board(board):
    print("\n")
    for i, row in enumerate(board):
        print(" " + " | ".join(row) + " ")
        if i < 2:
            print("---+---+---")
    print("\n")

def is_moves_left(board):
    for row in board:
        if EMPTY in row:
            return True
    return False

def evaluate(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return 10 if board[i][0] == AI else -10
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return 10 if board[0][i] == AI else -10

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return 10 if board[0][0] == AI else -10
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return 10 if board[0][2] == AI else -10

    return 0

def minimax(board, depth, is_max):
    score = evaluate(board)

    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = EMPTY
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = EMPTY
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                move_val = minimax(board, 0, False)
                board[i][j] = EMPTY

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    print("--- Tic-Tac-Toe AI (Minimax Algorithm) ---")
    print("Grid locations: 1-9 (Row-wise)")
    
    positions = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2)
    }

    print_board(board)

    while is_moves_left(board) and evaluate(board) == 0:
        try:
            move = int(input("Enter position (1-9) for 'X': "))
            if move not in positions:
                print("Invalid input! Choose between 1 and 9.")
                continue
            r, c = positions[move]
            if board[r][c] != EMPTY:
                print("Cell already occupied! Pick another.")
                continue
            board[r][c] = HUMAN
        except ValueError:
            print("Please enter a valid integer.")
            continue

        print_board(board)

        if evaluate(board) != 0 or not is_moves_left(board):
            break

        print("AI ('O') is thinking...")
        ai_row, ai_col = find_best_move(board)
        board[ai_row][ai_col] = AI
        print_board(board)

    final_score = evaluate(board)
    if final_score == 10:
        print("AI Wins!")
    elif final_score == -10:
        print("You Win!")
    else:
        print("It's a Draw!")

if __name__ == "__main__":
    play_game()
