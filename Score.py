def score(board):
    mine, theirs = 0, 0
    for sq in squares():
        piece = board[sq]
        if piece == BLACK: mine += 1
        elif piece == WHITE: theirs += 1
    return mine,theirs

def score_diff(player, board):
    mine, theirs = 0, 0
    opp = opponent(player)
    for sq in squares():
        piece = board[sq]
        if piece == player: mine += 1
        elif piece == opp: theirs += 1
    return mine-theirs
