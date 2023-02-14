import random
import sys
import serial
import time
ser = serial.Serial('COM3', 9600)


sys.setrecursionlimit(25000) # sometimes ther's a recursion error, so...

board = [' ' for x in range(10)] # create the board spaces

def test_san1():
	b = '100'
	ser.write(b.encode())


def print_board(board): #used to print board into terminal
	print(board[7], ' |', board[8], ' |', board[9])
	print('--', '+', '--', '+', '--')
	print(board[4], ' |', board[5], ' |', board[6])
	print('--', '+', '--', '+', '--')
	print(board[1], ' |', board[2], ' |', board[3])

def full_board(): # check if the board is full
	if board.count(' ') > 1: #check if board has at least 2 elements = ' ' 
		return
	else:
		print("It's a tie")
		quit()

def check_win(bo, le): #check all the options and if there's a win the game ends (bo = board, le = letter)
	if (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le):
		print("Has won the ", le, "'s")
		quit()
	else:
		return

def check_win2(bo, le): # this is like the last one but with little different output. Is used for the AI function
						# to check if the computer or the player can win with a single move
	return (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le)

def player_move(move, which_game):	# execute the player move

	if board[move] == ' ' and move >= 1 and move <= 9:
		board[move] = 'x'
		return move
	else:
		print('Invalid move')
		if which_game == 'ai':
			main2()

   
def player_move_o(move, which_game):	# execute the player move

	if board[move] == ' ' and move >= 1 and move <= 9:
		board[move] = 'o'
		return move
	else:
		print('Invalid move')
		if which_game == 'ai':
			main3()



def pc_move(move): # this is the computer move, it choses a position ramdomly
	move = random.randrange(1, 10)
	if board[move] == ' ':
		board[move] =  'o'
		move_str = str(move)
		ser.write(move_str.encode())
		return move
	else:
		full_board() # check if the board is full
		pc_move(move)
  
def pc_move_x(move): # this is the computer move, it choses a position ramdomly
	move = random.randrange(1, 10)
	if board[move] == ' ':
		board[move] =  'x'
		move_str = str(move)
		ser.write(move_str.encode())
		return move
	else:
		full_board() # check if the board is full
		pc_move_x(move)
  
def player_move2(move): # this is the player move, and we knew where it went
	if board[move] == ' ':
		board[move] =  'x'
		return move
	else:
		full_board() # check if the board is full
		player_move2(random.randrange(1, 10))
  
def player_move2_o(move): # this is the player move, and we knew where it went
	if board[move] == ' ':
		board[move] =  'o'
		return move
	else:
		full_board() # check if the board is full
		player_move2_o(random.randrange(1, 10))
  
def pc_blind(move): # this is the computer move, it choses a position ramdomly
	if board[move] == ' ':
		board[move] =  'o'
		move_str = str(move)
		ser.write(move_str.encode())
		return move
	else:
		full_board() # check if the board is full
		pc_blind(random.randrange(1, 10))
  
def pc_blind_x(move): # this is the computer move, it choses a position ramdomly
	if board[move] == ' ':
		board[move] =  'x'
		move_str = str(move)
		ser.write(move_str.encode())
		return move
	else:
		full_board() # check if the board is full
		pc_blind_x(random.randrange(1, 10))

def ai(move): # this is how the AI chooses its move.
	
	# 1. check if the computer can win with a single movement
	# 2. whith the same code, check if the player can win with a move
	possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0] 
	move = 0
	for let in ['o','x']:
		for i in possibleMoves:
			boardCopy = board[:]
			boardCopy[i] = let
			if check_win2(boardCopy, let): #let could be 'o' or 'x'
				move = i
				board[i] = 'o' #board[i] will fill with 'o' not to let the player win or will fill to win
				move_str = str(move)
				ser.write(move_str.encode())
				return move


	# 3. the same as before but with 2 moves
	for let in ['o','x']:
		for i in possibleMoves:
			for j in possibleMoves:
				boardCopy = board[:]
				boardCopy[i] = let
				boardCopy[j] = let
				if check_win2(boardCopy, let):
					move = i
					board[i] = 'o'
					move_str = str(move)
					ser.write(move_str.encode())
					return move

	# 4. check if the middle is empty, if it is chose that.
	if board[5] == ' ':
		board[5] = 'o'
		move = 5
		move_str = str(move)
		ser.write(move_str.encode())
		return move

	pc_move(move)
 
def ai_x(move): # this is how the AI chooses its move.
	
	# 1. check if the computer can win with a single movement
	# 2. whith the same code, check if the player can win with a move
	possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0] 
	move = 0
	for let in ['o','x']:
		for i in possibleMoves:
			boardCopy = board[:]
			boardCopy[i] = let
			if check_win2(boardCopy, let): #let could be 'o' or 'x'
				move = i
				board[i] = 'x' #board[i] will fill with 'o' not to let the player win or will fill to win
				move_str = str(move)
				ser.write(move_str.encode())
				return move

	# 3. the same as before but with 2 moves
	for let in ['o','x']:
		for i in possibleMoves:
			for j in possibleMoves:
				boardCopy = board[:]
				boardCopy[i] = let
				boardCopy[j] = let
				if check_win2(boardCopy, let):
					move = i
					board[i] = 'x'
					move_str = str(move)
					ser.write(move_str.encode())
					return move

	# 4. check if the middle is empty, if it is chose that.
	if board[5] == ' ':
		board[5] = 'x'
		move = 5
		move_str = str(move)
		ser.write(move_str.encode())
		return move

	pc_move_x(move)
 
def ai2(move): # this is how the AI chooses its move.
	
	# 1. check if the computer can win with a single movement
	# 2. whith the same code, check if the player can win with a move
	possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
	move = 0
	for let in ['o','x']:
		for i in possibleMoves:
			boardCopy = board[:]
			boardCopy[i] = let
			if check_win2(boardCopy, let): #let could be 'o' or 'x'
				move = i
				move_str = str(move)
				board[i] = 'o' #board[i] will fill with 'o' not to let the player win or will fill to win
				ser.write(move_str.encode())
				return move


	# 3. the same as before but with 2 moves
	for let in ['o','x']:
		for i in possibleMoves:
			for j in possibleMoves:
				boardCopy = board[:]
				boardCopy[i] = let
				boardCopy[j] = let
				if check_win2(boardCopy, let):
					move = i
					move_str = str(move)
					board[i] = 'o'
					ser.write(move_str.encode())
					return move

	# 4. check if the middle is empty, if it is chose that.
	if board[5] == ' ':
		board[5] = 'o'
		move = 5
		move_str = str(move)
		ser.write(move_str.encode())
		return move

	pc_blind(random.randrange(1, 10)) #dont know where to go, just go blind
 
def ai2_x(move): # this is how the AI chooses its move.
	
	# 1. check if the computer can win with a single movement
	# 2. whith the same code, check if the player can win with a move
	possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
	move = 0
	for let in ['o','x']:
		for i in possibleMoves:
			boardCopy = board[:]
			boardCopy[i] = let
			if check_win2(boardCopy, let): #let could be 'o' or 'x'
				move = i
				move_str = str(move)
				board[i] = 'x' #board[i] will fill with 'o' not to let the player win or will fill to win
				ser.write(move_str.encode())
				return move

	# 3. the same as before but with 2 moves
	for let in ['o','x']:
		for i in possibleMoves:
			for j in possibleMoves:
				boardCopy = board[:]
				boardCopy[i] = let
				boardCopy[j] = let
				if check_win2(boardCopy, let):
					move = i
					move_str = str(move)
					board[i] = 'x'
					ser.write(move_str.encode())
					return move

	# 4. check if the middle is empty, if it is chose that.
	if board[5] == ' ':
		board[5] = 'x'
		move = 5
		move_str = str(move)
		ser.write(move_str.encode())
		return move

	pc_blind_x(random.randrange(1, 10)) #dont know where to go, just go blind



def main2():    # the main function for the hard version of the game

	check_win(board, 'x')
	check_win(board, 'o')
	full_board()
	try:
		move = int(input("At which position do you move? 1-9   "))
	except ValueError:
		print("Invalid input. Please enter an integer number\n")
		main2()

	if move >= 1 and move <= 9:
		pass
	else:
		print('Invalid position')
		main2()
	player_move(move, 'ai')
	print_board(board)
	print("\n")
	ai(move)
	print_board(board)
	print("\n")

	main2()
 
def main2_x():    # the main function for the hard version of the game

	check_win(board, 'x')
	check_win(board, 'o')
	full_board()
	try:
		move = int(input("At which position do you move? 1-9   "))
	except ValueError:
		print("Invalid input. Please enter an integer number\n")
		main2_x()

	if move >= 1 and move <= 9:
		pass
	else:
		print('Invalid position')
		main2_x()
	player_move_o(move, 'ai')
	print_board(board)
	print("\n")
	ai_x(move)
	print_board(board)
	print("\n")

	main2_x()
  
def main3():
	check_win(board, 'x')
	check_win(board, 'o')
	full_board()
	try:
		move = int(input("At which position do you move? 1-9   "))
	except ValueError:
		print("Invalid input. Please enter an integer number\n")
		main3()

	if move >= 1 and move <= 9:
		pass
	else:
		print('Invalid position')
		main3()
	player_move2(move)
	print_board(board)
	print("\n")
	ai2(move)
	print_board(board)
	print("\n")
	main3()
 
def main3_x():
	check_win(board, 'x')
	check_win(board, 'o')
	full_board()
	try:
		move = int(input("At which position do you move? 1-9   "))
	except ValueError:
		print("Invalid input. Please enter an integer number\n")
		main3_x()

	if move >= 1 and move <= 9:
		pass
	else:
		print('Invalid position')
		main3_x()
	player_move2_o(move)
	print_board(board)
	print("\n")
	ai2_x(move)
	print_board(board)
	print("\n")
	main3_x()
 
def version_3x3():  # chose a version of the game
    a = '3'
    ser.write(a.encode())
    mode = str(input("what is ai mode: [o] or [x]?   "))
    if (mode == 'o'):
        ser.write(mode.encode())
        turn = str(input("Who play first? (m/p)"  ))
        if turn.lower() == 'p':
            main2()
        elif turn.lower() == 'm':
            pc_blind(1)
            print_board(board)
            print("\n")
            main3()
    elif (mode == 'x'):
        ser.write(mode.encode())
        turn2 = str(input("Who play first? (m/p)"  ))
        if turn2.lower() == 'p':
            main2_x()
        elif turn2.lower() == 'm':
            pc_blind_x(1)
            print_board(board)
            print("\n")
            main3_x()

