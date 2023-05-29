new_board = [' '] * 9

def print_board(board):
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

def is_game_over():
    # Sprawdzenie, czy któryś gracz wygrał
    if (board[0] == board[1] == board[2] != ' ') or \
       (board[3] == board[4] == board[5] != ' ') or \
       (board[6] == board[7] == board[8] != ' ') or \
       (board[0] == board[3] == board[6] != ' ') or \
       (board[1] == board[4] == board[7] != ' ') or \
       (board[2] == board[5] == board[8] != ' ') or \
       (board[0] == board[4] == board[8] != ' ') or \
       (board[2] == board[4] == board[6] != ' '):
        return True

    # Sprawdzenie, czy doszło do remisu
    if ' ' not in board:
        return True

    return False


