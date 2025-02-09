def print_board(board):
    """
    Print the game board.
    
    :param board: a 3x3 2D list of strings representing the game board
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    """
    Check if the given player has won the game.
    
    :param board: a 3x3 2D list of strings representing the game board
    :param player: a string, either 'X' or 'O', representing the player
    :return: bool, True if the player has won, False otherwise
    """
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    # check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    """
    Check if the game board is full.
    
    :param board: a 3x3 2D list of strings representing the game board
    :return: bool, True if the board is full, False otherwise
    """
    return all(all(cell != ' ' for cell in row) for row in board)

def main():
    """
    The main function of the game.
    """
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    while True:
        # Display the current state of the board
        print_board(board)
        
        # Get the row and column input from the current player
        row = int(input(f"Player {current_player}, enter the row (0, 1, 2): "))
        col = int(input(f"Player {current_player}, enter the column (0, 1, 2): "))

        # Check if the chosen cell is already taken
        if board[row][col] != ' ':
            print("Cell already taken, try again.")
            continue
        
        # Place the player's mark on the board
        board[row][col] = current_player
        
        # Check if the current player has won the game
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check if the board is full, resulting in a tie
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # Switch to the other player
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
