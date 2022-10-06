from time import process_time

def print_board(bo):
    print("")
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("———————|————————|——————")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def find_zero(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i,j

def valid(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    
    for i in range(pos[0]//3 * 3,pos[0]//3 * 3 +3):
        for j in range(pos[1]//3 * 3,pos[1]//3 * 3+3):
            if board[i][j] == num and pos != (i,j):
                return False
    
    return True


def solve(board):
    position = find_zero(board)
    if not position:
        return True
    else:
        row, col = position
    
    for i in range(1,10):
        if valid(board, i,(row,col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

with open("p096_sudoku.txt") as f:
    tables = []
    for i in range(50):
        table = []
        for j in range(10):
            row = f.readline().strip("\n")
            if "Grid" in row:
                table.append(row)
                continue
            row = list(map(int,list(row)))
            table.append(row)
        tables.append(table[1:])

ans = 0
for i in range(len(tables)):
    table = tables[i]
    print(f"Grid {i+1}")
    print_board(table)
    solve(table)
    print_board(table)
    ans += table[0][0]*100 + table[0][1]*10 + table[0][2] 
    print("————————————————————————————————————")

print(f"Answer is {ans}. Time elapsed: {round(process_time(),3)}.")