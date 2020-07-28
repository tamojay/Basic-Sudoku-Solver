import pprint

def solve(bo):
    find = find_empty(bo)
    if find:
        row, col = find
    else:
        return True

    for i in range(1, 10):
        if valid(bo, (row, col), i):
            bo[row][col] = i

            if (solve(bo)):
                return True
            
            bo[row][col] = 0
    return False

def valid(bo, pos, num):
    # Check row
    for i in range(0, len(bo)):
        if bo[pos[0]][i] == num and pos[1] != 1:
            return False
    
    # Check column
    for i in range(0, len(bo)):
        if bo[i][pos[1]] == num and pos[1] != 1:
            return False
    
    # Check box
    xbox = pos[1]//3
    ybox = pos[0]//3

    for i in range(ybox*3, ybox*3 + 3):
        for j in range(xbox*3, xbox*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True

def find_empty(bo):
    for i in range(len(bo[0])):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i,j)        
    return None

def main():
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    pp = pprint.PrettyPrinter(width=41, compact=True)
    solve(board)
    pp.pprint(board)

main()
