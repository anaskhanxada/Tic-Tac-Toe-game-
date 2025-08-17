import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':  # Row
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':  # Column
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != ' ':  # Diagonal
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':  # Diagonal
        return board[0][2]

    return None

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def user_move(board):
    while True:
        try:
            move = int(input("Your move (1-9): ")) - 1
            if move < 0 or move >= 9:
                print("Invalid move. Choose 1-9.")
                continue
            row, col = divmod(move, 3)
            if board[row][col] == ' ':
                return row, col
            else:
                print("Spot taken. Try again.")
        except ValueError:
            print("Invalid input. Enter a number.")

def computer_move(board):
    empty_spots = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']
    return random.choice(empty_spots)

def main():
    board = [[' '] * 3 for _ in range(3)]
    print("Welcome to Easy Cross and Circle Showdown!\nYou are 'O'. Computer is 'X'.")

    # Computer's first move
    board[1][1] = 'X'
    print_board(board)

    while True:
        # User's turn
        row, col = user_move(board)
        board[row][col] = 'O'
        print_board(board)

        if winner := check_winner(board):
            print("You win!" if winner == 'O' else "Computer wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break

        # Computer's turn
        row, col = computer_move(board)
        board[row][col] = 'X'
        print("Computer's move:")
        print_board(board)

        if winner := check_winner(board):
            print("You win!" if winner == 'O' else "Computer wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()


# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.
largest_number = max(number1, number2, number3)
# Print the result.
print("The largest number is:", largest_number)

i = 0
while i <= 5 :
    i += 1
    if i % 2 == 0:
      break
    print("*")

var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print("#")

var = 1
while var < 10:
    print("#")
    var = var << 1