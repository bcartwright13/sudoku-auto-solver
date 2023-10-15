def solve(board):

    return

def generatePossibleNumber():
    
    
    return

def usedNumbers(board):
    rowNumbers = {}
    columnNumbers = {}
    squareNumbers = {}
    for i in range(len(board)):
        rowNumbers[i] = set()
        columnNumbers[i] = set()
        for j in range(len(board[i])):
            if board[i][j] != 0:
                rowNumbers[i].add(board[i][j])
            if board[j][i] != 0:
                columnNumbers[i].add(board[j][i])
                



sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
