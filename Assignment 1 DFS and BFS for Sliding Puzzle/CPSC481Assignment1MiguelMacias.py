# Sliding Puzzle
# Miguel Macias
# CPSC 481
# Creating a DFS and BFS algorithm to solve a sliding puzzle
# 3x3 Does not work

# Helps keep track of puzzle states
class PuzzleState:
    cells = []
    emptySpot = None


tempCells = []


def main():
    initialState2x = [0, 3, 2, 1]
    goalState2x = [1, 2, 3, 0]
    puzzleSize = 2 if len(initialState2x) - 1 % 3 == 0 else 1
    puzzleSolver(initialState2x, goalState2x, puzzleSize)

    initalState3x = [1, 4, 3, 7, 0, 6, 5, 8, 2]
    goalState3x = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    puzzleSize = 2 if len(initalState3x) - 1 % 3 == 0 else 1
    puzzleSolver(initalState3x, goalState3x, puzzleSize)


def puzzleSolver(initalList, goalList, puzzleSize):

    # Creating tuples for set
    goalTuple = tuple(map(tuple, convertBoard(goalList, puzzleSize)))
    initalTuple = tuple(map(tuple, convertBoard(initalList, puzzleSize)))
    visitedStates = set()
    visitedStates.add(initalTuple)
    stack = [initalList]
    queue = [initalList]
    count = 1

    # Haven't gone thorugh every possible move\
    # DFS
    print("DFS Search")
    while len(stack) != 0:
        listOfBoards = tuple(map(tuple, possibleBoards(
            convertBoard(stack.pop(), puzzleSize), puzzleSize)))

        for board in listOfBoards:

            board = tuple(map(tuple, board))
            printMatrix(board, count)
            count += 1

            if(board == goalTuple):
                print("Solution found in DFS \n \n")
                stack.clear()
                break

            elif board not in visitedStates:
                visitedStates.add(board)
                board = list(board)
                board = [item for t in board for item in t]
                stack.append(board)

    # BFS
    # Reinitialize
    visitedStates.clear()
    visitedStates.add(initalTuple)
    count = 1

    print("BFS Search")
    while len(queue) != 0:
        listOfBoards = tuple(map(tuple, possibleBoards(
            convertBoard(queue.pop(0), puzzleSize), puzzleSize)))
        for board in listOfBoards:
            board = tuple(map(tuple, board))
            printMatrix(board, count)
            count += 1

            if(board == goalTuple):
                print("SOLUTION found in BFS")
                return

            elif board not in visitedStates:
                visitedStates.add(board)
                board = list(board)
                board = [item for t in board for item in t]
                queue.append(board)


# Looks at all possible moves

# Print current state
def printMatrix(matrix, count):
    matrix = list(matrix)
    matrix = [item for t in matrix for item in t]
    matrixString = ""
    for array in matrix:
        matrixString = matrixString + str(array)

    # rows
    for i in range(0, 4, 2):
        print(matrixString[i], matrixString[i+1])

    print("This is state: ", count)
    print(" |")
    print(" |")
    print(" V")


def possibleBoards(board, puzzleSize):
    board = board
    emptySpot = None
    possibleBoards = []
    directions = []

    # Different conditions for different size board
    if puzzleSize == 1:
        # Get blank location for possible moves
        for rows in range(puzzleSize + 1):

            for cols in range(puzzleSize + 1):

                if board[rows][cols] == 0:
                    # Find where the empty spot is
                    emptySpot = rows, cols
                    # Make sure to not go out of bounds
                    directions = calculateUsuableMoves(
                        emptySpot, puzzleSize)

        for a in directions:
            possibleBoards.append(genBoards(a, emptySpot, puzzleSize))

    elif puzzleSize == 2:
        for rows in range(puzzleSize + 1):

            for cols in range(puzzleSize + 1):
                if board[rows][cols] == 0:
                    # Find where the empty spot is
                    emptySpot = rows, cols
                    # Make sure to not go out of bounds
                    directions = calculateUsuableMoves(
                        emptySpot, puzzleSize)

        for a in directions:
            possibleBoards.append(genBoards(a, emptySpot, puzzleSize))

    return possibleBoards


# Return 2D converted array

def convertBoard(board, puzzleSize):
    puzzle = PuzzleState()
    cells = []
    board = list(board)
    board = board[:]
    board.reverse()  # Easier to pop
    global tempCells

    count = 0
    for rows in range(puzzleSize + 1):
        cells.append([])
        for cols in range(puzzleSize + 1):
            count += 1
            cells[rows].append(board.pop())

    puzzle.cells = cells
    tempCells = [values[:] for values in cells]
    return cells

# Look at all legal moves that can be done


def calculateUsuableMoves(emptySpot, puzzleSize):
    possibleMoves = []
    rows, cols = emptySpot

    if rows > 0:
        possibleMoves.append("UP")
    if cols > 0:
        possibleMoves.append("LEFT")
    if rows < puzzleSize:
        possibleMoves.append("DOWN")
    if cols < puzzleSize:
        possibleMoves.append("RIGHT")

    return possibleMoves


# Generates the actual boards

def genBoards(direction, emptySpot, puzzleSize):
    rows, cols = emptySpot

    if direction == 'UP':
        newcols = cols
        newrows = rows - 1

    elif direction == 'DOWN':
        newcols = cols
        newrows = rows + 1

    elif direction == 'LEFT':
        newcols = cols - 1
        newrows = rows

    elif direction == 'RIGHT':
        newcols = cols + 1
        newrows = rows

    newPuzzle = PuzzleState()
    newPuzzle.cells = [values[:] for values in tempCells]
    newPuzzle.cells[rows][cols] = tempCells[newrows][newcols]
    newPuzzle.cells[newrows][newcols] = tempCells[rows][cols]
    newPuzzle.emptySpot = newrows, newcols

    return newPuzzle.cells


def change2Dto1D(twoDArray):
    oneDArray = []
    for i in twoDArray:
        oneDArray = oneDArray + list(sum(i, ()))

    return


main()
