N = 9	# size of the board [9 * 9]

board = [	[6, '.', 2, '.', '.', '.', '.', 5, 3], 
			['.', 8, '.', '.', '.', 2, '.', '.', '.'], 
			['.', '.', '.', '.', '.', 4, '.', '.', 7], 
			[2, 6, 3, 1, '.', '.', '.', '.', 9], 
			['.', '.', '.', 9, '.', '.', '.', 6, '.'], 
			['.', 5, '.', 3, '.', 6, '.', '.', 2], 
			['.', '.', '.', '.', '.', '.', 4, '.', 5], 
			['.', 2, 8, '.', '.', 3, '.', '.', '.'], 
			[1, '.', '.', '.', '.', '.', 7, '.', '.']    ]


def isValid(value, row, col):
	# if the value already present in the the
	# inserted row or column return False
	if value in board[row][:] or value in [row[col] for row in board]:
		return False

	# if the value is present in the inserted box
	# return False
	box_pos_row = int(row / 3)
	box_pos_col = int(col / 3)
	for i in range(3):
		for j in range(3):
			if value == board[box_pos_row*3 + i][box_pos_col*3 +j]:
				return False
	return True


def insertValue(value, row, col):
	board[row][col] = value


def resetValue(row, col):
	board[row][col] = '.'


def isSolvable():
	# enumerate all positions
	for row in range(N):
		for col in range(N):
			if board[row][col] != '.':
				# value is set previously
				continue
			else:
				for val in range(1, N+1):
					# try to insert each values from 1-9
					# and see if there is any solution
					if isValid(val, row, col):
						# if the value has no confliction
						insertValue(val, row, col)
						if isSolvable():
							# recursively check the updated board
							return True
						else:
							# if the value doesn't give a solution
							# remove the value
							resetValue(row, col)
					# here the backtracking is happening
				return False	# has no solution, all values are exhausted
	return True # all squares are visited
	''' if a prefilled board is given which does not contain a solution,
		this condition will still result in a positive response
		because it is only checking "if the board is fully visited or not"
	'''


def printBoard():
	print('-------------------------')
	for x in range(N):
		print('| ', end = '')
		for y in range(N):
			print(str(board[x][y]), end = '')

			if y == N-1:
				print(' |')
			elif (y+1) % 3 == 0:
				print(' | ', end = '')
			else:
				print('|', end = '')

		if (x + 1) % 3 != 0:
			continue
		print('-------------------------')


printBoard()

if isSolvable():
	print('This board is solvable.')
	printBoard()
else:
	print('This board has no solution.')
