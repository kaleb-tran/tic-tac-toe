board = [" " for _ in range(9)]
saved_players = {}

class Player:
    def __init__(self, name):
        self.name = name
        self.x_score = 0
        self.o_score = 0

    def add_xpoint(self):
        self.x_score += 1

    def add_opoint(self):
        self.o_score += 1

    def display_score(self):
        print(f"{self.name}: {self.x_score + self.o_score} point(s)")
        print(f" {self.x_score} playing as X")
        print(f" {self.o_score} playing as O")

def welcome():
    print("Time for Tic Tac Toe!\n")

    print("Player X, Enter your username:")
    name = input()
    if name in saved_players:
        playerX = saved_players[name]
        print(f"Welcome, {playerX.name}")
    else:
        playerX = Player(name)
        saved_players[name] = playerX
    
    print("Player O, Enter your username:")
    name = input()
    if name in saved_players:
        playerO = saved_players[name]
        print(f"Welcome, {playerO.name}")
    else:
        playerO = Player(name)
        saved_players[name] = playerO
    
    print("Enter your move using the following integer positions:")
    print("0 | 1 | 2\n---------\n3 | 4 | 5\n---------\n6 | 7 | 8\n")
    return playerX, playerO

def print_board():
    print("Current Positions:")
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("-" * 9)
    print("")

def player_move(x_turn, playerX, playerO):
    try:
        if x_turn == True:
            print(f"{playerX.name} - Enter a position:")
            position = int(input())
            if (0 <= position < 9 and board[position] == ' '):
                board[position] = 'X'
                return False
            else:
                print("Invalid move. Try again.")
                return player_move(x_turn, playerX, playerO)
        else:
            print(f"{playerO.name} - Enter a position:")
            position = int(input())
            if (0 <= position < 9 and board[position] == ' '):
                board[position] = 'O'
                return True
            else:
                print("Invalid move. Try again.")
                return player_move(x_turn, playerX, playerO)
    except ValueError:
        print("You must enter an integer 0-8")
        return player_move(x_turn, playerX, playerO)

def check_win(num_moves, playerX, playerO):
    players = {'X': playerX, 'O': playerO}

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
            print(f"{players[board[a]].name} wins!")
            if board[a] == 'X':
                Player.add_xpoint(players[board[a]])
            else:
                Player.add_opoint(players[board[a]])
            Player.display_score(players[board[a]])
            return True

    if num_moves > 8:
        print_board()
        print("It's a draw! Well played.")
        return True
    
    return False

def game_loop(playerX, playerO):
    game_over = False
    x_turn = True
    num_moves = 0
    while game_over == False:
        print_board()
        x_turn = player_move(x_turn, playerX, playerO)
        num_moves += 1
        if num_moves > 4:
            game_over = check_win(num_moves, playerX, playerO)
        if (game_over == True):
            print("Enter any character to play again or 'q' to quit")
            if (input() == 'q'):
                print("Thanks for playing Tic Tac Toe!")
                break
            board[:] = [' '] * 9
            x_turn = True
            num_moves = 0
            game_over = False
            playerX, playerO = welcome()


game_loop(*welcome())