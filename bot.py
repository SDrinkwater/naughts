from random import randint


class Bot:
    """A simple naughts and crosses bot.

    This bot uses the following process to find a move:
        Move 1: Go in a corner.
        Move 2: If the other player did not go there then go in the opposite corner to move 1.
        Otherwise go in a free corner.
        Move 3: If there are two Xs and a space in a line (in any order) then go in that space.
        Otherwise if there are two Os and a space in a line then go in that space. Otherwise go in a free corner.
        Move 4: If there are two Xs and a space in a line (in any order) then go in that space.
        Otherwise if there are two Os and a space in a line then go in that space. Otherwise go in a free corner.
        Move 5: Go in the free space.

    Attributes:
        player: A string indicating the player controlled by the bot.
    """

    def __init__(self, player):
        self.player = player

    @staticmethod
    def get_all_lines(board):
        lines = []
        lines.append([[board[0][0], board[0][1], board[0][2]], {0: [0, 0], 1: [0, 1], 2: [0, 2]}])
        lines.append([[board[1][0], board[1][1], board[1][2]], {0: [1, 0], 1: [1, 1], 2: [1, 2]}])
        lines.append([[board[2][0], board[2][1], board[2][2]], {0: [2, 0], 1: [2, 1], 2: [2, 2]}])
        lines.append([[board[0][0], board[1][0], board[2][0]], {0: [0, 0], 1: [1, 0], 2: [2, 0]}])
        lines.append([[board[0][1], board[1][1], board[2][1]], {0: [0, 1], 1: [1, 1], 2: [2, 1]}])
        lines.append([[board[0][2], board[1][2], board[2][2]], {0: [0, 2], 1: [1, 2], 2: [2, 2]}])
        lines.append([[board[0][0], board[1][1], board[2][2]], {0: [0, 0], 1: [1, 1], 2: [2, 2]}])
        lines.append([[board[0][2], board[1][1], board[2][0]], {0: [0, 2], 1: [1, 1], 2: [2, 0]}])
        return lines

    def block_opponent(self, line):
        free_moves = [i for i, x in enumerate(line) if x == ' ']
        moves_taken_by_player = [j for j, x in enumerate(line) if x == self.player]
        moves_taken_by_opponent = [j for j, x in enumerate(line) if x != self.player and x != ' ']

        if len(free_moves) == 1 and len(moves_taken_by_opponent) == 0:
            return free_moves[0], True

        if len(free_moves) == 1 and len(moves_taken_by_player) == 0:
            return free_moves[0], False

        return -1, False

    @staticmethod
    def find_corners(board):
        corners = [[0, 0], [2, 2], [0, 2], [2, 0]]
        free_corners = []
        for corner in corners:
            if board[corner[0]][corner[1]] == ' ':
                free_corners.append(corner)

        return free_corners

    @staticmethod
    def find_free_space(board):
        for x, line in enumerate(board):
            for y, move in enumerate(line):
                if move == ' ':
                    return [x, y]

    def move(self, board):
        move = []
        for line in self.get_all_lines(board):
            new_move, win = self.block_opponent(line[0])
            if win:
                return line[1][new_move]

            if new_move >= 0:
                move = line[1][new_move]

        if len(move) > 0:
            return move

        corners = self.find_corners(board)
        if len(corners) > 0:
            idx = randint(0, len(corners) - 1)
            return corners[idx]
        return self.find_free_space(board)
