import random

# initialization of tic-tac-toe board and dictionary of players
board = [" " for _ in range(9)]
saved_players = {}

# player object for tracking names and points
class Player:
    def __init__(self, name):
        self.name = name
        self.x_score = 0
        self.o_score = 0

    def add_xpoint(self):
        self.x_score += 1

    def add_opoint(self):
        self.o_score += 1

    def get_tscore(self):
        return self.x_score + self.o_score

    def display_score(self):
        print(f"{self.name}: {self.x_score + self.o_score} point(s)")
        print(f" {self.x_score} point(s) playing as X")
        print(f" {self.o_score} point(s) playing as O")

# prints the current game board using for loop
def print_board():
    print("Current Positions:")
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("-" * 9)
    print("")

# prompts a move from the user
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

# checks to see if a player has won or if the board has been filled
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

# prompts player setup for user vs user
def prompt_1v1():
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

    return playerX, playerO

# runs a user vs user game
def game_1v1(playerX, playerO):
    game_over = False
    x_turn = True
    num_moves = 0
    while game_over == False:
        x_turn = player_move(x_turn, playerX, playerO)
        num_moves += 1
        if num_moves > 4:
            game_over = check_win(num_moves, playerX, playerO)
            if game_over == True:
                board[:] = [' '] * 9
                input("Enter any character to continue: ")
                break
        print_board()

# calculates CPU move
def cpu_move(userX):
    while True:
        random_int = random.randint(0, 8)
        if userX == False:
            if (0 <= random_int < 9 and board[random_int] == ' '):
                board[random_int] = 'X'
                print(f"CPU places an 'X' at position {random_int}")
                return False
            else:
                return cpu_move(userX)
        else:
            if (0 <= random_int < 9 and board[random_int] == ' '):
                board[random_int] = 'O'
                print(f"CPU places an 'O' at position {random_int}")
                return True
            else:
                return cpu_move(userX)

# runs a user vs cpu game
def game_cpu():
    # setup CPU
    if "CPU" not in saved_players:
        saved_players["CPU"] = Player("CPU")
    
    print("Enter your username:")
    name = input()
    while True:
        # prompt player setup if user has already played
        if name in saved_players:
            print(f"Welcome, {name}")
            choice = input("Enter 'X' or 'O' to play as X or O: ")
            match choice:
                case "X":
                    playerX = saved_players[name]
                    playerO = saved_players["CPU"]
                    userX = True
                    break
                case "O":
                    playerO = saved_players[name]
                    playerX = saved_players["CPU"]
                    userX = False
                    break
                case _:
                    print("Invalid option, try again.")
        # prompt player setup for new user
        else:
            choice = input("Enter 'X' or 'O' to play as X or O: ")
            match choice:
                case "X":
                    playerX = Player(name)
                    saved_players[name] = playerX
                    playerO = saved_players["CPU"]
                    userX = True
                    break
                case "O":
                    playerO = Player(name)
                    saved_players[name] = playerO
                    playerX = saved_players["CPU"]
                    userX = False
                    break
                case _:
                    print("Invalid option, try again.")
    # game logic
    game_over = False
    x_turn = True
    num_moves = 0
    print("\nEnter your move using the following integer positions:")
    print("0 | 1 | 2\n---------\n3 | 4 | 5\n---------\n6 | 7 | 8\n")
    while game_over == False:
        if userX == True:
            if x_turn == True:
                x_turn = player_move(x_turn, playerX, playerO)
            else:
                cpu_move(userX)
                x_turn = True
        else:
            if x_turn == True:
                cpu_move(userX)
                x_turn = False
            else:
                x_turn = player_move(x_turn, playerX, playerO)
        num_moves += 1
        if num_moves > 4:
            game_over = check_win(num_moves, playerX, playerO)
            if game_over == True:
                board[:] = [' '] * 9
                input("Enter any character to continue: ")
                break
        print_board()

# main function for tic-tac-toe
def main():
    while True:
        print("\nTime for Tic Tac Toe!\n")
        print("Select an option below 1-3:")
        print("1: Play against a friend")
        print("2: Play against a CPU")
        print("3: See scoreboard")
        print("q: Quit")
        choice = input("Your choice: ")
        print("")

        match choice:
            case "1":
                playerX, playerO = prompt_1v1()
                print("\nEnter your move using the following integer positions:")
                print("0 | 1 | 2\n---------\n3 | 4 | 5\n---------\n6 | 7 | 8\n")
                game_1v1(playerX, playerO)
            case "2":
                game_cpu()
            case "3":
                # sorts saved players dictionary into a list
                if len(saved_players) > 1:
                    sorted_players = list(saved_players.values())
                    for i in range(len(sorted_players) - 1):
                        for j in range(len(sorted_players) - i - 1):
                            if Player.get_tscore(sorted_players[j]) < Player.get_tscore(sorted_players[j + 1]):
                                sorted_players[j], sorted_players[j + 1] = sorted_players[j + 1], sorted_players[j]
                    # prints sorted list
                    for player in sorted_players:
                        Player.display_score(player)


                input("Enter any character to continue: ")
            case "q":
                print("Thanks for playing Tic Tac Toe!")
                break
            case _:
                print("Invalid option, try again.")
                input("Enter any character to continue: ")

main()