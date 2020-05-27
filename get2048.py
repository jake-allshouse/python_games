import random

name = '2048'

def get_new_board():
    return [[0]*4, [0]*4, [0]*4, [0]*4]

def print_board(board):
    for row in board:
        print('{} {} {} {}'.format(*['{: 4d}'.format(n) if n > 0 else '   _' for n in row]))
    print('--------------------------------')


def get_available(board):
    return [(r,c) for r in range(0, 4) for c in range(0, 4) if board[r][c] == 0]

def add_number(board):
    available = get_available(board)
    if not available:
        raise Exception('No tiles left')
    number = random.randint(1, 2) * 2
    location = available[random.randrange(0, len(available))]
    board[location[0]][location[1]] = number

def shift_numbers(numbers):
    nonzeros = [n for n in numbers if n > 0]
    previous = 0
    new_numbers = []
    for index in range(len(nonzeros) - 1, -1, -1):
        if nonzeros[index] == previous:
            new_numbers.insert(0, previous * 2)
            previous = 0
        else:
            if previous:
                new_numbers.insert(0, previous)
            previous = nonzeros[index]
    if previous:
        new_numbers.insert(0, previous)
    for x in range(0, 4-len(new_numbers)):
        new_numbers.insert(0, 0)

    return new_numbers

def shift_board(board, direction):
    new_board = []
    if direction == 'r' or direction == 'l':
        for row_index in range(0, 4):
            row = board[row_index].copy()

            if direction == 'l':
                row.reverse()

            row = shift_numbers(row)

            if direction == 'l':
                row.reverse()

            new_board.append(row)
    elif direction == 'u' or direction == 'd':
        new_board = get_new_board()
        for column_index in range(0, 4):
            column = [board[r][column_index] for r in range(0, 4)]

            if direction == 'u':
                column.reverse()

            column = shift_numbers(column)

            if direction == 'u':
                column.reverse()

            for row_index in range(0, 4):
                new_board[row_index][column_index] = column[row_index]
    else:
        raise Exception('Invalid direction')
        
    return new_board

def manual_strategy(last_move_changed_board):
    return input('Direction (U)p, (D)own, (L)eft, (R)ight, or (Q)uit? ').strip().casefold()

auto1_state = {'index': 0}

def auto_strategy1(last_move_changed_board):
    moves = ['u', 'r', 'd', 'l']
    index = auto1_state['index']
    auto1_state['index'] = (index + 1) % 4
    return moves[index]

auto2_state = {'index': 0}

def auto_strategy2(last_move_changed_board):
    moves = ['d', 'r', 'l', 'u']
    index = auto2_state['index']
    if not last_move_changed_board:
        auto2_state['index'] = (index + 1) % 4
    else:
        auto2_state['index'] = 0
    return moves[index]

auto3_state = {'index': 0}

def auto_strategy3(last_move_changed_board):
    moves = ['u', 'r', 'd', 'l', 'u']
    index = auto3_state['index']
    auto3_state['index'] = (index + 1) % 4
    return moves[index]


def play_game(strategy = manual_strategy, show_board = True):
    board = get_new_board()
    add_number(board)

    changed = True
    while True:        
        available = get_available(board)

        if not available and \
            board == shift_board(board, 'r') and \
            board == shift_board(board, 'l') and \
            board == shift_board(board, 'u') and \
            board == shift_board(board, 'd'):
            if show_board:
                print('No moves. Game over.')
            break
        
        if available and changed:            
            add_number(board)

        if show_board:
            print_board(board)

        direction = strategy(changed)

        if direction == 'q':
            break
        elif direction not in ('u', 'd', 'l', 'r'):
            print('Invalid direction')
            changed = False
            continue

        previous_board = board
        board = shift_board(board, direction)
        changed = board != previous_board
    return board
        

def test_strats(strategies, games):
    counter = 0
    stats = {}
    for strategy in strategies:
        counter += 1
        name = 'Strategy {}'.format(counter)
        max_highest = 0
        for game_number in range(0, games):
            board = play_game(strategy, show_board=False)
            flat_board = []
            for row in board:
                flat_board.extend(row)
            highest = max(flat_board)
            max_highest = max(highest, max_highest)
        stats[name] = max_highest
    return stats

def quick_test(games):
    strats = [auto_strategy1, auto_strategy2, auto_strategy3]
    stats = test_strats(strats, games)
    print(stats)

if __name__ == "__main__":
    #quick_test(10)
    play_game()