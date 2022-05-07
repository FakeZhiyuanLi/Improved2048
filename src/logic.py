import random

def initBoard(rows, cols):
    board = []
    for i in range(rows):
        board.append([0] * cols)
    return board

def startGame(rows, cols):
    board = initBoard(rows, cols)

    board = addTile()
    board = addTile()

    return board

def openSpace(board):
    for row in board:
        if 0 in row:
            return True
    return False

def addTile(board):
    while openSpace(board):
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board[0]) - 1)
        tileValue = random.randint(0, 3) # if 0-2 set tile to 2, if 3 set tile to 4

        if board[row][col] == 0:
            if tileValue <= 2:
                board[row][col] = 2
            else:
                board[row][col] = 4
            break
                
def left(board):
    pass

def right(board):
    pass

def up(board):
    pass

def down(board):
    pass

def gameOver(board):
    pass

if __name__ == '__main__':
    test_board = initBoard(4, 4)
    print(test_board)

    addTile(test_board)
    print(test_board)

    addTile(test_board)
    print(test_board)
    