import random

def initBoard(rows, cols):
    board = []
    for i in range(rows):
        board.append([0] * cols)
    return board

def startGame(rows, cols):
    board = initBoard(rows, cols)
    
    board = addTile(board)
    board = addTile(board)

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
    score = 0
    merged = set()
    AddTile = False
    for i in range(1, 0, -1):
        for j in range(0, 4):
            if board[j][i] == 0:
                continue
            if board[j][i-1] == board[j][i] and (j, i) not in merged:
                board[j][i-1] *= 2
                board[j][i] = 0
                score += board[j][i-1]
                for x in range(0, j + 1):
                    merged.add((x, i))
                AddTile = True
            else:
                if board[j][i-1] == 0:
                    board[j][i-1] = board[j][i]
                    board[j][i] = 0
                    AddTile = True
    for i in range(2, 0, -1):
        for j in range(0, 4):
            if board[j][i] == 0:
                continue
            if board[j][i-1] == board[j][i] and (j, i) not in merged:
                board[j][i-1] *= 2
                board[j][i] = 0
                score += board[j][i-1]
                for x in range(0, j + 1):
                    merged.add((x, i))
                AddTile = True
            else:
                if board[j][i-1] == 0:
                    board[j][i-1] = board[j][i]
                    board[j][i] = 0
                    AddTile = True
    for i in range(3, 0, -1):
        for j in range(0, 4):
            if board[j][i] == 0:
                continue
            if board[j][i-1] == board[j][i] and (j, i) not in merged:
                board[j][i-1] *= 2
                board[j][i] = 0
                score += board[j][i-1]
                for x in range(0, j + 1):
                    merged.add((x, i))
                AddTile = True
            else:
                if board[j][i-1] == 0:
                    board[j][i-1] = board[j][i]
                    board[j][i] = 0
                    AddTile = True
    if AddTile:
        addTile(board)
    return score

def right(board):
    score = 0
    merged = set()
    AddTile = False

    for i in range(2, 3):
        for j in range(0, 4):
            if board[j][i] == 0:
                continue
            if board[j][i] == board[j][i+1] and (j, i) not in merged:
                board[j][i+1] *= 2
                board[j][i] = 0
                score += board[j][i+1]
                for x in range(i+1, len(board)):
                    merged.add((j, x))
                AddTile = True
            else:
                if board[j][i+1] == 0:
                    board[j][i+1] = board[j][i]
                    board[j][i] = 0
                    AddTile = True
    for i in range(1, 3):
        for j in range(0, 4):
            if board[j][i] == 0:
                continue
            if board[j][i] == board[j][i+1] and (j, i) not in merged:
                board[j][i+1] *= 2
                board[j][i] = 0
                score += board[j][i+1]
                for x in range(i+1, len(board)):
                    merged.add((j, x))
                AddTile = True
            else:
                if board[j][i+1] == 0:
                    board[j][i+1] = board[j][i]
                    board[j][i] = 0
                    AddTile = True
    for i in range(0, 3):
        for j in range(0, 4):
            if board[j][i] == 0:
                continue
            if board[j][i] == board[j][i+1] and (j, i) not in merged:
                board[j][i+1] *= 2
                board[j][i] = 0
                score += board[j][i+1]
                for x in range(i+1, len(board)):
                    merged.add((j, x))
                AddTile = True
            else:
                if board[j][i+1] == 0:
                    board[j][i+1] = board[j][i]
                    board[j][i] = 0
                    AddTile = True
    if AddTile:
        addTile(board)
    return score

def up(board):
    score = 0
    merged = set()
    AddTile = False
    for i in range(1, 0, -1):
        for j in range(0, 4):
            if board[i][j] == 0:
                continue
            if board[i-1][j] == board[i][j] and (i, j) not in merged:
                board[i-1][j] *= 2
                board[i][j] = 0
                score += board[i-1][j]
                for x in range(0, i+1):
                    merged.add((x, j))
                AddTile = True
            else:
                if board[i-1][j] == 0:
                    board[i-1][j] = board[i][j]
                    board[i][j] = 0
                    AddTile = True
    for i in range(2, 0, -1):
        for j in range(0, 4):
            if board[i][j] == 0:
                continue
            if board[i-1][j] == board[i][j] and (i, j) not in merged:
                board[i-1][j] *= 2
                board[i][j] = 0
                score += board[i-1][j]
                for x in range(0, i+1):
                    merged.add((x, j))
                AddTile = True
            else:
                if board[i-1][j] == 0:
                    board[i-1][j] = board[i][j]
                    board[i][j] = 0
                    AddTile = True
    for i in range(3, 0, -1):
        for j in range(0, 4):
            if board[i][j] == 0:
                continue
            if board[i-1][j] == board[i][j] and (i, j) not in merged:
                board[i-1][j] *= 2
                board[i][j] = 0
                score += board[i-1][j]
                for x in range(0, i+1):
                    merged.add((x, j))
                AddTile = True
            else:
                if board[i-1][j] == 0:
                    board[i-1][j] = board[i][j]
                    board[i][j] = 0
                    AddTile = True
    if AddTile:
        addTile(board)
    return score

def down(board):
    score = 0
    merged = set()
    AddTile = False
    for i in range(2, 3):
        for j in range(0, 4):
            if board[i][j] == 0:
                continue
            if board[i][j] == board[i+1][j] and (i+1, j) not in merged:
                board[i+1][j] *= 2
                board[i][j] = 0
                score += board[i+1][j]
                for x in range(i+1, len(board)):
                    merged.add((x, j))
                AddTile = True
            else:
                if board[i+1][j] == 0:
                    board[i+1][j] = board[i][j]
                    board[i][j] = 0
                    AddTile = True
    for i in range(1, 3):
        for j in range(0, 4):
            if board[i][j] == 0:
                continue
            if board[i][j] == board[i+1][j] and (i+1, j) not in merged:
                board[i+1][j] *= 2
                board[i][j] = 0
                score += board[i+1][j]
                for x in range(i+1, len(board)):
                    merged.add((x, j))
                AddTile = True
            else:
                if board[i+1][j] == 0:
                    board[i+1][j] = board[i][j]
                    board[i][j] = 0
                    AddTile = True
    for i in range(0, 3):
        for j in range(0, 4):
            if board[i][j] == 0:
                continue
            if board[i][j] == board[i+1][j] and (i+1, j) not in merged:
                board[i+1][j] *= 2
                board[i][j] = 0
                score += board[i+1][j]
                for x in range(i+1, len(board)):
                    merged.add((x, j))
                AddTile = True
            else:
                if board[i+1][j] == 0:
                    board[i+1][j] = board[i][j]
                    board[i][j] = 0
                    AddTile = True
    if AddTile:
        addTile(board)
    return score

def gameOver(board):
    for row in board:
        for tile in row:
            if tile == 0:
                return False

    for i in range(0, len(board) - 1):
        for j in range(0, len(board[0])):
            if board[i][j] == board[i+1][j]:
                return False
    for i in range(0, len(board[0]) - 1):
        for j in range(0, len(board)):
            if board[j][i] == board[j][i+1]:
                return False

    return True
