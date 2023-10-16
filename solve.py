def solve(board):
    while True:
        rowNumbers, columnNumbers, squareNumbers = usedNumbers(board)
        possibleNumbers = generatePossibleNumber(board, rowNumbers, columnNumbers, squareNumbers)
        
        board, possibleNumbers, madeProgress = solveOnes(board, possibleNumbers)
        
        if not madeProgress:  
            break

    
    return board

def solveOnes(board, possibleNumbers):
    madeProgress = False
    for i in range(9):
        for j in range(9):
            if (i,j) in possibleNumbers and len(possibleNumbers[(i,j)]) == 1:
                    single_number = list(possibleNumbers[(i,j)])[0]
                    board[i][j] = single_number
                    del possibleNumbers[(i,j)]
                    madeProgress = True
                    
    return board, possibleNumbers, madeProgress
    
    


def generatePossibleNumber(board,rowNumbers, columnNumbers, squareNumbers):
    nums = set(range(1,10))
    possibleNumbers = {}
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                
                squareRow = 3 * (i // 3)
                squareCol = 3 * (j // 3)
                usedInRow = rowNumbers[i]
                usedInColumn = columnNumbers[j]
                usedInSquare = squareNumbers[(squareRow, squareCol)]
                usedNumbers = usedInRow | usedInColumn | usedInSquare
                possibleNums = nums - usedNumbers
                possibleNumbers[(i,j)] = possibleNums
    
    return possibleNumbers

def usedNumbers(board):
    rowNumbers = {}
    columnNumbers = {}
    squareNumbers = {}
    for i in range(len(board)):
        rowNumbers[i] = set()
        columnNumbers[i] = set()
        for j in range(len(board[i])):
            num = board[i][j]
            if num != 0:
                rowNumbers[i].add(board[i][j])
                
            
                squareRow = 3 * (i // 3)
                squareCol = 3 * (j // 3)
                if (squareRow, squareCol) not in squareNumbers:
                    squareNumbers[(squareRow, squareCol)] = set()
            
            
                squareNumbers[(squareRow, squareCol)].add(num)
            if board[j][i] != 0:
                columnNumbers[i].add(board[j][i])

    return rowNumbers, columnNumbers, squareNumbers
                




sudoku_board = [
    [0, 0, 3, 0, 2, 0, 6, 0, 0],
    [9, 0, 0, 3, 0, 5, 0, 0, 1],
    [0, 0, 1, 8, 0, 6, 4, 0, 0],
    [0, 0, 8, 1, 0, 2, 9, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 6, 7, 0, 8, 2, 0, 0],
    [0, 0, 2, 6, 0, 9, 5, 0, 0],
    [8, 0, 0, 2, 0, 3, 0, 0, 9],
    [0, 0, 5, 0, 1, 0, 3, 0, 0]
]


print(solve(sudoku_board))
