import random

rand = random.Random()
rand.seed(1)

def get_new_board():
    return [[0]*4, [0]*4, [0]*4, [0]*4]

def print_board(board):
    for row in board:
        print('{} {} {} {}'.format(*['{: 4d}'.format(n) if n > 0 else '   _' for n in row]))

def get_available(board):
    return [(r,c) for r in range(0, 4) for c in range(0, 4) if board[r][c] == 0]

def add_number(board):
    available = get_available(board)
    if not available:
        raise Exception('No tiles left')
    number = rand.randint(1, 2) * 2
    location = available[rand.randrange(0, len(available))]
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

def play_game():
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
            print('No moves. Game over.')
            break
        
        if available and changed:            
            add_number(board)
        print_board(board)

        direction = input('Direction (U)p, (D)own, (L)eft, (R)ight, or (Q)uit? ').strip().casefold()

        if direction == 'q':
            break
        elif direction not in ('u', 'd', 'l', 'r'):
            print('Invalid direction')
            changed = False
            continue

        previous_board = board
        board = shift_board(board, direction)
        changed = board != previous_board
        


if __name__ == "__main__":
    play_game()