import random
import sys
import serial
import time
ser = serial.Serial('COM3', 9600)
def TEST():
	r = '101'
	ser.write(r.encode())

sys.setrecursionlimit(25000) # sometimes ther's a recursion error, so...

board = [' ' for x in range(50)] # create the board spaces



def print_board(board): #used to print board into terminal
    print(board[43], ' |', board[44], ' |', board[45], ' |', board[46], ' |', board[47], ' |', board[48], ' |', board[49])
    print('--', '+', '--', '+', '--', '+', '--', '+', '--', '+', '--', '+', '--')
    print(board[36], ' |', board[37], ' |', board[38], ' |', board[39], ' |', board[40], ' |', board[41], ' |', board[42])
    print('--', '+', '--', '+', '--', '+', '--', '+', '--', '+', '--', '+', '--')
    print(board[29], ' |', board[30], ' |', board[31], ' |', board[32], ' |', board[33], ' |', board[34], ' |', board[35])
    print('--', '+', '--', '+', '--', '+', '--', '+', '--', '+', '--', '+', '--')
    print(board[22], ' |', board[23], ' |', board[24], ' |', board[25], ' |', board[26], ' |', board[27], ' |', board[28])
    print('--', '+', '--', '+', '--', '+', '--', '+', '--', '+', '--', '+', '--')
    print(board[15], ' |', board[16], ' |', board[17], ' |', board[18], ' |', board[19], ' |', board[20], ' |', board[21])
    print('--', '+', '--', '+', '--', '+', '--', '+', '--', '+', '--', '+', '--')
    print(board[8], ' |', board[9], ' |', board[10], ' |', board[11], ' |', board[12], ' |', board[13], ' |', board[14])
    print('--', '+', '--', '+', '--', '+', '--', '+', '--', '+', '--', '+', '--')
    print(board[1], ' |', board[2], ' |', board[3], ' |', board[4], ' |', board[5], ' |', board[6], ' |', board[7])

def full_board(): # check if the board is full
	if board.count(' ') > 1: #check if board has at least 2 elements = ' ' 
		return
	else:
		print("It's a tie")
		quit()

def check_win(bo, le): #check all the options and if there's a win the game ends (bo = board, le = letter)
	if (bo[1] == le and bo[2] == le and bo[3] == le and bo[4] == le and bo[5] == le) or (bo[2] ==le and bo[3] == le and bo[4] == le and bo[5] == le and bo[6] == le) or (bo[3] ==le and bo[4] == le and bo[5] == le and bo[6] == le and bo[7] == le) or (bo[8] ==le and bo[9] == le and bo[10] == le and bo[11] == le and bo[12] == le) or (bo[9] ==le and bo[10] == le and bo[11] == le and bo[12] == le and bo[13] == le) or (bo[10] ==le and bo[11] == le and bo[12] == le and bo[13] == le and bo[14] == le) or (bo[15] ==le and bo[16] == le and bo[17] == le and bo[18] == le and bo[19] == le) or (bo[16] ==le and bo[17] == le and bo[18] == le and bo[19] == le and bo[20] == le) or (bo[17] ==le and bo[18] == le and bo[19] == le and bo[20] == le and bo[21] == le) or (bo[22] ==le and bo[23] == le and bo[24] == le and bo[25] == le and bo[26] == le) or (bo[23] ==le and bo[24] == le and bo[25] == le and bo[26] == le and bo[27] == le) or (bo[24] ==le and bo[25] == le and bo[26] == le and bo[27] == le and bo[28] == le) or (bo[29] ==le and bo[30] == le and bo[31] == le and bo[32] == le and bo[33] == le) or (bo[30] ==le and bo[31] == le and bo[32] == le and bo[33] == le and bo[34] == le) or (bo[31] ==le and bo[32] == le and bo[33] == le and bo[34] == le and bo[35] == le) or (bo[36] ==le and bo[37] == le and bo[38] == le and bo[39] == le and bo[40] == le) or (bo[37] ==le and bo[38] == le and bo[39] == le and bo[40] == le and bo[41] == le) or (bo[38] ==le and bo[39] == le and bo[40] == le and bo[41] == le and bo[42] == le) or (bo[43] ==le and bo[44] == le and bo[45] == le and bo[46] == le and bo[47] == le) or (bo[44] ==le and bo[45] == le and bo[46] == le and bo[47] == le and bo[48] == le) or (bo[45] ==le and bo[46] == le and bo[47] == le and bo[48] == le and bo[49] == le) or (bo[1] ==le and bo[8] == le and bo[15] == le and bo[22] == le and bo[29] == le) or (bo[8] ==le and bo[15] == le and bo[22] == le and bo[29] == le and bo[36] == le) or (bo[15] ==le and bo[22] == le and bo[29] == le and bo[36] == le and bo[43] == le) or (bo[2] ==le and bo[9] == le and bo[16] == le and bo[23] == le and bo[30] == le) or (bo[3] == le and bo[10] == le and bo[17] == le and bo[24] == le and bo[31] == le) or (bo[10] ==le and bo[17] == le and bo[24] == le and bo[31] == le and bo[38] == le) or (bo[17] ==le and bo[24] == le and bo[31] == le and bo[38] == le and bo[45] == le) or (bo[4] ==le and bo[11] == le and bo[18] == le and bo[25] == le and bo[32] == le) or (bo[11] ==le and bo[18] == le and bo[25] == le and bo[32] == le and bo[39] == le) or (bo[18] ==le and bo[25] == le and bo[32] == le and bo[39] == le and bo[46] == le) or (bo[5] ==le and bo[12] == le and bo[19] == le and bo[26] == le and bo[33] == le) or (bo[12] ==le and bo[19] == le and bo[26] == le and bo[33] == le and bo[40] == le) or (bo[19] ==le and bo[26] == le and bo[33] == le and bo[40] == le and bo[47] == le) or (bo[6] ==le and bo[13] == le and bo[20] == le and bo[27] == le and bo[34] == le) or (bo[13] ==le and bo[20] == le and bo[27] == le and bo[34] == le and bo[41] == le) or (bo[20] ==le and bo[27] == le and bo[34] == le and bo[41] == le and bo[48] == le) or (bo[7] ==le and bo[14] == le and bo[21] == le and bo[28] == le and bo[35] == le) or (bo[14] ==le and bo[21] == le and bo[28] == le and bo[35] == le and bo[42] == le) or (bo[21] ==le and bo[28] == le and bo[35] == le and bo[42] == le and bo[49] == le) or (bo[5] ==le and bo[11] == le and bo[17] == le and bo[23] == le and bo[29] == le) or (bo[6] ==le and bo[12] == le and bo[18] == le and bo[24] == le and bo[30] == le) or (bo[12] ==le and bo[18] == le and bo[24] == le and bo[30] == le and bo[36] == le) or (bo[7] ==le and bo[13] == le and bo[19] == le and bo[25] == le and bo[31] == le) or (bo[13] ==le and bo[19] == le and bo[25] == le and bo[31] == le and bo[37] == le) or (bo[19] ==le and bo[25] == le and bo[31] == le and bo[37] == le and bo[43] == le) or (bo[14] ==le and bo[20] == le and bo[26] == le and bo[32] == le and bo[38] == le) or (bo[20] ==le and bo[26] == le and bo[32] == le and bo[38] == le and bo[44] == le) or (bo[21] ==le and bo[27] == le and bo[33] == le and bo[39] == le and bo[45] == le) or (bo[15] ==le and bo[23] == le and bo[31] == le and bo[39] == le and bo[47] == le) or (bo[8] ==le and bo[16] == le and bo[24] == le and bo[32] == le and bo[40] == le) or (bo[16] ==le and bo[24] == le and bo[32] == le and bo[40] == le and bo[48] == le) or (bo[1] ==le and bo[9] == le and bo[17] == le and bo[25] == le and bo[33] == le) or (bo[9] ==le and bo[17] == le and bo[25] == le and bo[33] == le and bo[41] == le) or (bo[17] ==le and bo[25] == le and bo[33] == le and bo[41] == le and bo[49] == le) or (bo[2] ==le and bo[10] == le and bo[18] == le and bo[26] == le and bo[34] == le) or (bo[10] ==le and bo[18] == le and bo[26] == le and bo[34] == le and bo[42] == le) or (bo[3] ==le and bo[11] == le and bo[19] == le and bo[27] == le and bo[35] == le):
		print("Has won the ", le, "'s")
		quit()
	else:
		return

def check_win2(bo, le): # this is like the last one but with little different output. Is used for the AI function
						# to check if the computer or the player can win with a single move
	return (bo[1] == le and bo[2] == le and bo[3] == le and bo[4] == le and bo[5] == le) or (bo[2] ==le and bo[3] == le and bo[4] == le and bo[5] == le and bo[6] == le) or (bo[3] ==le and bo[4] == le and bo[5] == le and bo[6] == le and bo[7] == le) or (bo[8] ==le and bo[9] == le and bo[10] == le and bo[11] == le and bo[12] == le) or (bo[9] ==le and bo[10] == le and bo[11] == le and bo[12] == le and bo[13] == le) or (bo[10] ==le and bo[11] == le and bo[12] == le and bo[13] == le and bo[14] == le) or (bo[15] ==le and bo[16] == le and bo[17] == le and bo[18] == le and bo[19] == le) or (bo[16] ==le and bo[17] == le and bo[18] == le and bo[19] == le and bo[20] == le) or (bo[17] ==le and bo[18] == le and bo[19] == le and bo[20] == le and bo[21] == le) or (bo[22] ==le and bo[23] == le and bo[24] == le and bo[25] == le and bo[26] == le) or (bo[23] ==le and bo[24] == le and bo[25] == le and bo[26] == le and bo[27] == le) or (bo[24] ==le and bo[25] == le and bo[26] == le and bo[27] == le and bo[28] == le) or (bo[29] ==le and bo[30] == le and bo[31] == le and bo[32] == le and bo[33] == le) or (bo[30] ==le and bo[31] == le and bo[32] == le and bo[33] == le and bo[34] == le) or (bo[31] ==le and bo[32] == le and bo[33] == le and bo[34] == le and bo[35] == le) or (bo[36] ==le and bo[37] == le and bo[38] == le and bo[39] == le and bo[40] == le) or (bo[37] ==le and bo[38] == le and bo[39] == le and bo[40] == le and bo[41] == le) or (bo[38] ==le and bo[39] == le and bo[40] == le and bo[41] == le and bo[42] == le) or (bo[43] ==le and bo[44] == le and bo[45] == le and bo[46] == le and bo[47] == le) or (bo[44] ==le and bo[45] == le and bo[46] == le and bo[47] == le and bo[48] == le) or (bo[45] ==le and bo[46] == le and bo[47] == le and bo[48] == le and bo[49] == le) or (bo[1] ==le and bo[8] == le and bo[15] == le and bo[22] == le and bo[29] == le) or (bo[8] ==le and bo[15] == le and bo[22] == le and bo[29] == le and bo[36] == le) or (bo[15] ==le and bo[22] == le and bo[29] == le and bo[36] == le and bo[43] == le) or (bo[2] ==le and bo[9] == le and bo[16] == le and bo[23] == le and bo[30] == le) or (bo[3] == le and bo[10] == le and bo[17] == le and bo[24] == le and bo[31] == le) or (bo[10] ==le and bo[17] == le and bo[24] == le and bo[31] == le and bo[38] == le) or (bo[17] ==le and bo[24] == le and bo[31] == le and bo[38] == le and bo[45] == le) or (bo[4] ==le and bo[11] == le and bo[18] == le and bo[25] == le and bo[32] == le) or (bo[11] ==le and bo[18] == le and bo[25] == le and bo[32] == le and bo[39] == le) or (bo[18] ==le and bo[25] == le and bo[32] == le and bo[39] == le and bo[46] == le) or (bo[5] ==le and bo[12] == le and bo[19] == le and bo[26] == le and bo[33] == le) or (bo[12] ==le and bo[19] == le and bo[26] == le and bo[33] == le and bo[40] == le) or (bo[19] ==le and bo[26] == le and bo[33] == le and bo[40] == le and bo[47] == le) or (bo[6] ==le and bo[13] == le and bo[20] == le and bo[27] == le and bo[34] == le) or (bo[13] ==le and bo[20] == le and bo[27] == le and bo[34] == le and bo[41] == le) or (bo[20] ==le and bo[27] == le and bo[34] == le and bo[41] == le and bo[48] == le) or (bo[7] ==le and bo[14] == le and bo[21] == le and bo[28] == le and bo[35] == le) or (bo[14] ==le and bo[21] == le and bo[28] == le and bo[35] == le and bo[42] == le) or (bo[21] ==le and bo[28] == le and bo[35] == le and bo[42] == le and bo[49] == le) or (bo[5] ==le and bo[11] == le and bo[17] == le and bo[23] == le and bo[29] == le) or (bo[6] ==le and bo[12] == le and bo[18] == le and bo[24] == le and bo[30] == le) or (bo[12] ==le and bo[18] == le and bo[24] == le and bo[30] == le and bo[36] == le) or (bo[7] ==le and bo[13] == le and bo[19] == le and bo[25] == le and bo[31] == le) or (bo[13] ==le and bo[19] == le and bo[25] == le and bo[31] == le and bo[37] == le) or (bo[19] ==le and bo[25] == le and bo[31] == le and bo[37] == le and bo[43] == le) or (bo[14] ==le and bo[20] == le and bo[26] == le and bo[32] == le and bo[38] == le) or (bo[20] ==le and bo[26] == le and bo[32] == le and bo[38] == le and bo[44] == le) or (bo[21] ==le and bo[27] == le and bo[33] == le and bo[39] == le and bo[45] == le) or (bo[15] ==le and bo[23] == le and bo[31] == le and bo[39] == le and bo[47] == le) or (bo[8] ==le and bo[16] == le and bo[24] == le and bo[32] == le and bo[40] == le) or (bo[16] ==le and bo[24] == le and bo[32] == le and bo[40] == le and bo[48] == le) or (bo[1] ==le and bo[9] == le and bo[17] == le and bo[25] == le and bo[33] == le) or (bo[9] ==le and bo[17] == le and bo[25] == le and bo[33] == le and bo[41] == le) or (bo[17] ==le and bo[25] == le and bo[33] == le and bo[41] == le and bo[49] == le) or (bo[2] ==le and bo[10] == le and bo[18] == le and bo[26] == le and bo[34] == le) or (bo[10] ==le and bo[18] == le and bo[26] == le and bo[34] == le and bo[42] == le) or (bo[3] ==le and bo[11] == le and bo[19] == le and bo[27] == le and bo[35] == le)

def player_move(move, which_game):	# execute the player move

	if board[move] == ' ' and move >= 1 and move <= 49:
		board[move] = 'x'
		return move
	else:
		print('Invalid move')
		if which_game == 'ai':
			main2()

   
def player_move_o(move, which_game):	# execute the player move

	if board[move] == ' ' and move >= 1 and move <= 49:
		board[move] = 'o'
		return move
	else:
		print('Invalid move')
		if which_game == 'ai':
			main3()



def pc_move(move): # this is the computer move, it choses a position ramdomly
	move = random.randrange(1, 50)
	if board[move] == ' ':
		board[move] =  'o'
		move_str = str(move)
		ser.write(move_str.encode())
		return move
	else:
		full_board() # check if the board is full
		pc_move(move)
  
def pc_move_x(move): # this is the computer move, it choses a position ramdomly
	move = random.randrange(1, 50)
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
		player_move2(random.randrange(1, 50))
  
def player_move2_o(move): # this is the player move, and we knew where it went
	if board[move] == ' ':
		board[move] =  'o'
		return move
	else:
		full_board() # check if the board is full
		player_move2_o(random.randrange(1, 50))
  
def pc_blind(move): # this is the computer move, it choses a position ramdomly
	if board[move] == ' ':
		board[move] =  'o'
		move_str = str(move)
		ser.write(move_str.encode())
		return move
	else:
		full_board() # check if the board is full
		pc_blind(random.randrange(1, 50))
  
def pc_blind_x(move): # this is the computer move, it choses a position ramdomly
	if board[move] == ' ':
		board[move] =  'x'
		move_str = str(move)
		ser.write(move_str.encode())
		return move
	else:
		full_board() # check if the board is full
		pc_blind_x(random.randrange(1, 50))

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
	if board[25] == ' ':
		board[25] = 'o'
		move = 25
		move_str = str(move)
		ser.write(move_str.encode())
		return move

	# 5. same as step 3 but with 3 moves
	for let in ['o','x']:
		for i in possibleMoves:
			for j in possibleMoves:
				for t in possibleMoves:
					boardCopy = board[:]
					boardCopy[i] = let
					boardCopy[j] = let
					boardCopy[t] = let
					if check_win2(boardCopy, let):
						move = i
						board[i] = 'o'
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
	if board[25] == ' ':
		board[25] = 'x'
		move = 25
		move_str = str(move)
		ser.write(move_str.encode())
		return move

	# 5. same as step 3 but with 3 moves
	for let in ['o','x']:
		for i in possibleMoves:
			for j in possibleMoves:
				for t in possibleMoves:
					boardCopy = board[:]
					boardCopy[i] = let
					boardCopy[j] = let
					boardCopy[t] = let
					if check_win2(boardCopy, let):
						move = i
						board[i] = 'x'
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
	if board[25] == ' ':
		board[25] = 'o'
		move = 25
		move_str = str(move)
		ser.write(move_str.encode())
		return move

	# 5. same as step 3 but with 3 moves
	for let in ['o','x']:
		for i in possibleMoves:
			for j in possibleMoves:
				for t in possibleMoves:
					boardCopy = board[:]
					boardCopy[i] = let
					boardCopy[j] = let
					boardCopy[t] = let
					if check_win2(boardCopy, let):
						move = i
						move_str = str(move)
						board[i] = 'o'
						ser.write(move_str.encode())
						return move

	pc_blind(random.randrange(1, 50)) #dont know where to go, just go blind
 
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
	if board[25] == ' ':
		board[25] = 'x'
		move = 25
		move_str = str(move)
		ser.write(move_str.encode())
		return move

	# 5. same as step 3 but with 3 moves
	for let in ['o','x']:
		for i in possibleMoves:
			for j in possibleMoves:
				for t in possibleMoves:
					boardCopy = board[:]
					boardCopy[i] = let
					boardCopy[j] = let
					boardCopy[t] = let
					if check_win2(boardCopy, let):
						move = i
						move_str = str(move)
						board[i] = 'x'
						ser.write(move_str.encode())
						return move

	pc_blind_x(random.randrange(1, 50)) #dont know where to go, just go blind



def main2():    # the main function for the hard version of the game

	check_win(board, 'x')
	check_win(board, 'o')
	full_board()
	try:
		move = int(input("At which position do you move? 1-49   "))
	except ValueError:
		print("Invalid input. Please enter an integer number\n")
		main2()

	if move >= 1 and move <= 49:
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
		move = int(input("At which position do you move? 1-49   "))
	except ValueError:
		print("Invalid input. Please enter an integer number\n")
		main2_x()

	if move >= 1 and move <= 49:
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
		move = int(input("At which position do you move? 1-49   "))
	except ValueError:
		print("Invalid input. Please enter an integer number\n")
		main3()

	if move >= 1 and move <= 49:
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
		move = int(input("At which position do you move? 1-49   "))
	except ValueError:
		print("Invalid input. Please enter an integer number\n")
		main3_x()

	if move >= 1 and move <= 49:
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
 
def version_7x7():  # chose a version of the game
    a = '7'
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
