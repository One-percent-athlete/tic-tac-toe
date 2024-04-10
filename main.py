# Define player and AI markers
PLAYER = 'X'
AI = 'O'

# Define the game board
board = [' ' for _ in range(9)]


# Function to display the game board
def display_board(board):
    for i in range(3):
        print('| ' + ' | '.join(board[i * 3:(i * 3) + 3]) + ' |')
        if i != 2:
            print('-' * 11)


# Function to check if a player has won
def is_winner(board, player):
    win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6))
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False


# Function to check if the board is full
def is_board_full(board):
    return ' ' not in board


# Function to get the player's move
def get_player_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        try:
            move = int(move) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")


# Minimax algorithm for AI
def minimax(board, player, depth):
    # Base cases
    if is_winner(board, AI):
        return 10
    elif is_winner(board, PLAYER):
        return -10
    elif is_board_full(board):
        return 0

    # Maximize for AI and minimize for opponent
    if player == AI:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = AI
                score = minimax(board, PLAYER, depth + 1)
                board[i] = ' '
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = PLAYER
                score = minimax(board, AI, depth + 1)
                board[i] = ' '
                best_score = min(best_score, score)
        return best_score


# Function to get the AI's move using minimax
def get_ai_move(board):
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = AI
            score = minimax(board, PLAYER, 0)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    return best_move


# Main game loop
def main():
    print("Welcome to Tic Tac Toe!")
    display_board(board)

    turn = PLAYER
    while True:
        # Player's turn
        if turn == PLAYER:
            move = get_player_move(board)
            board[move] = PLAYER
            display_board(board)

            if is_winner(board, PLAYER):
                print("You won!")
                break
            elif is_board_full(board):
                print("It's a tie!")
                break

            turn = AI

        # AI's turn
        else:
            move = get_ai_move(board)
            board[move] = AI
            print("AI's move:")
            display_board(board)

            if is_winner(board, AI):
                print("AI won!")
                break
            elif is_board_full(board):
                print("It's a tie!")
                break

            turn = PLAYER


if __name__ == "__main__":
    main()