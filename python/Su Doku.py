def entropy(i,j,table) -> set:
    available = set(range(1,10)).difference(getRow(i,j,table).union(getCol(i,j,table),getSquare(i,j,table)))
    return available

def getRow(i,j,table) -> set:
    temp = table[i]
    row = set(map(int,temp))-{0}
    return row

def getCol(i,j,table) -> set:
    temp = list(zip(*table[::-1]))
    col = set(map(int, temp[j]))-{0}
    return col

def getSquare(i,j,table) -> set:
    x, y = i//3, j//3
    square = set(map(int, table[a][y*3:y*3+3]) for a in range(x*3,x*3+3))
    return square

def print_board(bo):
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

for i in range(len(tables)):
    print(f"Grid {i+1}")
    table = tables[i]
    print_board(table)
    print("")
    k = 0
    while k < len(table):
        l = 0
        while l < len(table[0]):
            cell = table[k][l]
            if cell == 0:
                ent = entropy(k,l,table)
                if len(ent) == 1:
                    table[k][l] = list(ent)[0]
                    k,l = 0,0
            l += 1
        k += 1
    print_board(table)