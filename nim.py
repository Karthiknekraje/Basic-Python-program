import random

def display_sticks(sticks):
    print("Sticks remaining:", '| ' * sticks)

def player_turn(sticks):
    while True:
        display_sticks(sticks)
        max_remove = sticks // 2 if sticks % 2 == 0 else (sticks - 1) // 2  # Maximum sticks a player can remove
        remove = int(input(f"Select number of sticks to remove (1-{max_remove}): "))
        if 1 <= remove <= max_remove:
            return remove
        print("Invalid number of sticks. Please try again.")

def computer_turn(sticks):
    max_remove = max(1, sticks // 2 if sticks % 2 == 0 else (sticks - 1) // 2)  # Maximum sticks the computer can remove, ensuring it's at least 1
    remove = random.randint(1, max_remove)
    print(f"\nThe computer removes {remove} sticks.")
    return remove

def nim_game():
    sticks = random.randint(10, 30)  # Random initial number of sticks
    if sticks % 2 == 0:
        max_pick = sticks // 2
    else:
        max_pick = (sticks - 1) // 2
    print("Welcome to the game of Nim! You're playing with", sticks, "sticks.")
    player_turn_flag = True  # Flag to indicate player's turn
    while sticks > 0:
        if player_turn_flag:
            remove = player_turn(sticks)
        else:
            remove = computer_turn(sticks)
        sticks -= remove
        player_turn_flag = not player_turn_flag  # Switch turns
    # Determine the winner based on the last picker
    if player_turn_flag:
        print("\nCongratulations! You win!")
    else:
        print("\nSorry, you lost. Better luck next time!")

nim_game()
