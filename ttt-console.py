board = [" " for _ in range(9)]

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_point(self):
        self.score += 1

    def display_score(self):
        print(f"{self.name}: {self.score} point(s)")

def welcome():
    print("Time for Tic Tac Toe!\n")
    print("Enter your move using the following integer positions:")
    print("0 | 1 | 2\n---------\n3 | 4 | 5\n---------\n6 | 7 | 8\n")

def print_board():
    print("Current Positions:")
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("-" * 9)
    print("")

def player_move(x_turn):
    try:
        if x_turn == True:
            print("Player X - Enter a position:")
            position = int(input())
            if (0 <= position < 9 and board[position] == ' '):
                board[position] = 'X'
                return False
            else:
                print("Invalid move. Try again.")
                return player_move(x_turn)
        else:
            print("Player O - Enter a position:")
            position = int(input())
            if (0 <= position < 9 and board[position] == ' '):
                board[position] = 'O'
                return True
            else:
                print("Invalid move. Try again.")
                return player_move(x_turn)
    except ValueError:
        print("You must enter an integer 0-8")
        return player_move(x_turn)

def check_win(num_moves):
    win_conditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combo in win_conditions:
        a, b, c = combo
        if board[a] == board[b] == board[c] and board[a] in ('X', 'O'):
            print_board()
            print(f"Player {board[a]} wins!")
            return True

    if num_moves > 8:
        print_board()
        print("It's a draw! Well played.")
        return True
    
    return False

def game_loop():
    game_over = False
    x_turn = True
    num_moves = 0
    while game_over == False:
        print_board()
        x_turn = player_move(x_turn)
        num_moves += 1
        game_over = check_win(num_moves)
        if (game_over == True):
            print("Enter any character to play again or 'q' to quit")
            if (input() == 'q'):
                print("Thanks for playing Tic Tac Toe!")
                break
            board[:] = [' '] * 9
            x_turn = True
            num_moves = 0
            game_over = False
            welcome()


welcome()
game_loop()