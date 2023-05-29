from studentA import print_board, is_game_over, new_board
from studentB import ai_move, is_player_starting, get_user_move

# from ... import announce_outcome

board = new_board()
players_move = is_player_starting()
while not is_game_over(board):
    print_board(board)
    choice = get_user_move()
    if (players_move):
        board[choice]='X'
    else:
        board[choice] = 'O'


    players_move = not players_move

#announce_outcome(board,players_move)