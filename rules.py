def is_valid(move):
    return int(move) and move in squares()

#alternate turns for each player
def opponent(player):
    return BLACK if player is WHITE else WHITE


#
def make_move(move, player, board):
    board[move] = player
    for d in (UP, UP_RIGHT, RIGHT, DOWN_RIGHT, DOWN, DOWN_LEFT, LEFT, UP_LEFT):
        make_flips(move, player, board, d)
    return board


def make_flips(move, player, board, direction):
    bracket = find_bracket(move, player, board, direction)
    if not bracket:
        return
    square = move + direction
    while square != bracket:
        board[square] = player
        square += direction



def is_legal(move, player, board):
    hasbracket = lambda direction: find_bracket(move, player, board, direction)
    return board[move] == EMPTY and any(map(hasbracket, DIRECTIONS))

def any_legal_move(player, board):
    return any(is_legal(sq, player, board) for sq in squares())

def next_player(board, prev_player):
    opp = opponent(prev_player)
    if any_legal_move(opp, board):
        return opp
    elif any_legal_move(prev_player, board):
        return prev_player
    return None


def get_move(strategy, player, board):
    copy = list(board) # copy the board to prevent cheating
    move = strategy(player, copy)
    if not is_valid(move) or not is_legal(move, player, board):
        print("Invalid Move")
        return get_move(strategy, player, board)
    return move

def find_bracket(square, player, board, direction):
    bracket = square + direction
    if board[bracket] == player:
        return None
    opp = opponent(player)
    while board[bracket] == opp:
        bracket += direction
    return None if board[bracket] in (OUTER, EMPTY) else bracket


def legal_moves(player, board):
    return [sq for sq in squares() if is_legal(sq, player, board)]

def human_strategy(player,board):
    print(print_board(board))
    print(legal_moves(player,board))
    user=int(input("Enter your choice"))
    return user
