import numpy as np

board = np.full((3,3), '')

def get_win(board):
    if np.any(board == ''):
        return 'None'
    for i in range(3):
        if np.all(board[i] == 'O') or np.all(board[:,i] == 'O'):
            return 'O'
        elif np.all(board[i] == 'X') or np.all(board[:,i] == 'X'):
            return 'X'
        else:
            return 'D'

def print_board(board):
    for i, row in enumerate(board):
        chs = []
        for j, ch in enumerate(row):
            if ch == '':
                ch = i * 3 + j + 1
            chs.append(ch)
        print(" ".join(chs))
            
current = 'X'
while get_win(board) == None:
    print(board)
    field = input(f'Player {current} enter field: ')

    try:
        field = int(field) - 1
        i = field // 3
        j = field % 3
    except:
        print('please enter valid field.')
        continue

    board[i,j] = current

    if current == 'X':
        current = 'O'
    else:
        current = 'X'

print(board)