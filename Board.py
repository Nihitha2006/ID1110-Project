EMPTY, BLACK, WHITE, OUTER = '.', 'B', 'W', '?'
PIECES = (EMPTY, BLACK, WHITE, OUTER)
PLAYERS = {BLACK: 'Black', WHITE: 'White'}

UP, DOWN, LEFT, RIGHT = -10, 10, -1, 1
UP_RIGHT, DOWN_RIGHT, DOWN_LEFT, UP_LEFT = -9, 11, 9, -11
DIRECTIONS = (UP, UP_RIGHT, RIGHT, DOWN_RIGHT, DOWN, DOWN_LEFT, LEFT, UP_LEFT)

print("IT'S PLAY TIME !!!")

#returns list of valid squares/moves
def squares():
    return [i for i in range(11, 89) if 1 <= (i % 10) <= 8]

# returns list of actual board
def initial_board():
    board = [OUTER] * 100 #->['?','?','?'....]
    for i in squares():
        board[i] = EMPTY
    board[44], board[45] = BLACK,WHITE
    board[54], board[55] =  WHITE,BLACK
    return board

# to print actual 8x8 board
def print_board(board):
    rep = ''
    rep += '  %s\n' % ' '.join(map(str, range(1, 9)))
    for row in range(1, 9):
        begin, end = 10*row + 1, 10*row + 9
        rep += '%d %s\n' % (row, ' '.join(board[begin:end]))
    return rep
