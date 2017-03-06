# Move 1: Go in a corner.
# Move 2: If the other player did not go there then go in the opposite corner to move 1. Otherwise go in a free corner.
# Move 3: If there are two Xs and a space in a line (in any order) then go in that space. Otherwise if there are two Os and a space in a line then go in that space. Otherwise go in a free corner.
# Move 4: If there are two Xs and a space in a line (in any order) then go in that space. Otherwise if there are two Os and a space in a line then go in that space. Otherwise go in a free corner.
# Move 5: Go in the free space.

class Bot:

	def __init__(self, player):
		self.player = player

	def get_all_lines(self, board):
		lines = []
		lines.append([[board[0][0], board[0][1], board[0][2]], {0: [0,0], 1: [0,1], 2: [0,2]}])
		lines.append([[board[1][0], board[1][1], board[1][2]], {0: [1,0], 1: [1,1], 2: [1,2]}])
		lines.append([[board[2][0], board[2][1], board[2][2]], {0: [2,0], 1: [2,1], 2: [2,2]}])
		lines.append([[board[0][0], board[1][0], board[2][0]], {0: [0,0], 1: [1,0], 2: [2,0]}])
		lines.append([[board[0][1], board[1][1], board[2][1]], {0: [0,1], 1: [1,1], 2: [2,1]}])
		lines.append([[board[0][2], board[1][2], board[2][2]], {0: [0,2], 1: [1,2], 2: [2,2]}])
		lines.append([[board[0][0], board[1][1], board[2][2]], {0: [0,0], 1: [1,1], 2: [2,2]}])
		lines.append([[board[0][2], board[1][1], board[2][0]], {0: [0,2], 1: [1,1], 2: [2,0]}])
		return lines

	def block_opponent(self, line):
		free_moves = [i for i,x in enumerate(line) if x == ' ']
		moves_taken_by_player = [j for j,x in enumerate(line) if x == self.player]

		if len(free_moves) == 1 and len(moves_taken_by_player) == 0:
			return free_moves[0]

	def find_corner(self, board):
		corners = [[0,0], [0,2], [2,0], [2,2]]
		for corner in corners:
			if board[corner[0]][corner[1]] == ' ':
				return corner

	def find_free_space(self, board):
		for x, line in enumerate(board):
			for y, move in enumerate(line):
				if move == ' ':
					return [x, y]


	def move(self, board):
		for line in self.get_all_lines(board):
			move = self.block_opponent(line[0])
			if move is not None:
				return line[1][move]
		corner = self.find_corner(board)
		if corner is not None:
			return corner
		return self.find_free_space(board)