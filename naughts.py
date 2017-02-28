
def coordinate_to_board_position(coordinate):
    x_plane = {'A': 0, 'B': 1, 'C': 2}
    y_plane = {'1': 0, '2': 1, '3': 2}

    return [y_plane[coordinate[1]], x_plane[coordinate[0]]]


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
            response = input('{0}\'s turn: '.format(player)).upper()
            if len(response) == 2 and response[0] >= 'A' and response[0] <= 'C' and int(response[1]) >= 1 and int(response[1]) <= 3:
                xy = coordinate_to_board_position(response)
                if moves[xy[0]][xy[1]] == ' ':
                    return response
        except:
            print("Please enter your move as a letter and a number: \"A1\"\n")
            continue


def main():
    moves_taken = 0
    moves = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]
    players = ['X', 'O']

    while moves_taken < 9:
        player = players[moves_taken % 2]
        print_board(moves)
        print('Moves:', moves_taken)

        move = coordinate_to_board_position(get_valid_move(player, moves))
        moves[int(move[0])][int(move[1])] = player
        moves_taken += 1
    print_board(moves)

main()
