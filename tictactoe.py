from random import randrange

def display_board(board):
    print("+-------+-------+-------+")
    for row in range(3):
        print("|       |       |       |")
        print("|", end="")
        for col in range(3):
            cell = board[row][col]
            print(f"   {cell}   |", end="")
        print()
        print("|       |       |       |")
        print("+-------+-------+-------+")

def make_list(board):
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                free.append(board[row][col])
    return free

def enter_move(board):
    free = make_list(board)
    while True:
        try:
            move = int(input("Enter your move: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if move < 1 or move > 9:
            print("Invalid move. Must be between 1 and 9.")
        elif move not in free:
            print("That field is already occupied!")
        else:
            row = (move - 1) // 3
            col = (move - 1) % 3
            board[row][col] = 'O'
            break

def draw_move(board):
    free = make_list(board)
    if not free:
        return
    choice = free[randrange(len(free))]
    row = (choice - 1) // 3
    col = (choice - 1) % 3
    board[row][col] = 'X'

def victory_for(board, sign):
    # Check rows
    for row in range(3):
        if all(board[row][col] == sign for col in range(3)):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == sign for i in range(3)):
        return True
    if all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False

def main():
    board = [
        [1, 2, 3],
        [4, 'X', 6],
        [7, 8, 9]
    ]

    display_board(board)

    while True:
        # User's turn
        enter_move(board)
        display_board(board)

        if victory_for(board, 'O'):
            print("You won!")
            break
        if not make_list(board):
            print("It's a tie!")
            break

        # Computer's turn
        draw_move(board)
        display_board(board)

        if victory_for(board, 'X'):
            print("The computer won!")
            break
        if not make_list(board):
            print("It's a tie!")
            break

main()