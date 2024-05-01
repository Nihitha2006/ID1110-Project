def play(black_strategy, white_strategy):
    board = initial_board()
    player = BLACK
    while player is not None:
        if player==WHITE:
            print("Choose WHITE's move.....................................................")
            move = get_move(white_strategy, player, board)
        else:
            print("Choose BLACK's move.....................................................")
            move = get_move(black_strategy, player, board)
        make_move(move, player, board)
        black,white=score(board)
        print("Black:",black,"White:",white)
        player = next_player(board, player)
    return board, final_score(board)
final_board,final_score=play(human_strategy,human_strategy)
print(print_board(final_board))
if final_score==0:
    print("*******************DRAW*************************")
elif final_score>0:
    print("*************YOU HAVE WON************************")
else:
    print("*************YOU LOSE****************************")
