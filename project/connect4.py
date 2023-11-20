import random
import os
import time
def clear_screen():
	"""
	Clears the terminal for Windows and Linux/MacOS.

	:return: None
	"""
	os.system('cls' if os.name == 'nt' else 'clear')


def print_rules():
	"""
	Prints the rules of the game.

	:return: None
	"""
	print("================= Rules =================")
	print("Connect 4 is a two-player game where the")
	print("objective is to get four of your pieces")
	print("in a row either horizontally, vertically")
	print("or diagonally. The game is played on a")
	print("6x7 grid. The first player to get four")
	print("pieces in a row wins the game. If the")
	print("grid is filled and no player has won,")
	print("the game is a draw.")
	print("=========================================")


def validate_input(prompt, valid_inputs):
    # Prompting the user for a input with a string from function parameter and initializing variable userinput to input value
	userinput = input(prompt)
    # Notify user of invalid input if their input is not in valid_inputs parameter
	while not userinput in valid_inputs:
			print("Invalid input, please try again.")
	# prompting for their input again until userinput is in valid_inputs
			userinput = input(prompt)
    # Returns the userinput as a string
	return userinput


def create_board():
    """
    Returns a 2D list of rows and columns to represent
    the game board. Default cell value is 0.

    :return: A 2D list of nxm dimensions.
    """
    # Implement your solution below
    # List comprehension to iterate and append in the inner and outer lists. The inner list appends '0' 7 times and the outer list loops it 6 times
    board = [[0 for x in range(7)] for x in range(6)]
    return (board)


def print_board(board):
    print('=' * 10, 'Connect4', '=' * 9)
    print("Player 1: X       Player 2: O\n\n  1   2   3   4   5   6   7")
    row = ' '
    for j in range(6):
        row = ''
        print(' ---' * 7)
        for i in range(7):
            if board[j][i] == 0:
                    row += '|   '
            elif board[j][i] == 1:
                    row += '| X '
            elif board[j][i] == 2:
                    row += '| O '
        print(row + '|')

    print(' ---' * 7)
    print('=' * 29)


def drop_piece(board, player, column):
    # If the first row of column given in parameter does not equal 0 then that column must be full
	if board[0][column-1] != 0:
    # returns False for full columns
		return False
    # if the first row is not full
	else:
    # loop through all the rows starting from the bottom row
		for i in range(6):
    # For a specific column, the piece will be dropped in the bottom most row
    # As soon as function detects a row is vacant
			if board[-i-1][column-1] == 0:
    # player piece will be dropped into that column at the bottom most row
				board[-i-1][column-1] = player
    # the code no longer needs to check any more rows above as it is going from bottom to top therefore breaking out the for-loop
				break
    # returns True if column is vacant
		return True
    # column - 1 because python indexing starts at 0 but column indexing starts at 1
    # e.g if user wants to drop piece into column 1 by passing 1 into the function parameter without implementing column - 1
    # the piece will be dropped in column 2 instead as column 1 = index 0, and column 2 = index 1


def execute_player_turn(player, board):
	while True:
		# prompt user for input using validate_input()
		column = int(validate_input(f"Player {player}, please enter the column you would like to drop your piece into: ", ["1", "2", "3", "4", "5", "6", "7"]))
		# checks if drop_piece can be executed
		if drop_piece(board, player, column) == False:
			print("That column is full, please try again.")
		# continues prompting until executed succesfully
			continue
		else:
			break
	return column



def end_of_game(board):
	"""
		Prompts user for a legal move given the current game board
		and executes the move.

		:return: Column that the piece was dropped into, int.
		"""
	n_rows = 7
	n_columns = 6
	n_k = 4
	n_players = 2
	# Calls the helper function to check if there are four elements in the rows, columns or diagonals
	row_result = row_check(board, n_k, n_players) # Checks if there are matching values in any rows
	column_result = column_check(board, n_rows,  n_k, n_players) # Checks if there's a win in any column
	primary_diagonal_result = Primarydiag(
		board, n_rows, n_columns, n_k, n_players)# Checks if the diagonals have matching elements
	secondary_diagonal_result = Secondarydiag(
		board, n_rows, n_columns, n_k, n_players)
	incomplete_game_result = incomplete_game(board)
	# Returns appropriate value if any of the functions return a non zero value
	if column_result:
		return int(column_result)
	elif row_result:
		return int(row_result)
	elif primary_diagonal_result:			# Returns the statements
		return int(primary_diagonal_result)
	elif secondary_diagonal_result:
		return int(secondary_diagonal_result)
	elif incomplete_game_result:
		return 0
	else:
		return 3


def row_check(board, n_k, n_players):
	""" Extracts rows of the table and checks if there's a win
	"""
	for row in board:
		value = linear_check(row, n_k, n_players) # Extracts every row as a list and passes it to the linear checker
		if value != False:
			return value


def column_check(board, n_rows, n_k, n_players):
	"""Extracts columns of the game board and passes to the linear_check function"""
	for i in range(0, n_rows):
		column = [row[i] for row in board] # Generates a new list by appending the first item of every row
		value = linear_check(column, n_k, n_players)
		if value != False:
			return value


def linear_check(data, n_k, n_players):
	"""Uses string manipulation to check if there's a win in the given list"""

	data = str(data).replace(',', '').replace(' ', '') # Converts the list to string and removes whitespaces and commas
	validator = [str(i)*n_k for i in range(1, n_players+1)]

	for row in validator:
		if row in data:
			return row[0]	# Checks if the string is present in the list data
		else:
			pass
	return False


def incomplete_game(board):
	"""Checks if the board is incomplete"""
	if 0 in board[0]:
		return True
	else:
		return False


def Primarydiag(board, n_rows, n_columns, n_k, n_players):
	"""Extracts the diagonals of the board"""
	# compute the range for k
	if n_rows > n_columns:
		k_range = n_rows
	else:
		k_range = n_columns
	# go through all the diagonals
	for k in range(-1 * k_range, k_range):
		diagonal = []
		for i in range(len(board)):
			for j in range(len(board[0])):
				if i - j == k:
					diagonal.append(board[i][j])
		if len(diagonal) > n_k - 1:

			value = linear_check(diagonal, n_k, n_players)
			if value != False:
				return value  # should exit the loop if a match is found.


def Secondarydiag(board, n_rows, n_columns, n_k, n_players):
	"""Extracts the other set of diagonals from the game board"""
	# compute the range for k
	if n_rows > n_columns:
		k_range = n_rows
	else:
		k_range = n_columns
	# go through all the diagonals
	for k in range(0, k_range * 2):
		diagonal = []
		for i in range(len(board)):
			for j in range(len(board[0])):
				if i + j == k:
					diagonal.append(board[i][j])

		if len(diagonal) > n_k - 1:

			value = linear_check(diagonal, n_k, n_players)
			if value != False:
				return value  # should exit the loop if a match is found.



def local_2_player_game():
    updatedBoard = create_board()
    column = 0
    # checking if updatedboard has 4 consecutive pieces
    while end_of_game(updatedBoard) == 0:
        clear_screen()
        print_board(updatedBoard)
    # clear_screen() and print_board(updatedBoard) above will only execute in the first iteration
        if column != 0:
            print(f"Player 2 dropped a piece into column {column}")
    # prompting player 1 to execute first turn
        column = execute_player_turn(1, updatedBoard)
    # checking if updatedboard does not have 4 consecutive pieces
        if end_of_game(updatedBoard) != 0:
            break
        clear_screen()
        print_board(updatedBoard)
    # printing player 1's previous move to the console
        print(f"Player 1 dropped a piece into column {column}")
    # prompting player 2 to make a move
        column = execute_player_turn(2, updatedBoard)
    # checking if updatedboard does not have 4 consecutive pieces
        if end_of_game(updatedBoard) != 0:
            break
    # printing player 2's previous move to the console and looping back to the top back to player 1's turn
        print(f"Player 2 dropped a piece into column {column}")

    # checking if game is a draw
    if end_of_game(updatedBoard) == 3:
        clear_screen()
        print_board(updatedBoard)
        print("It's a draw!")

    else:
        clear_screen()
        print_board(updatedBoard)
    # print the winner of the game to the console
        print(f"Player {end_of_game(updatedBoard)} wins!")

def check_row_3(board):
    # Loop through the rows of the board
    # Checks whether the number of 2s in the row = 4
    for i in range(6):
        counter = 0
        for j in range(7):
            if board[i][j] == 2:
                counter += 1
            elif board[i][j] != 2:
                counter = 0
            if counter == 3:
                return 2
    # Checks whether the number of 1s in the row = 4
        counter = 0
        for j in range(7):
            if board[i][j] == 1:
                counter += 1
            elif board[i][j] != 1:
                counter = 0
            if counter == 3:
                return 1
    return 0

def check_column_3(board):
    # Loop through the rows of the board
    # Checks whether the number of 2s in the column = 4
    for i in range(7):
        counter = 0
        for j in range(6):
            if board[j][i] == 2:
                counter += 1
            elif board[j][i] != 2:
                counter = 0
            if counter == 3:
                return 2
    # Checks whether the number of 1s in the column = 4
        counter = 0
        for j in range(6):
            if board[j][i] == 1:
                counter += 1
            elif board[j][i] != 1:
                counter = 0
            if counter == 3:
                return 1
    return 0

def check_diagup_3(board):
    # Making a look up table [row, column, how many iterations]
    LUT =[
    [3, 0, 4],
    [4, 0, 5],
    [5, 0, 6],
    [5, 1, 6],
    [5, 2, 5],
    [5, 3, 4]
        ]
    # Loop through the diagup of the board
    # Checks whether the number of 2s in the column = 4
    for i in range(6):
        counter = 0
        for j in range(LUT[i][2]):
            if board[LUT[i][0] - j][LUT[i][1] + j] == 2:
                counter += 1
            elif board[LUT[i][0] - j][LUT[i][1] + j] != 2:
                counter = 0
            if counter == 3:
                return 2
    # Checks whether the number of 1s in the column = 4
        counter = 0
        for j in range(LUT[i][2]):
            if board[LUT[i][0] - j][LUT[i][1] + j] == 1:
                counter += 1
            elif board[LUT[i][0] - j][LUT[i][1] + j] != 1:
                counter = 0
            if counter == 3:
                return 1
    return 0

def check_diagdown_3(board):
    # Making a look up table [row, column, how many iterations]
    LUT =[
    [2, 0, 4],
    [1, 0, 5],
    [0, 0, 6],
    [0, 1, 6],
    [0, 2, 5],
    [0, 3, 4]
        ]
    # Loop through the diagup of the board
    # Checks whether the number of 2s in the column = 4
    for i in range(6):
        counter = 0
        for j in range(LUT[i][2]):
            if board[LUT[i][0] + j][LUT[i][1] + j] == 2:
                counter += 1
            elif board[LUT[i][0] + j][LUT[i][1] + j] != 2:
                counter = 0
            if counter == 3:
                return 2
    # Checks whether the number of 1s in the column = 4
        counter = 0
        for j in range(LUT[i][2]):
            if board[LUT[i][0] + j][LUT[i][1] + j] == 1:
                counter += 1
            elif board[LUT[i][0] + j][LUT[i][1] + j] != 1:
                counter = 0
            if counter == 3:
                return 1
    return 0

def end_of_game_3(board):
    game_state = check_row_3(board)
    if game_state in [1, 2]:
        return game_state
    game_state = check_column_3(board)
    if game_state in [1, 2]:
        return game_state
    game_state = check_diagup_3(board)
    if game_state in [1, 2]:
        return game_state
    game_state = check_diagdown_3(board)
    if game_state in [1, 2]:
        return game_state
    if 0 in board[0]:
        return 0
    else:
        return 3


from copy import copy, deepcopy


def main():
    while True:
        clear_screen()
	# Print options
        print("=============== Main Menu ===============\nWelcome to Connect 4!\n1. View Rules\n2. Play a local 2 player game\n3. Play a game against the computer\n4. Exit\n=========================================")
        choosen_option = validate_input("Pick an option (1, 2, 3, 4): ", ["1", "2", "3", "4"])
        if choosen_option == "1": # if user selects to see the rules
            clear_screen()
            print_rules()
            input("Press enter to return to main menu")
        elif choosen_option == "2": # if user chooses to play a game against local human players
            local_2_player_game()
        elif choosen_option == "3": # if user chooses to play a game against CPU
            game_against_cpu()
        else: # Exits the program i.e. stop the loop
            return None


def cpu_player_easy(board, player):
    """
    Executes a move for the CPU on easy difficulty. This function
    plays a randomly selected column.

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player whose turn it is, integer value of 1 or 2.
    :return: Column that the piece was dropped into, int.
    """
	# Generates a random number between 1 and 7 to simulate a drop in the column of the board.
    while True:
        column = random.randint(1, 7)
        if drop_piece(board, player, column):
            return column


def cpu_player_medium(board, player):
    # defining the player & opponent
    if player == 1:
        opponent = 2
    else:
        opponent = 1
    winmove = False
    blockmove = False
# checking for a possible move to win instantly
    imgboard = deepcopy(board)
# looping through all possible columns
    for j in range(7):
# creating an imaginary board state before any piece has been dropped
        previous = deepcopy(imgboard)
# checking for vacant columns
        if imgboard[0][j] == 0:
# try dropping a piece into a vacant column
            drop_piece(imgboard, player, j+1)
# checkig whether this move results in a win
        if end_of_game(imgboard) == player:
# if so, drop the piece on the actual board
            drop_piece(board, player, j+1)
# return column the piece was dropped into and exit function
            winmove = True
            return j+1
# if the drop does not result in win the set board back to previous state and try next column
        else:
            imgboard = previous
# checking for a possible move to block opponent's instant win
    if winmove == False:
        for j in range(7):
            previous = deepcopy(imgboard)
            if imgboard[0][j] == 0:
# try dropping an opponent piece into a vacant column
                drop_piece(imgboard, opponent, j+1)
# if opponent is able to play a win move after
                if end_of_game(imgboard) == opponent:
# drop a player piece in that colum to prevent opponent's win
                    drop_piece(board, player, j+1)
                    blockmove = True
# return column number
                    return j+1
                else:
                    imgboard = previous
# if both winmove and blockmove cannot be played, drop a piece into a random column
    if winmove == False and blockmove == False:
        return cpu_player_easy(board, player)


def cpu_player_hard(board, player):
    if player == 1:
        opponent = 2
    else:
        opponent = 1
    winmove = False
    blockmove = False

# checking for win moves for cpu
    imgboard = deepcopy(board) # creating an imaginary board, which can operate independent to
    for j in range(7):
        previous = deepcopy(imgboard)
        if imgboard[0][j] == 0:
            drop_piece(imgboard, player, j+1)
            if end_of_game(imgboard) == player:
                drop_piece(board, player, j+1)
                winmove = True
                return j+1
            else:
                imgboard = previous

# checking for block moves to prevent oppoent win
    if winmove == False:
        for j in range(7):
            previous = deepcopy(imgboard)
            if imgboard[0][j] == 0:
                drop_piece(imgboard, opponent, j+1)
                if end_of_game(imgboard) == opponent:
                    drop_piece(board, player, j+1)
                    blockmove = True
                    return j+1
                else:
                    imgboard = previous

# check for wrong moves that will enable the opponent to win the move after
    if winmove == False and blockmove == False:


        wrongmoves = []
# implement imaginary scenarios on what wrong moves could be possible after testing dropping a piece in each column
        for i in range(7):
            imgboard = deepcopy(board)
            if drop_piece(imgboard, player, i+1):
                if drop_piece(imgboard, opponent, i+1):
                    if end_of_game(imgboard) == opponent:
                        wrongmoves.append(i+1)



# prevent 4 move/quick wins by the player
        if 0 in board[5]:
            if board[4] == [0, 0, 0, 0, 0, 0, 0]:
                for i in range(7):
                    if board[5][i] != 0:
                        wrongmoves.append(i+1)

        freecolumns = []
        bestmoves = []
        possiblemoves = []
        for i in range(7):
            if board[0][i] == 0:
                freecolumns.append(i+1)
# determine what columns are available to be played


# finding the intersection between freecolumns and wrongmoves' and appending those elements to possiblemoves
        for i in range(7):
            if (i+1 in freecolumns) and not (i+1 in wrongmoves):
                possiblemoves.append(i+1)


        # need to change under here to further improve win rate
# secure a win in 4 moves
        # check if it is the first round
        if board[5].count(0) + board[4].count(0) == 13: # if the sum of zeros in the bottom 2 rows add up to 13
            if board[5][3] == 0:
                drop_piece(board, player, 4)
                return 4 # drop in column 4 as the first move when possible
        elif board[5][3] == player: # if CPU has a piece in bottom row middle column (column 4)
            # check if it is less than 4 rounds
            if board[5].count(0) + board[4].count(0) + board[3].count(0) + board[2].count(0) >= 21:
                # check if it is possible to connect4 bottom row
                counter = 0
                for element in board[5]:
                    if element != opponent:
                        counter += 1
                    else:
                        counter = 0
                    if counter == 4: # then we continue
                        # second round
                        if board[5].count(0) + board[4].count(0) == 11: # if the sum of zeros in the bottom 2 rows add up to 11
                            for column in [3, 5]:
                                if board[5][column - 1] == 0:
                                    drop_piece(board, player, column)
                                    return column
                        # third round
                        elif board[5].count(0) + board[4].count(0) + board[3].count(0) == 16: # if the sum of zeros in the bottom 3 rows add up to 16
                            for column in [3, 5, 2, 6]:
                                if board[5][column - 1] == 0:
                                    if board[5][column] == player and board[5][column - 2] == player:
                                        drop_piece(board, player, column)
                                        return column
                        # the fourth round should be secure via winmove

# checking for block moves to prevent oppoent to connect3
        for j in range(7):
            previous = deepcopy(imgboard)
            if imgboard[0][j] == 0:
                drop_piece(imgboard, opponent, j+1)
                if end_of_game_3(imgboard) == opponent: #smthing wrong w this line
                    if j+1 not in wrongmoves:
                        if j+1 not in [1,2,6,7] and (board[1][j] == 0):
                            drop_piece(board, player, j+1)
                            return j+1
                    else:
                        imgboard = previous
                else:
                    imgboard = previous


# checking for placing a 3 in a row
        imgboard = deepcopy(board)
        for j in range(7):
            previous = deepcopy(imgboard)
            if imgboard[0][j] == 0:
                drop_piece(imgboard, player, j+1)
                if end_of_game_3(imgboard) == player:
                    if j+1 not in wrongmoves:
                        if j+1 not in [1,2,6,7] and (board[1][j] == 0):
                            drop_piece(board, player, j+1)
                            return j+1
                        else:
                            imgboard = previous
                else:
                    imgboard = previous

        if possiblemoves == []:
            choices = random.randint(2,6)
        else:
            choices = random.choice(possiblemoves)
            for i in range(3,5):
                if i in possiblemoves:
                    bestmoves.append(i)
            if len(bestmoves) > 0:
                choices = random.choice(bestmoves)

            # randomise a good column
            drop_piece(board, player, choices)
            return choices


def game_against_cpu():
    end_game_message = [
        "Player 1 wins!",
        "Player 2 wins!",
        "Draw!"
    ]
    difficulty = validate_input("Select the difficulty (easy, medium, hard): ", ["easy", "medium", "hard"])
    if difficulty == "easy":
        board = create_board()
        print_board(board)
        while end_of_game(board) == 0:
            execute_player_turn(1, board)
            clear_screen()
            if end_of_game(board) == 0:
                cpu_move = cpu_player_easy(board, 2)
                print_board(board)
                print("Player CPU dropped a piece into column", cpu_move)
        print_board(board)
        print(end_game_message[end_of_game(board) - 1])
        time.sleep(2)
        return end_of_game(board)

    elif difficulty == "medium":
        board = create_board()
        print_board(board)
        while end_of_game(board) == 0:
            execute_player_turn(1, board)
            clear_screen()
            if end_of_game(board) == 0:
                cpu_move = cpu_player_medium(board, 2)
                print_board(board)
                print("Player CPU dropped a piece into column", cpu_move)
        print_board(board)
        print(end_game_message[end_of_game(board) - 1])
        time.sleep(2)
        return end_of_game(board)
    else:
        board = create_board()
        print_board(board)
        while end_of_game(board) == 0:
            execute_player_turn(1, board)
            clear_screen()
            if end_of_game(board) == 0:
                cpu_move = cpu_player_hard(board, 2)
                print_board(board)
                print("Player CPU dropped a piece into column", cpu_move)
        print_board(board)
        print(end_game_message[end_of_game(board) - 1])
        time.sleep(2)
        return end_of_game(board)


if __name__ == "__main__":
    main()
