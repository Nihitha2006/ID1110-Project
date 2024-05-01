def score(board):
    black_count, white_count = 0, 0
    for sq in squares():
        piece = board[sq]
        if piece == BLACK: black_count+= 1
        elif piece == WHITE: white_count += 1
    return black_count,white_count

def score_diff(player, board):
    black_count,white_count = 0, 0
    opp = opponent(player)
    for sq in squares():
        piece = board[sq]
        if piece == player: black_count += 1
        elif piece == opp:  white_count+= 1
    return black_count-white_count
