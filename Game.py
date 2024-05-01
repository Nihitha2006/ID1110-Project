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
    return board, score_diff(player,board)
final_board,score_diff=play(human_strategy,human_strategy)
print(print_board(final_board))
if score_diff==0:
    print("*******************DRAW*************************")
elif score_diff>0:
    print("*************WHITE WON,BLACK LOSE************************")
else:
    print("*************BLACK WON,WHITE LOSE****************************")
