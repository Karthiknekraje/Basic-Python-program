def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True

    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2-i] == player for i in range(3)]):
        return True

    return False

def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

def get_player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if 1 <= move <= 9:
                return (move - 1) // 3, (move - 1) % 3
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    board = [[" "]*3 for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    print("Welcome to Tic Tac Toe!")

    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn")
        row, col = get_player_move()

        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            else:
                turn += 1
        else:
            print("That cell is already taken. Please choose another one.")

if __name__ == "__main__":
    main()
