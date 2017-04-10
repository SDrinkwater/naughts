import signal
import sys
from bot import Bot


def coordinate_to_board_position(coordinate):
    x_plane = {'A': 0, 'B': 1, 'C': 2}
    y_plane = {'1': 0, '2': 1, '3': 2}

    return [y_plane[coordinate[1]], x_plane[coordinate[0]]]


def game_over(moves):
    if moves[0][0] != ' ' and moves[0][0] == moves[0][1] == moves[0][2]:
        return moves[0][0]
    if moves[0][0] != ' ' and moves[0][0] == moves[1][0] == moves[2][0]:
        return moves[0][0]
    if moves[0][0] != ' ' and moves[0][0] == moves[1][1] == moves[2][2]:
        return moves[0][0]
    if moves[0][2] != ' ' and moves[0][2] == moves[1][2] == moves[2][2]:
        return moves[0][2]
    if moves[0][2] != ' ' and moves[0][2] == moves[1][1] == moves[2][0]:
        return moves[0][2]
    if moves[2][0] != ' ' and moves[2][0] == moves[2][1] == moves[2][2]:
        return moves[2][0]
    if moves[1][0] != ' ' and moves[1][0] == moves[1][1] == moves[1][2]:
        return moves[1][0]


def print_board(moves):
    y_coords_to_line = {1: 0, 4: 1, 7: 2}
    line_to_x_coords = {0: 3, 1: 8, 2: 13}
    board = [
        '      |   |     ',
        '1     |   |     ',
        ' _____|___|_____',
        '      |   |     ',
        '2     |   |     ',
        ' _____|___|_____',
        '      |   |     ',
        '3     |   |     ',
        '      |   |     ',
        '   A    B    C  ',
    ]

    for idx, line in enumerate(board):
        line_as_list = list(line)
        if idx in [1, 4, 7]:
            for idx_moves, move in enumerate(moves[y_coords_to_line[idx]]):
                line_as_list[line_to_x_coords[idx_moves]] = move

        print(''.join(line_as_list))


def get_valid_move(player, moves):
    while True:
        try:
            response = input('Player {0}\'s turn: '.format(player)).upper()
            if response == 'Q':
                sys.exit(0)
            print(response)
            if len(response) == 2 and 'A' <= response[0] <= 'C' and 0 < int(response[1]) < 4:
                move = coordinate_to_board_position(response)
                if moves[move[0]][move[1]] != ' ':
                    raise ValueError('That move is already taken!')
                else:
                    return move
            raise ValueError('Please enter a valid move, i.e., "A1"\n')
        except ValueError as error:
            print(error)
            continue


def get_input(message, options=['y', 'n']):
    while True:
        response = input(message).lower()
        if len(options) > 0:
            if response in options:
                return response
        else:
            return response


def play_game(players):
    moves_taken = 0
    moves = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]
    b = Bot('X')
    winner = None

    while moves_taken < 9:
        player = players[moves_taken % 2]
        print_board(moves)
        print('Moves:', moves_taken)

        if player == 'X':
            move = b.move(moves)
        else:
            move = get_valid_move(player, moves)

        moves[int(move[0])][int(move[1])] = player
        moves_taken += 1
        winner = game_over(moves)
        if winner:
            break
    print_board(moves)
    if winner:
        print('\n{0} wins the game!\n'.format(player))
    else:
        print('\nDraw!\n')


def signal_handler(signal, frame):
    print('\n')
    sys.exit(0)


def main():
    players = ['X', 'O']

    while True:
        play_game(players)
        if get_input('Play again? (y/n) ') == 'n':
            break


signal.signal(signal.SIGINT, signal_handler)
main()
